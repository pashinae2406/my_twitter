from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.orm import selectinload
import models
import schemas
from database import engine, session, async_session
from typing import List
from pathlib import Path


app = FastAPI()
static_path = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=str(static_path), html=True), name="static")
app.mount("/css", StaticFiles(directory=str(static_path) + "/css"), name="css")
app.mount("/js", StaticFiles(directory=str(static_path) + "/js"), name="js")

templates = Jinja2Templates(directory="templates")

async def get_session():
    async with async_session() as s:
        yield s

@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get('/users', response_model=List[schemas.UserOut])
async def users() -> List[models.User]:
    """Ендпоинт для получения списка пользователей"""

    res = await session.execute(select(models.User))
    return res.scalars().all()

@app.get('/api/users/me')
async def user_me():
    async with session.begin():
        res = await session.execute(select(models.User).where(models.User.id == 1))
        user = res.scalar()
        return JSONResponse(
            {
                "result": True,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "followers": [],
                    "following": [],
                }
            }
        )

@app.get('/login')
def login():
    pass
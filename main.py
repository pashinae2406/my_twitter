from fastapi import FastAPI, Request, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse, RedirectResponse
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.orm import selectinload
import models
import schemas
from database import engine, session, async_session
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

@app.get('/api/users/me', response_model=schemas.UserOut)
async def user_me(api_key: str = Header()):
    """Ендпоинт для получения информации о своем профиле"""

    header_dict: dict = {'Api-Key': api_key}
    async with session.begin():
        res_user = await session.execute(select(models.User).where(models.User.api_key == header_dict['Api-Key']))
        user = res_user.scalar()
        if user:
            res_follower = await session.execute(select(models.Followers.follower_id).where(models.Followers.user_id == user.id))
            followers: list = []
            for fol in res_follower.scalars().all():
                res_name = await session.execute(select(models.User.name).where(models.User.id == fol))
                name: str = res_name.scalar()
                followers.append({"id": fol, "name": name})
            res_following = await session.execute(select(models.Followings.following_id).where(models.Followings.user_id == user.id))
            followings: list = []
            for fol in res_following.scalars().all():
                res_name = await session.execute(select(models.User.name).where(models.User.id == fol))
                name: str = res_name.scalar()
                followings.append({"id": fol, "name": name})
            return JSONResponse(
                {
                    "result": True,
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "followers": followers,
                        "following": followings,
                    }
                }
            )
        else:
            return JSONResponse(
                {
                    "result": False,
                    "user": {
                        "id": None,
                        "name": "Пользователь по указанному api-key не найден.",
                        "followers": [],
                        "following": [],
                    }
                }
            )



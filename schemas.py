from pydantic import BaseModel
from typing import List


class BaseUser(BaseModel):
    """Базовая схема ингредиента"""
    name: str
    phone: str

class UserIn(BaseUser):
    """Схема входных данных пользователя"""
    ...

class UserOut(BaseUser):
    """Схема выходных данных пользователя"""
    ...

    class Config:
        orm_mode = True

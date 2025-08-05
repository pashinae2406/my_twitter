from pydantic import BaseModel
from typing import List


class BaseFollower(BaseModel):
    """Базовая схема фалловера"""
    user_id: int
    follower_id: int

class FollowerIn(BaseFollower):
    """Схема входных данных фалловера"""
    ...

class FollowerOut(BaseFollower):
    """Схема выходных данных подписок"""
    ...

    class Config:
        orm_mode = True

class BaseFollowing(BaseModel):
    """Базовая схема подписок"""
    user_id: int
    following_id: int

class FollowingIn(BaseFollowing):
    """Схема входных данных подписок"""
    ...

class FollowingOut(BaseFollowing):
    """Схема выходных данных подписок"""
    ...

    class Config:
        orm_mode = True

class BaseUser(BaseModel):
    """Базовая схема ингредиента"""
    id: int
    name: str
    # api_key: str

class UserIn(BaseUser):
    """Схема входных данных пользователя"""
    ...

class UserOut(BaseUser):
    """Схема выходных данных пользователя"""
    follower_id: List[BaseUser] = []
    following_id: List[BaseUser] = []

    class Config:
        orm_mode = True
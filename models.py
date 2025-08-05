from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from typing import Dict, Any

from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    """Класс Пользователь"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    api_key = Column(String, index=True, unique=True)
    # follower_id = Column(Integer, ForeignKey('followers.follower_id'))
    # following_id = Column(Integer, ForeignKey('followings.following_id'))
    followers = relationship('Followers', back_populates='users')
    followings = relationship('Followings', back_populates='users')

    def __repr__(self):
        return f"User_id: {self.id}, name: {self.name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Followers(Base):
    """Класс Подписчики"""

    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    follower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship("User", back_populates="followers",
                         cascade="all", lazy="select")

class Followings(Base):
    """Класс Подписки пользователя"""

    __tablename__ = 'followings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    following_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship("User", back_populates="followings",
                         cascade="all", lazy="select")
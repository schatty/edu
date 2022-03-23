"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, declared_attr, relationship, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    def __repr__(self):
        return str(self)

    id = Column(Integer, primary_key=True)


# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base(bind=engine, cls=Base)


class User(Base):
    name = Column(String(), nullable=False)
    username = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"User id {self.id} (name={self.name}, "
            f"username={self.username}, email={self.email})"
        )


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text)

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return (f"Post id={self.id}\t{self.title!r}")


# session = AsyncSession(bind=engine)
Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


if __name__ == "__main__":
    print("session:", Session)

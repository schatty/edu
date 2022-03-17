"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from typing import List
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from models import engine, Base, User, Post, Session
from jsonplaceholder_requests import fetch_user, fetch_post, TOTAL_POSTS, TOTAL_USERS


async def init_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Schemas created.")


async def fetch_users_data() -> List[dict]:
    coros = [
        await fetch_user(user_id)
        for user_id in range(1, TOTAL_USERS + 1)
    ]
    return coros


async def fetch_posts_data() -> List[dict]:
    coros = [
        await fetch_post(post_id)
        for post_id in range(1, TOTAL_POSTS + 1)
    ]
    return coros

 
async def create_user(session: AsyncSession, name: str, username: str, email: str):
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()

    await session.refresh(user)
    print("Added user:", user)


async def create_post(session: AsyncSession, user_id: int, title: str, body: str = ""):
    post = Post(user_id=user_id, title=title, body=body)
    session.add(post)
    await session.commit()

    await session.refresh(post)
    print("Added post:", post)


async def upload_users(session, users_data: List[dict]):
    coros = [
        await create_user(session, name=user["name"], username=user["username"], email=user["email"])
        for user in users_data
    ]
    return coros


async def upload_posts(session, posts_data: List[dict]):
    coros = [
        await create_post(session, user_id=post["userId"], title=post["title"], body=post["body"])
        for post in posts_data
    ]
    return coros


async def async_main():
    # Creating schemas
    await init_schemas()

    # Fetching data from web

    users_data: List[dict]
    posts_data: List[dict]

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )
    print(f"Fetched {len(users_data)} users and {len(posts_data)} posts.users_data.")

    # Uploading data to DB

    async with Session() as session:
        await asyncio.gather(
            upload_users(session, users_data),
        )

        await asyncio.gather(
            upload_posts(session, posts_data)
        )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

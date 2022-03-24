"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from aiohttp import ClientSession
from loguru import logger


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

TOTAL_USERS = 10
TOTAL_POSTS = 100


async def fetch_json(session: ClientSession, url):
    async with session.get(url) as response:
        response_json = await response.json()
        return response_json


async def fetch_user(user_id: int):
    user_url = f"{USERS_DATA_URL}/{user_id}"
    async with ClientSession() as session:
        user_data = await fetch_json(session, user_url)

    return user_data 


async def fetch_all_users():
    async with ClientSession() as session:
        user_data = await fetch_json(session, USERS_DATA_URL)
    return user_data


async def fetch_post(post_id: int):
    post_url = f"{POSTS_DATA_URL}/{post_id}"
    async with ClientSession() as session:
        post_data = await fetch_json(session, post_url)

    return post_data 


async def fetch_all_posts():
    async with ClientSession() as session:
        post_data = await fetch_json(session, POSTS_DATA_URL)
    return post_data


async def async_main():
    logger.info("Start async main")

    user = await fetch_user(2)
    logger.info("Fetched single user: {}", user['name'])

    post = await fetch_user(2)
    logger.info("Fetched single post: {}", post['name'])

    users = await fetch_all_users()
    logger.info("Fetched all users: {}", len(users))
    
    posts = await fetch_all_posts()
    logger.info("Fetched all posts: {}", len(posts))


if __name__ == "__main__":
    asyncio.run(async_main())
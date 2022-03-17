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


async def fetch_user(user_id):
    user_url = f"{USERS_DATA_URL}/{user_id}"
    async with ClientSession() as session:
        user_data = await fetch_json(session, user_url)

    return user_data 


async def fetch_post(post_id):
    post_url = f"{POSTS_DATA_URL}/{post_id}"
    async with ClientSession() as session:
        post_data = await fetch_json(session, post_url)

    return post_data 


async def async_main():
    logger.info("Start async main")

    user = await fetch_user(USERS_DATA_URL, 2)
    logger.info("user: {}", user)

    post = await fetch_user(POSTS_DATA_URL, 2)
    logger.info("user: {}", post)
    

if __name__ == "__main__":
    asyncio.run(async_main())
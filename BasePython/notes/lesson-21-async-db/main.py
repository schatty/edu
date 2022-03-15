import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, noload, selectinload, joinedload
from sqlalchemy.engine.result import Result

from blog_project import config
from blog_project.models.database import Base
from blog_project.models import User, Tag, Post, Author


engine = create_async_engine(
    config.SQLA_ASYNC_CONN_URI,
    echo=config.SQLA_ECHO,
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def create_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str):
    user = User(username=username)
    print("Create user", user)
    session.add(user)
    await session.commit()

    await session.refresh(user)
    print("Refreshed user:", user)


async def create_author_for_user(session: AsyncSession, username: str, author_name: str):
    # Need to apply select if we want some filter-logic
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user = result.scalar_one()
    print("user", user)

    author = Author(
        name=author_name,
        user=user
    )
    print("Create author", author, "for user", user)
    session.add(user)
    await session.commit()


async def get_user_by_id(session: AsyncSession, user_id: int):
    # We can use single line .get if the case of the simple requiests
    user = await session.get(User, user_id)
    print("found user", user, " by id", user_id)
    return user


async def create_post_for_user(
    session: AsyncSession,
    username: str,
    *posts_titles: str
):
    stmt = select(Author).join(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    author: Author = result.scalar_one()

    for title in posts_titles:
        post = Post(
            title=title,
            author=author
        )
        session.add(post)

    await session.commit()


async def create_tags(session: AsyncSession, *tag_names: str):
    tags = [
        Tag(name=tag)
        for tag in tag_names
    ]
    print(tags)

    session.add_all(tags)
    await session.commit()


async def create_posts_tags_association(session: AsyncSession):
    stmt_tags = select(Tag)
    result: Result = await session.execute(stmt_tags)
    tags: list[Tag] = list(result.scalars())
    print("fetched tags:", tags)

    stmt_posts = select(Post).options(noload(Post.tags))
    result: Result = await session.execute(stmt_posts)
    posts: list[Post] = list(result.scalars())
    print("fetched posts:", tags)

    for post in posts:
        for tag in tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)
                print("Added tag", tag, "to post", post)

    await session.commit()


async def fetch_posts_with_tags_and_authors(session: AsyncSession):
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
    )
    result: Result = await session.execute(stmt)
    posts: list[Post] = list(result.scalars())

    for post in posts:
        print("Post", post)
        print(" -- Tags", post.tags)
        print(" -- User", post.author.user)
        print(" -- Author", post.author)


async def main_async():
    # Can used for test, better use alembic for scheme creation
    # await create_schemas()

    async with async_session() as session:
        # await create_user(session, "john")
        # await create_user(session, "sam")
        
        # await create_author_for_user(session, "john", "John Smith")
        # await create_author_for_user(session, "sam", "Sam Smith")

        # await get_user_by_id(session, 1)

        # await create_post_for_user(session, "john", "Lesson Django", "Lesson Flask")
        # await create_post_for_user(session, "sam", "News", "Lesson PyCharm")

        # await create_tags(session, "news", "python", "django", "flask")

        # await create_posts_tags_association(session)

        await fetch_posts_with_tags_and_authors(session)
        

def main():
     asyncio.run(main_async())


if __name__ == "__main__":
    main()

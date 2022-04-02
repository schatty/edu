from functools import wraps
from sqlalchemy.orm import joinedload, selectinload

from models.database import Base, Session
from models import User, Author, Post, author


def with_session(func):

    @wraps(func)
    def wrapper():
        session = Session()
        func(session)
        session.close()

    return wrapper


def create_user():
    session = Session()
    sam = User(username="sam", is_staff=False)
    print("created", sam)

    session.add(sam)
    session.commit() 
    print("saved", sam)

    session.close()


def create_author_sam():
    session = Session()
    sam: User = session.query(User).filter_by(username="sam").one()
    author_sam = Author(
        name="Samuel White",
        # user_id will be automatically inserted by SQLAlchemy
        user=sam
    )
    print("create author for sam:", author_sam, sam)

    session.add(author_sam)
    session.commit()

    print("user for author:", author_sam.user)

    session.close()

@with_session
def create_posts_for_timm(session):
    author_timm: Author = (
        session
        .query(Author)
        .join(User)
        .filter(User.username == "timm")
        .one()
    )
    print(author_timm)

    post_django = Post(
        title="Lesson Django",
        author=author_timm
    )
    print("post django:", post_django)

    post_flask = Post(
        title="Lesson Flask",
        author=author_timm
    )
    print("post flask:", post_flask)

    session.commit()


@with_session
def fetch_posts_with_all_data(session):
    # posts = session.query(Post).all()

    posts: list[Post] = (
        session
        .query(Post)
        .options(
            joinedload(Post.author).joinedload(Author.user)
        )
    )

    for post in posts:
        print("post:", post)
        print("\tauthor", post.author)
        print("\tuser", post.author.user)


@with_session
def fetch_authors_with_lesson_posts_with_all_data(session): 
    q_authors = (
        session
        .query(Author)
        .join(Post, Post.author_id == Author.id)
        .options(
            joinedload(Author.user),
            selectinload(Author.posts),
        )
        .filter(Post.title.ilike("lesson%"))
    )

    authors: list[Author] = q_authors.all()

    for author in authors:
        print("author:", author)

def main():
    #print("User mro():", User.mro())
    # Base.metadata.create_all()

    # create_user()
    # create_author_sam()
    # create_posts_for_timm()
    # fetch_posts_with_all_data()
    fetch_authors_with_lesson_posts_with_all_data()


if __name__ == "__main__":
    main()
from functools import wraps
from sqlalchemy.orm import joinedload, selectinload

from blog_project.models.database import Base, Session
from blog_project.models import User, Author, Post, Tag


def with_session(func):

    @wraps(func)
    def wrapper(*args):
        session = Session()
        func(session, *args)
        session.close()

    return wrapper


@with_session
def create_user(session, username):
    user = User(username=username, is_staff=False)
    print("created", user)

    session.add(user)
    session.commit() 
    print("saved", user)


@with_session
def create_author_for_user(session, username: str, authorname: str):
    user: User = session.query(User).filter_by(username=username).one()
    author_user = Author(
        name=authorname,
        # user_id will be automatically inserted by SQLAlchemy
        user=user
    )
    print("create author for sam:", author_user, user)

    session.add(author_user)
    session.commit()


@with_session
def create_posts_for_user(session, username: str, *posts_titles: str):
    author: Author = (
        session
        .query(Author)
        .join(User)
        .filter(User.username == username)
        .one()
    )
    print(author)

    for title in posts_titles:
        post = Post(
            title=title,
            author=author
        )
        print("post:", post)
        session.add(post)
        
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


@with_session
def create_posts_with_tags_association(session):
    q_tags = session.query(Tag)
    tag_python = q_tags.filter_by(name="python").one()
    other_tags = q_tags.filter(Tag.id != tag_python.id).all()

    # tag_news = q_tags.filter_by(name="news").one()
    # tag_django = q_tags.filter_by(name="django").one()
    # tag_flask = q_tags.filter_by(name="flask").one()

    posts: list[Post] = session.query(Post).all()

    for post in posts:
        post.tags.append(tag_python)
        for tag in other_tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)
        
    session.commit()


@with_session
def fetch_posts_with_tags(session):
    posts: list[Post] = session.query(Post).options(joinedload(Post.tags))
    for post in posts:
        print("post:", post)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data(session):
    posts: list[Post] = (
        session
        .query(Post)
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user)
        )
    )

    for post in posts:
        print("post:", post)
        print("--authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data_by_tags(session, *tags: str):
    posts: list[Post] = (
        session
        .query(Post)
        .join(Tag, Post.tags)
        .filter(
            Tag.name.in_(tags)
        )
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user)
        )
    )

    for post in posts:
        print("post:", post)
        print("--authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


def prepare_db_data():
    # Base.metadata.create_all()

    create_user("sam")
    create_user("john")

    create_author_for_user("sam", "Samuel")
    create_author_for_user("john", "Johnatan")
    
    create_posts_for_user("john", "Lesson Django", "Lesson Flask")
    create_posts_for_user("sam", "Python News", "Lesson PyCharm")

    fetch_posts_with_all_data()
    fetch_authors_with_lesson_posts_with_all_data()


@with_session
def create_tags(session, *names: str):
    tags = [
        Tag(name=name)
        for name in names
    ]
    print(tags)
    session.add_all(tags)
    session.commit()


def main():
    # create_tags("news", "python", "django", "flask")
    # create_posts_with_tags_association()
    # fetch_posts_with_tags()
    # fetch_posts_with_all_data()
    fetch_posts_with_all_data_by_tags("news", "flask")


if __name__ == "__main__":
    main()
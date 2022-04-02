from datetime import datetime
from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    String,
    Integer,
    Boolean,
    DateTime
)
from sqlalchemy.orm import (
    declarative_base,
    scoped_session,
    sessionmaker
)


DB_URL = "sqlite:///example-04.db"
engine = create_engine(DB_URL, echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id} " \
               f"username={self.username!r} " \
               f"is_staff={self.is_staff} "\
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    session = Session()

    user = User(username=username)
    print("created", user)
    session.add(user)
    session.commit()
    print("saved", user)

    session.close()
    return user

def get_all_users() -> list[User]:
    session = Session()

    users = session.query(User).all()

    session.close()
    return users


def get_user(username: str) -> User:
    session = Session()
    user = session.query(User).filter_by(username=username).one()
    session.close()
    return user


def find_user_by_str(name_part: str) -> list[User]:
    session = Session()

    query = session.query(User).filter(
        User.username.like(f"{name_part}%")
    )
    users = query.all()

    session.close()
    return users


def user_updating(username: str):
    session = Session()

    user = session.query(User).filter_by(username=username).one()
    user.is_staff = True
    session.commit()

    session.close()
    return user


def user_creation():
    create_user("sam")


def users_fetching():
    #users = get_all_users()
    #print(users)
    #return users
    users = find_user_by_str("sa")
    print(users)
    return users


def main():
    #Base.metadata.create_all()
    #create_user("john")
    #create_user("sam")
    #users_fetching()
    user_updating("john")


if __name__ == "__main__":
    main()
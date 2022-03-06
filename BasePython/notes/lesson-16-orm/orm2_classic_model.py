from click import echo
from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    String,
    Integer,
    Boolean,
    null,
)
from sqlalchemy.orm import mapper


DB_URL = "sqlite:///example-01.sqlite"
engine = create_engine(DB_URL, echo=True)
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False, nullable=False),
)


class User:
    def __init__(self, id: int, username: str, is_staff: bool):
        self.id = id
        self.username = username
        self.is_staff = is_staff


mapper(User, users_table)


if __name__ == "__main__":
    metadata.create_all(bind=engine)



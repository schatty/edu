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
from sqlalchemy.orm import declarative_base


DB_URL = "sqlite:///example-03.db"
engine = create_engine(DB_URL, echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


def create_table():
    Base.metadata.create_all()


if __name__ == "__main__":
    create_table()
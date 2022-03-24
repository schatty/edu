from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from .database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    username = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)

    def __str__(self):
        return (
            f"User id {self.id} (name={self.name}, "
            f"username={self.username}, email={self.email})"
        )
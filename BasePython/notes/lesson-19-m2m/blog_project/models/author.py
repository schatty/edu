from ast import For
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base
from .mixins import TimestampMixin


class Author(TimestampMixin, Base):
    name = Column(
        String(32),
        unique=False,
        nullable=False,
        default="", server_default=""
    )

    # Example of 1:1 relation
    user_id =  Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=True
    )

    user = relationship("User", back_populates="author")
    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}("\
               f"id={self.id} " \
               f"name={self.name!r} " \
               f"user_id={self.user_id} " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)
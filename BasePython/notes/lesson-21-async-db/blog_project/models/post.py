from sqlalchemy import Column, String, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .database import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association_table


class Post(TimestampMixin, Base):
    title = Column(
        String(200), 
        nullable=False,
        default="",
        server_default=""
    )

    body = Column(
        Text,
        nullable=False,
        default="",
        server_default=""
    )
    status = Column(
        String(10),
        nullable=False,
        default="draft",
        server_default="default"
    )

    author_id = Column(
        Integer,
        ForeignKey("blog_authors.id"),
        nullable=False
    )
    author = relationship("Author", back_populates="posts")

    tags = relationship("Tag", secondary=posts_tags_association_table, back_populates="posts")
    
    def __str__(self):
        return f"{self.__class__.__name__}("\
               f"id={self.id} " \
               f"name={self.title!r} " \
               f"author_id={self.author_id} " \
               f"created_at={self.created_at!r})"
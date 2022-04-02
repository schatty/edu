from datetime import date, datetime
from http import server
from sqlite3 import Date

from sqlalchemy import (
    Column,
    DateTime,
    func
)


class TimestampMixin:
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )
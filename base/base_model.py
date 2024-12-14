# from sqlalchemy.orm import DeclarativeBase
from datetime import date

from sqlalchemy import Column, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    __allow_unmapped__ = True
    created_at = Column(DateTime, default=date.today())
    updated_at = Column(DateTime, default=date.today(), onupdate=date.today())


# BaseModel = declarative_base(cls=ModelBase)
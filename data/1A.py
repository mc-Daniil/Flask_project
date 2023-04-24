import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class A1(SqlAlchemyBase):
    __tablename__ = '1A'


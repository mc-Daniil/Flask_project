import sqlalchemy
from .db_session import SqlAlchemyBase
import datetime
from sqlalchemy import orm


class Kilogram(SqlAlchemyBase):
    __tablename__ = "kilograms"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    value = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship("User")
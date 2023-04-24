import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class A1(SqlAlchemyBase):
    __tablename__ = 'A1'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    kilo = orm.relationship("Kilograms", back_populates="pupil")





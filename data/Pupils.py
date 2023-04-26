import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Pupils(SqlAlchemyBase):
    __tablename__ = 'Pupils'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    grade = sqlalchemy.Column(sqlalchemy.String)

    kilo = orm.relationship("Kilograms", back_populates="pupil")





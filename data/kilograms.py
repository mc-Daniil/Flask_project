import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Kilograms(SqlAlchemyBase):
    __tablename__ = 'kilograms'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    value = sqlalchemy.Column(sqlalchemy.Integer)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    pupil_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Pupils.id"))
    user = orm.relationship('User')
    pupil = orm.relationship("Pupils")
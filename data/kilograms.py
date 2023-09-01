import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Kilograms(SqlAlchemyBase):
    """
    Класс для взаимодействия с одной из трёх таблиц базы данных, которая хранит историю отправленных килограммов
    """
    __tablename__ = 'kilograms'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True) # ID записи
    value = sqlalchemy.Column(sqlalchemy.Integer) # Кол-во килограммов

    # Время отправки. На сервере -3 часа, поэтому прибавляю 3 часа
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=(datetime.datetime.now() + datetime.timedelta(hours=3)))

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id")) # ID волонтёра

    pupil_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Pupils.id")) # ID ученика
    user = orm.relationship('User') # Связь с таблицой БД, которая хранит волонтёров
    pupil = orm.relationship("Pupils") # Связь с таблицой БД, которая хранит учеников
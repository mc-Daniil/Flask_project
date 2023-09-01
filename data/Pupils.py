import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Pupils(SqlAlchemyBase):
    """
    Класс для взаимодействия с таблицей БД, которая хранит всех учеников
    """
    __tablename__ = 'Pupils'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True) # ID ученика
    name = sqlalchemy.Column(sqlalchemy.String) # Имя и фамилия ученика
    value = sqlalchemy.Column(sqlalchemy.Integer, default=0) # Кол-во сданных килограммов
    grade = sqlalchemy.Column(sqlalchemy.String) # Класс

    kilo = orm.relationship("Kilograms", back_populates="pupil") # Связь в таблицей БД, которая хранит килограммы





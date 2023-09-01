import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    """
    Класс для взаимодействия с таблицей БД, которая хранит волонтёров
    """
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True) # ID волонтёра
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True) # Имя волонтёра
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True) # Дополнительная информация
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True) # Почта, у каждого своя
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True) # Зашифрованный пароль
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean) # Админ или нет
    got = sqlalchemy.Column(sqlalchemy.Integer, default=0) # Сколько собрал килограммов
    got_pupils = sqlalchemy.Column(sqlalchemy.Integer, default=0) # Сколько человек обслужил

    kilograms = orm.relationship("Kilograms", back_populates='user') # Связь с таблицей с килограммами

    def set_password(self, password):
        """
        Функция для шифрования пароля
        :param password:
        :return:
        """
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """
        Функция для сравнения зашифрованного пароля в БД и введённого пароля
        :param password:
        :return:
        """
        return check_password_hash(self.hashed_password, password)

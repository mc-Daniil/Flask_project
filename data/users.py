import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)

    kilogram = orm.relationship("Kilogram", back_populates="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

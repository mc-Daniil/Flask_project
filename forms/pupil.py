from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField, IntegerField


class PostForm(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[("Вася Пупкин"), ("Иван Иванов")])
    value = IntegerField("Килограммы")
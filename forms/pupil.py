from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField, IntegerField, SubmitField


class Post1A(FlaskForm):

    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open("db/1A.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")
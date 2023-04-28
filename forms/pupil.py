from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField, IntegerField, SubmitField


class Post1A(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/1А.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post2A(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/2А.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post2B(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/2Б.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post3A(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/3А.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post3B(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/3Б.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post3C(FlaskForm):
    name = SelectField("Фамилия и имя", choices=[(i.strip()) for i in open(f"db/Grades/3В.txt", encoding="utf-8").readlines()], validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post4A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/4А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post4B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/4Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post4C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/4В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post5A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/5А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post5B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/5Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post5C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/5В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post6A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/6А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post6B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/6Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post6C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/6В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post7A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/7А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post7B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/7Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post7C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/7В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post8A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/8А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post8B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/8Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post8C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/8В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post9A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/9А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post9B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/9Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post9C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/9В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post10A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/10А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post10B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/10Б.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post10C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/10В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post11A(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/11А.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post11B(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/11Б.txt", encoding="utf-8")],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class Post11C(FlaskForm):
    name = SelectField("Фамилия и имя",
                       choices=[(i.strip()) for i in open(f"db/Grades/11В.txt", encoding="utf-8").readlines()],
                       validators=[DataRequired()])
    value = IntegerField("Килограммы", validators=[DataRequired()])
    submit = SubmitField("Отправить")
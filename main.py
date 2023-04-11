from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = "Машина дикая"


# @app.route("/")
# @app.route("/index")
# def index():
#     user = "Daniil"
#     return render_template("index.html", title="Стартовая страница", username=user)


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/success")
def success():
    return render_template("success.html", title="Успешная авторизация")


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
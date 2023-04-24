from flask import Flask, render_template, redirect
from data import db_session
from data.kilograms import Kilograms
from forms.user import RegisterForm, LoginForm
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.A1 import A1
from forms.pupil import Post1A

app = Flask(__name__)
app.config['SECRET_KEY'] = "Машина дикая"
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/stats")
def stats():
    return render_template("base.html", title="Статитстика")


@app.route("/post1a", methods=["GET", "POST"])
@login_required
def post1a():
    form = Post1A()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        pupil = db_sess.query(A1).filter(A1.name == form.name.data).first()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        kilo = Kilograms()

        pupil.value += form.value.data

        user.got_pupils += 1
        user.got += form.value.data

        kilo.value = form.value.data
        kilo.user_id = current_user.id
        kilo.pupil_id = pupil.id

        db_sess.add(kilo)
        db_sess.commit()

    return render_template("post_form.html", title="1А", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
@app.route("/index")
def main_page():
    db_sess = db_session.create_session()
    kilograms = db_sess.query(Kilograms)

    return render_template("index.html", kilograms=kilograms)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            is_admin=form.is_admin.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/history")
def history():



def main():
    db_session.global_init("db/base.db")
    app.run()


if __name__ == '__main__':
    main()
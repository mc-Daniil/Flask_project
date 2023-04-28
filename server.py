from flask import Flask, render_template, redirect, request, abort
from data import db_session
from data.kilograms import Kilograms
from forms.user import RegisterForm, LoginForm
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.Pupils import Pupils
import forms.pupil

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
    return render_template("stats.html", title="Статитстика")


@app.route("/post1a", methods=["GET", "POST"])
@login_required
def post1a():
    form = forms.pupil.Post1A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="1А", form=form, grade="1А")


@app.route("/post2a", methods=["GET", "POST"])
@login_required
def post2a():
    form = forms.pupil.Post2A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="2А", form=form, grade="2А")


@app.route("/post2b", methods=["GET", "POST"])
@login_required
def post2b():
    form = forms.pupil.Post2B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="2Б", form=form, grade="2Б")


@app.route("/post3a", methods=["GET", "POST"])
@login_required
def post3a():
    form = forms.pupil.Post3A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="3А", form=form, grade="3А")


@app.route("/post3b", methods=["GET", "POST"])
@login_required
def post3b():
    form = forms.pupil.Post3B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="3Б", form=form, grade="3Б")


@app.route("/post3c", methods=["GET", "POST"])
@login_required
def post3c():
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="3В", form=form, grade="3В")


@app.route("/post4a", methods=["GET", "POST"])
@login_required
def post4a():
    form = forms.pupil.Post4A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="4А", form=form, grade="4А")


@app.route("/post4b", methods=["GET", "POST"])
@login_required
def post4b():
    form = forms.pupil.Post4B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="4Б", form=form, grade="4Б")


@app.route("/post4c", methods=["GET", "POST"])
@login_required
def post4c():
    form = forms.pupil.Post4C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="4В", form=form, grade="4В")


@app.route("/post5a", methods=["GET", "POST"])
@login_required
def post5a():
    form = forms.pupil.Post5A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="5А", form=form, grade="5А")


@app.route("/post5b", methods=["GET", "POST"])
@login_required
def post5b():
    form = forms.pupil.Post5B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="5Б", form=form, grade="5Б")


@app.route("/post5c", methods=["GET", "POST"])
@login_required
def post5c():
    form = forms.pupil.Post5C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="5В", form=form, grade="5В")


@app.route("/post6a", methods=["GET", "POST"])
@login_required
def post6a():
    form = forms.pupil.Post3A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="6А", form=form, grade="6А")


@app.route("/post6b", methods=["GET", "POST"])
@login_required
def post6b():
    form = forms.pupil.Post6B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="6Б", form=form, grade="6Б")


@app.route("/post6c", methods=["GET", "POST"])
@login_required
def post6c():
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="6В", form=form, grade="6В")


@app.route("/post7a", methods=["GET", "POST"])
@login_required
def post7a():
    form = forms.pupil.Post7A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="7А", form=form, grade="7А")


@app.route("/post7b", methods=["GET", "POST"])
@login_required
def post7b():
    form = forms.pupil.Post7B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="7Б", form=form, grade="7Б")


@app.route("/post7c", methods=["GET", "POST"])
@login_required
def post7c():
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="7В", form=form, grade="7В")


@app.route("/post8a", methods=["GET", "POST"])
@login_required
def post8a():
    form = forms.pupil.Post8A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="8А", form=form, grade="8А")


@app.route("/post8b", methods=["GET", "POST"])
@login_required
def post8b():
    form = forms.pupil.Post8B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="8Б", form=form, grade="8Б")


@app.route("/post8c", methods=["GET", "POST"])
@login_required
def post8c():
    form = forms.pupil.Post8C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="8В", form=form, grade="8В")


@app.route("/post9a", methods=["GET", "POST"])
@login_required
def post9a():
    form = forms.pupil.Post9A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="9А", form=form, grade="9А")


@app.route("/post9b", methods=["GET", "POST"])
@login_required
def post9b():
    form = forms.pupil.Post9B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="9Б", form=form, grade="9Б")


@app.route("/post9c", methods=["GET", "POST"])
@login_required
def post9c():
    form = forms.pupil.Post9C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="9В", form=form, grade="9В")


@app.route("/post10a", methods=["GET", "POST"])
@login_required
def post10a():
    form = forms.pupil.Post10A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="10А", form=form, grade="10А")


@app.route("/post10b", methods=["GET", "POST"])
@login_required
def post10b():
    form = forms.pupil.Post10B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="10Б", form=form, grade="10Б")


@app.route("/post10c", methods=["GET", "POST"])
@login_required
def post10c():
    form = forms.pupil.Post10C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="10В", form=form, grade="10В")


@app.route("/post11a", methods=["GET", "POST"])
@login_required
def post11a():
    form = forms.pupil.Post11A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="11А", form=form, grade="11А")


@app.route("/post11b", methods=["GET", "POST"])
@login_required
def post11b():
    form = forms.pupil.Post11B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="11Б", form=form, grade="11Б")


@app.route("/post11c", methods=["GET", "POST"])
@login_required
def post11c():
    form = forms.pupil.Post11C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data).first()
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

    return render_template("post_form.html", title="11В", form=form, grade="11В")


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
    db_sess = db_session.create_session()
    kilo = db_sess.query(Kilograms)
    return render_template("history.html", kilo=kilo)


@app.route("/users")
def users():
    db_sess = db_session.create_session()
    user = db_sess.query(User)
    return render_template("users.html", user=user)


def main():
    db_session.global_init("db/base.db")

    # db_sess = db_session.create_session()
    # for j in ["1А", "2А", "2Б", "3А", "3Б", "3В", "4А", "4Б", "4В", "5А", "5Б", "5В", "6А", "6Б", "6В", ]
    # for i in open("E:/Code/Python/Flask_project/db/Grades/1А.txt", encoding="utf-8").readlines():
    #     pupil = Pupils()
    #     pupil.name = i.strip()
    #     pupil.grade = "1А"
    #     db_sess.add(pupil)
    #
    #
    # db_sess.commit()


    app.run()


if __name__ == '__main__':
    main()
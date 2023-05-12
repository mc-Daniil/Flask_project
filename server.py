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
    db_sess = db_session.create_session()

    _1a = db_sess.query(Pupils).filter(Pupils.grade == "1А").all()
    sum_1a = 0
    for i in _1a:
        sum_1a += i.value

    _2a = db_sess.query(Pupils).filter(Pupils.grade == "2А").all()
    sum_2a = 0
    for i in _2a:
        sum_2a += i.value

    return render_template("stats.html", title="Статитстика", sum_1a=sum_1a, sum_2a=sum_2a)


@app.route("/post1a", methods=["GET", "POST"])
@login_required
def post1a():
    grade = "1А"
    form = forms.pupil.Post1A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post2a", methods=["GET", "POST"])
@login_required
def post2a():
    grade = "2А"
    form = forms.pupil.Post2A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post2b", methods=["GET", "POST"])
@login_required
def post2b():
    grade = "2Б"
    form = forms.pupil.Post2B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3a", methods=["GET", "POST"])
@login_required
def post3a():
    grade = "3А"
    form = forms.pupil.Post3A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3b", methods=["GET", "POST"])
@login_required
def post3b():
    grade = "3Б"
    form = forms.pupil.Post3B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3c", methods=["GET", "POST"])
@login_required
def post3c():
    grade = "3В"
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4a", methods=["GET", "POST"])
@login_required
def post4a():
    grade = "4А"
    form = forms.pupil.Post4A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4b", methods=["GET", "POST"])
@login_required
def post4b():
    grade = "4Б"
    form = forms.pupil.Post4B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4c", methods=["GET", "POST"])
@login_required
def post4c():
    grade = "4В"
    form = forms.pupil.Post4C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5a", methods=["GET", "POST"])
@login_required
def post5a():
    grade = "5А"
    form = forms.pupil.Post5A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5b", methods=["GET", "POST"])
@login_required
def post5b():
    grade = "5Б"
    form = forms.pupil.Post5B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5c", methods=["GET", "POST"])
@login_required
def post5c():
    grade = "5В"
    form = forms.pupil.Post5C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6a", methods=["GET", "POST"])
@login_required
def post6a():
    grade = "6А"
    form = forms.pupil.Post3A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6b", methods=["GET", "POST"])
@login_required
def post6b():
    grade = "6Б"
    form = forms.pupil.Post6B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6c", methods=["GET", "POST"])
@login_required
def post6c():
    grade = "6В"
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7a", methods=["GET", "POST"])
@login_required
def post7a():
    grade = "7А"
    form = forms.pupil.Post7A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7b", methods=["GET", "POST"])
@login_required
def post7b():
    grade = "7Б"
    form = forms.pupil.Post7B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7c", methods=["GET", "POST"])
@login_required
def post7c():
    grade = "7В"
    form = forms.pupil.Post3C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8a", methods=["GET", "POST"])
@login_required
def post8a():
    grade = "8А"
    form = forms.pupil.Post8A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8b", methods=["GET", "POST"])
@login_required
def post8b():
    grade = "8Б"
    form = forms.pupil.Post8B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8c", methods=["GET", "POST"])
@login_required
def post8c():
    grade = "8В"
    form = forms.pupil.Post8C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9a", methods=["GET", "POST"])
@login_required
def post9a():
    grade = "9А"
    form = forms.pupil.Post9A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9b", methods=["GET", "POST"])
@login_required
def post9b():
    grade = "9Б"
    form = forms.pupil.Post9B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9c", methods=["GET", "POST"])
@login_required
def post9c():
    grade = "9В"
    form = forms.pupil.Post9C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10a", methods=["GET", "POST"])
@login_required
def post10a():
    grade = "10А"
    form = forms.pupil.Post10A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10b", methods=["GET", "POST"])
@login_required
def post10b():
    grade = "10Б"
    form = forms.pupil.Post10B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10c", methods=["GET", "POST"])
@login_required
def post10c():
    grade = "10В"
    form = forms.pupil.Post10C()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11a", methods=["GET", "POST"])
@login_required
def post11a():
    grade = "11А"
    form = forms.pupil.Post11A()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11b", methods=["GET", "POST"])
@login_required
def post11b():
    grade = "11Б"
    form = forms.pupil.Post11B()
    if form.validate_on_submit() and current_user.is_authenticated:
        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11c", methods=["GET", "POST"])
@login_required
def post11c():
    form = forms.pupil.Post11C()
    grade = "11В"
    if form.validate_on_submit() and current_user.is_authenticated:

        db_sess = db_session.create_session()

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first()
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
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/stats1a")
@login_required
def stats1a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "1А").all()
    return render_template("stats_grade.html", db=pupils, grade="1А", title="1А статистика")


@app.route("/stats2a")
@login_required
def stats2a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "2А").all()
    return render_template("stats_grade.html", db=pupils, grade="2А", title="2А статистика")


@app.route("/stats2b")
@login_required
def stats2b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "2Б").all()
    return render_template("stats_grade.html", db=pupils, grade="2Б", title="2Б статистика")


@app.route("/stats3a")
@login_required
def stats3a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3А").all()
    return render_template("stats_grade.html", db=pupils, grade="3А", title="3А статистика")


@app.route("/stats3b")
@login_required
def stats3b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3Б").all()
    return render_template("stats_grade.html", db=pupils, grade="3Б", title="3Б статистика")


@app.route("/stats3c")
@login_required
def stats3c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3В").all()
    return render_template("stats_grade.html", db=pupils, grade="3В", title="3В статистика")


@app.route("/stats4a")
@login_required
def stats4a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4А").all()
    return render_template("stats_grade.html", db=pupils, grade="4А", title="4А статистика")


@app.route("/stats4b")
@login_required
def stats4b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4Б").all()
    return render_template("stats_grade.html", db=pupils, grade="4Б", title="4Б статистика")


@app.route("/stats4c")
@login_required
def stats4c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4В").all()
    return render_template("stats_grade.html", db=pupils, grade="4В", title="4В статистика")


@app.route("/stats5a")
@login_required
def stats5a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5А").all()
    return render_template("stats_grade.html", db=pupils, grade="5А", title="5А статистика")


@app.route("/stats5b")
@login_required
def stats5b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5Б").all()
    return render_template("stats_grade.html", db=pupils, grade="5Б", title="5Б статистика")


@app.route("/stats5c")
@login_required
def stats5c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5В").all()
    return render_template("stats_grade.html", db=pupils, grade="5В", title="5В статистика")


@app.route("/stats6a")
@login_required
def stats6a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6А").all()
    return render_template("stats_grade.html", db=pupils, grade="6А", title="6А статистика")


@app.route("/stats6b")
@login_required
def stats6b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6Б").all()
    return render_template("stats_grade.html", db=pupils, grade="6Б", title="6Б статистика")


@app.route("/stats6c")
@login_required
def stats6c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6В").all()
    return render_template("stats_grade.html", db=pupils, grade="6В", title="6В статистика")


@app.route("/stats7a")
@login_required
def stats7a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7А").all()
    return render_template("stats_grade.html", db=pupils, grade="7А", title="7А статистика")


@app.route("/stats7b")
@login_required
def stats7b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7Б").all()
    return render_template("stats_grade.html", db=pupils, grade="7Б", title="7Б статистика")


@app.route("/stats7c")
@login_required
def stats7c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7В").all()
    return render_template("stats_grade.html", db=pupils, grade="7В", title="7В статистика")


@app.route("/stats8a")
@login_required
def stats8a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8А").all()
    return render_template("stats_grade.html", db=pupils, grade="8А", title="8А статистика")


@app.route("/stats8b")
@login_required
def stats8b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8Б").all()
    return render_template("stats_grade.html", db=pupils, grade="8Б", title="8Б статистика")


@app.route("/stats8c")
@login_required
def stats8c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8В").all()
    return render_template("stats_grade.html", db=pupils, grade="8В", title="8В статистика")


@app.route("/stats9a")
@login_required
def stats9a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9А").all()
    return render_template("stats_grade.html", db=pupils, grade="9А", title="9А статистика")


@app.route("/stats9b")
@login_required
def stats9b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9Б").all()
    return render_template("stats_grade.html", db=pupils, grade="9Б", title="9Б статистика")


@app.route("/stats9c")
@login_required
def stats9c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9В").all()
    return render_template("stats_grade.html", db=pupils, grade="9В", title="9В статистика")


@app.route("/stats10a")
@login_required
def stats10a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10А").all()
    return render_template("stats_grade.html", db=pupils, grade="10А", title="10А статистика")


@app.route("/stats10b")
@login_required
def stats10b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10Б").all()
    return render_template("stats_grade.html", db=pupils, grade="10Б", title="10Б статистика")


@app.route("/stats10c")
@login_required
def stats10c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10В").all()
    return render_template("stats_grade.html", db=pupils, grade="10В", title="10В статистика")


@app.route("/stats11a")
@login_required
def stats11a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11А").all()
    return render_template("stats_grade.html", db=pupils, grade="11А", title="11А статистика")


@app.route("/stats11b")
@login_required
def stats11b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11Б").all()
    return render_template("stats_grade.html", db=pupils, grade="11Б", title="11Б статистика")


@app.route("/stats11c")
@login_required
def stats11c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11В").all()
    return render_template("stats_grade.html", db=pupils, grade="11В", title="11В статистика")


@app.route("/history")
def history():
    db_sess = db_session.create_session()
    kilo = db_sess.query(Kilograms)
    return render_template("history.html", kilo=kilo)


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


@app.route("/kilo_delete/<int:id>", methods=["GET", "POST"])
@login_required
def kilo_delete(id):
    db_sess = db_session.create_session()
    kilo = db_sess.query(Kilograms).filter(Kilograms.id == id).first()
    if kilo:
        user_id = kilo.user_id
        pupil_id = kilo.id
        value = kilo.value

        user = db_sess.query(User).filter(User.id == user_id).first()
        pupil = db_sess.query(Pupils).filter(Pupils.id == pupil_id).first()

        user.got_pupils -= 1
        user.got -= value

        pupil.value -= value

        db_sess.delete(kilo)
        db_sess.commit()

    else:
        abort(404)
    return redirect("/history")



@app.route("/users")
def users():
    db_sess = db_session.create_session()
    user = db_sess.query(User)
    return render_template("users.html", user=user)


def main():
    db_session.global_init("db/base.db")

    # db_sess = db_session.create_session()
    # for j in ["1А", "2А", "2Б", "3А", "3Б", "3В", "4А", "4Б", "4В", "5А", "5Б", "5В", "6А", "6Б", "6В",
    #           "7А", "7Б", "7В", "8А", "8Б", "8В", "9А", "9Б", "9В", "10А", "10Б", "10В", "11А", "11Б", "11В"]:
    #     for i in open(f"E:/Code/Python/Flask_project/db/Grades/{j}.txt", encoding="utf-8").readlines():
    #         pupil = Pupils()
    #         pupil.name = i.strip()
    #         pupil.grade = j
    #         db_sess.add(pupil)
    #
    #     db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
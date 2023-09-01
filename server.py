from flask import Flask, render_template, redirect, abort, send_from_directory
from data import db_session
from data.kilograms import Kilograms
from forms.user import RegisterForm, LoginForm
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.Pupils import Pupils
import forms.pupil
import xlsxwriter
import tempfile

app = Flask(__name__) # Само приложение
app.config['SECRET_KEY'] = "Машина дикая"
login_manager = LoginManager() # Инструмент для входа и выхода пользователей
login_manager.init_app(app) # Применение инструмента для нашего приложения


@login_manager.user_loader # Декоратор для авторизации пользователей
def load_user(user_id):
    db_sess = db_session.create_session()
    user_id = db_sess.query(User).get(user_id)
    db_sess.close()
    return user_id


@app.route('/login', methods=['GET', 'POST']) # Адрес страницы для входа. Использует методы отправки и принятия данных
def login():
    """
    Функция со страницей для авторизации существующих пользователей
    """
    form = LoginForm() # Форма авторизации
    if form.validate_on_submit(): # Если нажата кнопка "Войти"
        db_sess = db_session.create_session() # Подключение к БД
        user = db_sess.query(User).filter(User.email == form.email.data).first() # Достать пользователя по почте
        if user and user.check_password(form.password.data): # Если пользователь существует и пароль верный
            login_user(user, remember=form.remember_me.data) # Войти
            db_sess.close() # Завершить сессию
            return redirect("/") # Направить на главную страницу
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form) # Иначе открыть эту же страницу с сообщением об ошибке
    return render_template('login.html', title='Авторизация', form=form) # Иначе просто открыть страницу с формой авторизации


@app.route("/stats") # Адрес страницы со статистикой по классам
def stats():
    """
    Функция считает, сколько кг собрал каждый класс и открывает страницу с этой информацией
    """
    # Переменные для подсчёта кг для каждого класса
    global sum_1a, sum_2a, sum_2b, sum_3a, sum_3b, sum_3c, sum_4a, sum_4b, sum_4c, sum_5a, sum_5b, sum_5c, \
        sum_6a, sum_6b, sum_6c, sum_7a, sum_7b, sum_7c, sum_8a, sum_8b, sum_8c, sum_9a, sum_9b, sum_9c, \
        sum_10a, sum_10b, sum_10c, sum_11a, sum_11b, sum_11c

    db_sess = db_session.create_session() # Создание сессии

    _1a = db_sess.query(Pupils).filter(Pupils.grade == "1А").all() # Получаем всех учеников из 1А
    sum_1a = 0
    for i in _1a: # Идём по всем ученикам 1А
        sum_1a += i.value # Прибавляем кг конкретного ученика

    # Аналогично с другими классами

    _2a = db_sess.query(Pupils).filter(Pupils.grade == "2А").all()
    sum_2a = 0
    for i in _2a:
        sum_2a += i.value

    _2b = db_sess.query(Pupils).filter(Pupils.grade == "2Б").all()
    sum_2b = 0
    for i in _2b:
        sum_2b += i.value

    _3a = db_sess.query(Pupils).filter(Pupils.grade == "3А").all()
    sum_3a = 0
    for i in _3a:
        sum_3a += i.value

    _3b = db_sess.query(Pupils).filter(Pupils.grade == "3Б").all()
    sum_3b = 0
    for i in _3b:
        sum_3b += i.value

    _3c = db_sess.query(Pupils).filter(Pupils.grade == "3В").all()
    sum_3c = 0
    for i in _3c:
        sum_3c += i.value

    _4a = db_sess.query(Pupils).filter(Pupils.grade == "4А").all()
    sum_4a = 0
    for i in _4a:
        sum_4a += i.value

    _4b = db_sess.query(Pupils).filter(Pupils.grade == "4Б").all()
    sum_4b = 0
    for i in _4b:
        sum_4b += i.value

    _4c = db_sess.query(Pupils).filter(Pupils.grade == "4В").all()
    sum_4c = 0
    for i in _4c:
        sum_4c += i.value

    _5a = db_sess.query(Pupils).filter(Pupils.grade == "5А").all()
    sum_5a = 0
    for i in _5a:
        sum_5a += i.value

    _5b = db_sess.query(Pupils).filter(Pupils.grade == "5Б").all()
    sum_5b = 0
    for i in _5b:
        sum_5b += i.value

    _5c = db_sess.query(Pupils).filter(Pupils.grade == "5В").all()
    sum_5c = 0
    for i in _5c:
        sum_5c += i.value

    _6a = db_sess.query(Pupils).filter(Pupils.grade == "6А").all()
    sum_6a = 0
    for i in _6a:
        sum_6a += i.value

    _6b = db_sess.query(Pupils).filter(Pupils.grade == "6Б").all()
    sum_6b = 0
    for i in _6b:
        sum_6b += i.value

    _6c = db_sess.query(Pupils).filter(Pupils.grade == "6В").all()
    sum_6c = 0
    for i in _6c:
        sum_6c += i.value

    _7a = db_sess.query(Pupils).filter(Pupils.grade == "7А").all()
    sum_7a = 0
    for i in _7a:
        sum_7a += i.value

    _7b = db_sess.query(Pupils).filter(Pupils.grade == "7Б").all()
    sum_7b = 0
    for i in _7b:
        sum_7b += i.value

    _7c = db_sess.query(Pupils).filter(Pupils.grade == "7В").all()
    sum_7c = 0
    for i in _7c:
        sum_7c += i.value

    _8a = db_sess.query(Pupils).filter(Pupils.grade == "8А").all()
    sum_8a = 0
    for i in _8a:
        sum_8a += i.value

    _8b = db_sess.query(Pupils).filter(Pupils.grade == "8Б").all()
    sum_8b = 0
    for i in _8b:
        sum_8b += i.value

    _8c = db_sess.query(Pupils).filter(Pupils.grade == "8В").all()
    sum_8c = 0
    for i in _8c:
        sum_8c += i.value

    _9a = db_sess.query(Pupils).filter(Pupils.grade == "9А").all()
    sum_9a = 0
    for i in _9a:
        sum_9a += i.value

    _9b = db_sess.query(Pupils).filter(Pupils.grade == "9Б").all()
    sum_9b = 0
    for i in _9b:
        sum_9b += i.value

    _9c = db_sess.query(Pupils).filter(Pupils.grade == "9В").all()
    sum_9c = 0
    for i in _9c:
        sum_9c += i.value

    _10a = db_sess.query(Pupils).filter(Pupils.grade == "10А").all()
    sum_10a = 0
    for i in _10a:
        sum_10a += i.value

    _10b = db_sess.query(Pupils).filter(Pupils.grade == "10Б").all()
    sum_10b = 0
    for i in _10b:
        sum_10b += i.value

    _10c = db_sess.query(Pupils).filter(Pupils.grade == "10В").all()
    sum_10c = 0
    for i in _10c:
        sum_10c += i.value

    _11a = db_sess.query(Pupils).filter(Pupils.grade == "11А").all()
    sum_11a = 0
    for i in _11a:
        sum_11a += i.value

    _11b = db_sess.query(Pupils).filter(Pupils.grade == "11Б").all()
    sum_11b = 0
    for i in _11b:
        sum_11b += i.value

    _11c = db_sess.query(Pupils).filter(Pupils.grade == "11В").all()
    sum_11c = 0
    for i in _11c:
        sum_11c += i.value

    db_sess.close() # Заканчиваем сессию с БД
    # Показываем страницу с кол-ом кг для каждого класса
    return render_template("stats.html", title="Статитстика", sum_1a=sum_1a, sum_2a=sum_2a, sum_2b=sum_2b,
                           sum_3a=sum_3a, sum_3b=sum_3b, sum_3c=sum_3c, sum_4a=sum_4a, sum_4b=sum_4b, sum_4c=sum_4c,
                           sum_5a=sum_5a, sum_5b=sum_5b, sum_5c=sum_5c, sum_6a=sum_6a, sum_6b=sum_6b, sum_6c=sum_6c,
                           sum_7a=sum_7a, sum_7b=sum_7b, sum_7c=sum_7c, sum_8a=sum_8a, sum_8b=sum_8b, sum_8c=sum_8c,
                           sum_9a=sum_9a, sum_9b=sum_9b, sum_9c=sum_9c,
                           sum_10a=sum_10a, sum_10b=sum_10b, sum_10c=sum_10c,
                           sum_11a=sum_11a, sum_11b=sum_11b, sum_11c=sum_11c)


@app.route("/post1a", methods=["GET", "POST"]) # Адрес страницы для отправки данных по 1А классу
@login_required
def post1a():
    """
    Страница с формой отправки данных по 1А классу
    """
    grade = "1А"
    form = forms.pupil.Post1A() # Форма для отправки данных по 1А классу
    if form.validate_on_submit() and current_user.is_authenticated: # Если нажата кнопка "Отправить" и при этом пользователь аутентифицирован
        db_sess = db_session.create_session() # Созадть сессию с БД

        pupil = db_sess.query(Pupils).filter(Pupils.name == form.name.data and Pupils.grade == grade).first() # Извлечь из БД ученика по введённому имени и классу
        user = db_sess.query(User).filter(User.id == current_user.id).first() # Извлечь из БД текущего пользователя
        kilo = Kilograms() # Класс для отправки данных о кол-ве сданных килограммов. В нём кол-во кг, имя пользователя и ученика

        print(form.name.data, form.value.data)
        pupil.value += form.value.data # Увеличить сумму сданных учеником килограммов

        user.got_pupils += 1 # Увеличить кол-во обслуженных текущим пользователем посетителей
        user.got += form.value.data # Увеличить суммарное кол-во колиграммов, собранных текущим пользователем

        kilo.value = form.value.data # Кол-во кг
        kilo.user_id = current_user.id # ИД текущего пользователя
        kilo.pupil_id = pupil.id # ИД ученика

        db_sess.add(kilo) # Добавить в БД в таблицу с историей текущую информацию
        db_sess.commit() # Сохранить изменения
        db_sess.close() # Завершить сессию
        return redirect("/") # Открыть главную страницу

    return render_template("post_form.html", title=grade, form=form, grade=grade) # Открыть страницу с формой отправки данных по 1А классу

# Аналогично с другими классами


@app.route("/post2a", methods=["GET", "POST"])
@login_required
def post2a():
    """
    Страница с формой отправки данных по 2А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post2b", methods=["GET", "POST"])
@login_required
def post2b():
    """
    Страница с формой отправки данных по 2Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3a", methods=["GET", "POST"])
@login_required
def post3a():
    """
    Страница с формой отправки данных по 3А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3b", methods=["GET", "POST"])
@login_required
def post3b():
    """
    Страница с формой отправки данных по 3Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post3c", methods=["GET", "POST"])
@login_required
def post3c():
    """
    Страница с формой отправки данных по 3В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4a", methods=["GET", "POST"])
@login_required
def post4a():
    """
    Страница с формой отправки данных по 4А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4b", methods=["GET", "POST"])
@login_required
def post4b():
    """
    Страница с формой отправки данных по 4Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post4c", methods=["GET", "POST"])
@login_required
def post4c():
    """
    Страница с формой отправки данных по 4В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5a", methods=["GET", "POST"])
@login_required
def post5a():
    """
    Страница с формой отправки данных по 5А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5b", methods=["GET", "POST"])
@login_required
def post5b():
    """
    Страница с формой отправки данных по 5Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post5c", methods=["GET", "POST"])
@login_required
def post5c():
    """
    Страница с формой отправки данных по 5В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6a", methods=["GET", "POST"])
@login_required
def post6a():
    """
    Страница с формой отправки данных по 6А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6b", methods=["GET", "POST"])
@login_required
def post6b():
    """
    Страница с формой отправки данных по 6Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post6c", methods=["GET", "POST"])
@login_required
def post6c():
    """
    Страница с формой отправки данных по 6В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7a", methods=["GET", "POST"])
@login_required
def post7a():
    """
    Страница с формой отправки данных по 7А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7b", methods=["GET", "POST"])
@login_required
def post7b():
    """
    Страница с формой отправки данных по 7Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post7c", methods=["GET", "POST"])
@login_required
def post7c():
    """
    Страница с формой отправки данных по 7В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8a", methods=["GET", "POST"])
@login_required
def post8a():
    """
    Страница с формой отправки данных по 8А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8b", methods=["GET", "POST"])
@login_required
def post8b():
    """
    Страница с формой отправки данных по 8Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post8c", methods=["GET", "POST"])
@login_required
def post8c():
    """
    Страница с формой отправки данных по 8В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9a", methods=["GET", "POST"])
@login_required
def post9a():
    """
    Страница с формой отправки данных по 9А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9b", methods=["GET", "POST"])
@login_required
def post9b():
    """
    Страница с формой отправки данных по 9Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post9c", methods=["GET", "POST"])
@login_required
def post9c():
    """
    Страница с формой отправки данных по 9В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10a", methods=["GET", "POST"])
@login_required
def post10a():
    """
    Страница с формой отправки данных по 10А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10b", methods=["GET", "POST"])
@login_required
def post10b():
    """
    Страница с формой отправки данных по 10Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post10c", methods=["GET", "POST"])
@login_required
def post10c():
    """
    Страница с формой отправки данных по 10В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11a", methods=["GET", "POST"])
@login_required
def post11a():
    """
    Страница с формой отправки данных по 11А классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11b", methods=["GET", "POST"])
@login_required
def post11b():
    """
    Страница с формой отправки данных по 11Б классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/post11c", methods=["GET", "POST"])
@login_required
def post11c():
    """
    Страница с формой отправки данных по 11В классу
    """
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
        db_sess.close()
        return redirect("/")

    return render_template("post_form.html", title=grade, form=form, grade=grade)


@app.route("/stats1a") # Адрес страницы со статистикой по 1А классу
@login_required
def stats1a():
    """
    Страница со статистикой по 1А классу пофамильно
    """
    db_sess = db_session.create_session() # Сессия с БД
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "1А").all() # Все ученики 1А класса
    db_sess.close() # Конец сессии
    return render_template("stats_grade.html", db=pupils, grade="1А", title="1А статистика") # На страницу передаются все ученики 1А класса

# Аналогично с остальными
@app.route("/stats2a")
@login_required
def stats2a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "2А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="2А", title="2А статистика")


@app.route("/stats2b")
@login_required
def stats2b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "2Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="2Б", title="2Б статистика")


@app.route("/stats3a")
@login_required
def stats3a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="3А", title="3А статистика")


@app.route("/stats3b")
@login_required
def stats3b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="3Б", title="3Б статистика")


@app.route("/stats3c")
@login_required
def stats3c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "3В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="3В", title="3В статистика")


@app.route("/stats4a")
@login_required
def stats4a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="4А", title="4А статистика")


@app.route("/stats4b")
@login_required
def stats4b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="4Б", title="4Б статистика")


@app.route("/stats4c")
@login_required
def stats4c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "4В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="4В", title="4В статистика")


@app.route("/stats5a")
@login_required
def stats5a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="5А", title="5А статистика")


@app.route("/stats5b")
@login_required
def stats5b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="5Б", title="5Б статистика")


@app.route("/stats5c")
@login_required
def stats5c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "5В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="5В", title="5В статистика")


@app.route("/stats6a")
@login_required
def stats6a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="6А", title="6А статистика")


@app.route("/stats6b")
@login_required
def stats6b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="6Б", title="6Б статистика")


@app.route("/stats6c")
@login_required
def stats6c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "6В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="6В", title="6В статистика")


@app.route("/stats7a")
@login_required
def stats7a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="7А", title="7А статистика")


@app.route("/stats7b")
@login_required
def stats7b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="7Б", title="7Б статистика")


@app.route("/stats7c")
@login_required
def stats7c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "7В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="7В", title="7В статистика")


@app.route("/stats8a")
@login_required
def stats8a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="8А", title="8А статистика")


@app.route("/stats8b")
@login_required
def stats8b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="8Б", title="8Б статистика")


@app.route("/stats8c")
@login_required
def stats8c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "8В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="8В", title="8В статистика")


@app.route("/stats9a")
@login_required
def stats9a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="9А", title="9А статистика")


@app.route("/stats9b")
@login_required
def stats9b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="9Б", title="9Б статистика")


@app.route("/stats9c")
@login_required
def stats9c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "9В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="9В", title="9В статистика")


@app.route("/stats10a")
@login_required
def stats10a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="10А", title="10А статистика")


@app.route("/stats10b")
@login_required
def stats10b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="10Б", title="10Б статистика")


@app.route("/stats10c")
@login_required
def stats10c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "10В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="10В", title="10В статистика")


@app.route("/stats11a")
@login_required
def stats11a():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11А").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="11А", title="11А статистика")


@app.route("/stats11b")
@login_required
def stats11b():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11Б").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="11Б", title="11Б статистика")


@app.route("/stats11c")
@login_required
def stats11c():
    db_sess = db_session.create_session()
    pupils = db_sess.query(Pupils).filter(Pupils.grade == "11В").all()
    db_sess.close()
    return render_template("stats_grade.html", db=pupils, grade="11В", title="11В статистика")


@app.route("/history") # Адрес страницы с историей отправленных запросов
def history():
    """
    Страница с историей отправленных килограммов
    """
    db_sess = db_session.create_session() # Начало сессии с БД
    kilo = db_sess.query(Kilograms) # Вся таблица базы данных с историей отправлений
    db_sess.close() # Конец сессии
    return render_template("history.html", kilo=kilo) # Странице отправляется таблица


@app.route('/logout') # Адрес страницы, которая обеспечивает выход пользователя
@login_required
def logout():
    """
    Страница, которая обеспечивает выход пользователя из системы
    """
    logout_user() # Выход пользователя
    return redirect("/") # Направить на главную страницу


@app.route("/")
@app.route("/index") # Адрес главной страницы
def main_page():
    """
    Главная страница
    """
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST']) # Ссылка на страницу регистрации
def reqister():
    form = RegisterForm() # Форма регистрации
    if form.validate_on_submit(): # Если нажата кнопка "Зарегистрировать"
        if form.password.data != form.password_again.data: # Если введённые пароли не совпадают
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают") # Показать ту же страницу, но с ошибкой

        db_sess = db_session.create_session() # Сессия с БД
        if db_sess.query(User).filter(User.email == form.email.data).first(): # Если удалось найти в БД пользователя по введённой почте
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть") # Та же страница, но с ошибкой
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            is_admin=form.is_admin.data
        ) # Новый пользователь с введённой информацией
        user.set_password(form.password.data) # Зашифровать введённый пароль
        db_sess.add(user) # Добавить пользователя в БД
        db_sess.commit() # Сохранить изменения
        db_sess.close() # Завершить сессию
        return redirect('/') # Перейти на главную страницу
    return render_template('register.html', title='Регистрация', form=form) # Показать страницу с формой регистрации


@app.route("/kilo_delete/<int:id>", methods=["GET", "POST"]) # Адрес страницы для удаления из БД чьих-то килограммов
@login_required
def kilo_delete(id):
    """
    Удаление из БД записи о сданных учеником килограммах по полученному ID.
    :param id:
    :return:
    """
    db_sess = db_session.create_session() # Сессия с БД
    kilo = db_sess.query(Kilograms).filter(Kilograms.id == id).first() # Извлечь чьи-то колиграммы по полученному ID
    if kilo: # Если запись нашлась
        user_id = kilo.user_id # Извлечь ID волонтёра
        pupil_id = kilo.pupil_id # Извдечь ID ученика
        value = kilo.value # Извлечь кол-во килограммов

        user = db_sess.query(User).filter(User.id == user_id).first() # Найти в БД волонтёра по его ID
        pupil = db_sess.query(Pupils).filter(Pupils.id == pupil_id).first() # Найти в БД ученика по его ID

        user.got_pupils -= 1 # Уменьшаем кол-во обслуженных волонтёром учеников
        user.got -= value # Уменьшаем кол-во собранных волонтёром килограммов

        pupil.value -= value # Уменьшаем кол-во сданных учеником килограммов

        db_sess.delete(kilo) # Удаляем из БД килограммы
        db_sess.commit() # Сохраняем изменения
        db_sess.close() # Завершаем сессию
    else:
        abort(404) # Если в БД нет нужно записи, возвращаем ошибку 404
    return redirect("/history") # Переходим на страницу с историей отправки килограммов


@app.route("/user_delete/<int:id>", methods=["GET", "POST"]) # Адрес страницы для удаление волонтёра по его ID
@login_required
def user_delete(id):
    """
    Функция удаляет из БД волонтёра по его ID.
    TODO Нельзя удалить волонтёра, который отправил информацию по килограммам
    :param id:
    :return:
    """
    if current_user.is_admin: # Если текущий пользователь - админ
        db_sess = db_session.create_session() # Сессия с БД
        user = db_sess.query(User).filter(User.id == id).first() # Извлечь из БД волонтёра по полученному ID
        if user: # Если в БД есть такой волонтёр
            if user.id != current_user.id and user.got == 0: # Если волонтёр не удаляет себя и удаляемый волонтёр ничего не собрал
                db_sess.delete(user) # Удаляем
                db_sess.commit() # Сохраняем
                db_sess.close() # Завершаем сессию
        else:
            abort(404) # Иначе ошибка 404

    return redirect("/users") # Переходим на страницу с пользователями


@app.route("/users") # Адрес страницы с волонтёрами
def users():
    """
    Страница с волонтёрами. Показывает информацию о всех волонтёрах
    :return:
    """
    db_sess = db_session.create_session() # Сессия с БД
    user = db_sess.query(User) # Извлечь всех пользователей
    db_sess.close() # Завершить сессию
    return render_template("users.html", user=user) # Передать странице информацию о всех пользователях


@login_required
@app.route("/download_excel") # Адрес страницы для загрузки отчёта в файле .xlsx
def download_excel():
    """
    При нажатии на кнопку скачивается .xlsx файл с отчётом по всем классам
    TODO В глобальной версии не загружается xlsx файл, поэтому в глобальной версии загружается файл базы данных
    :return:
    """
    # Суммарное кол-во собранных классами килограммов
    global sum_1a, sum_2a, sum_2b, sum_3a, sum_3b, sum_3c, sum_4a, sum_4b, sum_4c, sum_5a, sum_5b, sum_5c, \
        sum_6a, sum_6b, sum_6c, sum_7a, sum_7b, sum_7c, sum_8a, sum_8b, sum_8c, sum_9a, sum_9b, sum_9c, \
        sum_10a, sum_10b, sum_10c, sum_11a, sum_11b, sum_11c

    if current_user.is_admin: # Если текущий пользователь - админ
        db_sess = db_session.create_session() # Сессия с БД
        tf = tempfile.NamedTemporaryFile() # Файл для заполнения
        filename = tf.name.split("\\")[-1] # Имя файла
        workbook = xlsxwriter.Workbook(f'{filename}.xlsx') # Создать файл
        grades = ["1А", "2А", "2Б", "3А", "3Б", "3В", "4А", "4Б", "4В", "5А", "5Б", "5В", "6А", "6Б", "6В",
                  "7А", "7Б", "7В", "8А", "8Б", "8В", "9А", "9Б", "9В", "10А", "10Б", "10В", "11А", "11Б", "11В"]

        sums = [sum_1a, sum_2a, sum_2b, sum_3a, sum_3b, sum_3c, sum_4a, sum_4b, sum_4c, sum_5a, sum_5b, sum_5c, \
        sum_6a, sum_6b, sum_6c, sum_7a, sum_7b, sum_7c, sum_8a, sum_8b, sum_8c, sum_9a, sum_9b, sum_9c, \
        sum_10a, sum_10b, sum_10c, sum_11a, sum_11b, sum_11c]

        worksheet = workbook.add_worksheet("Все классы") # Создать лист
        for i in range(len(grades)):
            worksheet.write(i, 0, grades[i]) # Записать в итую ячейку в первый столбик класс
            worksheet.write(i, 1, sums[i]) # Записать в итую ячейку во второй столбик сумму килограммов, собранную классом

        for i in grades:
            worksheet = workbook.add_worksheet(f"{i}") # Создать таблицу по каждому классу
            pupils = db_sess.query(Pupils).filter(Pupils.grade == i).all() # Извлечь всех учеников класса
            for num, pup in list(enumerate(pupils)):
                worksheet.write(num, 0, pup.name) # Записать в первый столбик имя ученика
                worksheet.write(num, 1, pup.value) # Записать во второй столбик кол-во киограммов, собранных учеником

        workbook.close() # Закрыть excel
        db_sess.close() # Завершить сессию с БД
        return send_from_directory("Flask_project/", f"/Flask_project/{filename}.xlsx") # Загрузить файл



def main():
    db_session.global_init("db/base.db") # Файл базы данных со всей информацией

    """
    Изначально база данных пустая. Следующий закоментированный код создаёт сессию для доступа к базе данных, перебирает
    каждый учебный класс (в следующем году их количество может измениться), открывает текстовый файл со списком 
    конкретного класса (названия файлов - {класс}.txt) и создаёт таблицу из двух столбцов: ФИ и класс. После цикла все 
    изменения в базе данных сохраняются.
    """
    """
    db_sess = db_session.create_session() # Создание сессии для доступа к БД
    for j in ["1А", "2А", "2Б", "3А", "3Б", "3В", "4А", "4Б", "4В", "5А", "5Б", "5В", "6А", "6Б", "6В", # Перебор классов
              "7А", "7Б", "7В", "8А", "8Б", "8В", "9А", "9Б", "9В", "10А", "10Б", "10В", "11А", "11Б", "11В"]:
        for i in open(f"E:/Code/Python/Flask_project/db/Grades/{j}.txt", encoding="utf-8").readlines(): # Перебор ФИ в файле
            pupil = Pupils() # Экземпляр на одного ученика для добавления в БД
            pupil.name = i.strip() # Имя из переменной во втором цикле
            pupil.grade = j # Класс из переменной в первом цикле
            db_sess.add(pupil) # Добавление ученика в БД

        db_sess.commit() # Сохранение изменений
    """

    app.run() # Запуск сайта


if __name__ == '__main__':
    main()
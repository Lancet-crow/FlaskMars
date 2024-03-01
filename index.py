from flask import Flask, render_template, redirect

from data import db_session
from data.users import User
from forms.user import RegisterForm
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировки', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
                   "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог",
                   "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер", "штурман",
                   "пилот дронов"]
    return render_template('list_prof.html', title='Список профессий', list=list, professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {"title": "Анкета", "surname": "Watny", "name": "Mark", "education": "выше среднего",
              "profession": "штурман марсохода", "sex": "male", "motivation": "Всегда мечтал застрять на Марсе!",
              "ready": "True"}
    return render_template('auto_answer.html', **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    db_session.global_init('db/mars_explorer.db')
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
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            address=form.address.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    astronauts = "Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"
    return render_template('distribution.html', title='Размещение по каютам', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

from flask import Flask, render_template

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

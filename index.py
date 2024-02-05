from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def return_index_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def return_promotion_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_mars')
def return_mars_image_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def return_promotion_image_page():
    lines = ("Человечество вырастает из детства",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!")
    url_style = url_for('static', filename='css/style.css')
    url_image = url_for('static', filename='img/mars.png')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_style}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_image}"</img>
                    <div class="alert alert-secondary">{lines[0]}</div>
                    <div class="alert alert-success">{lines[1]}</div>
                    <div class="alert alert-secondary">{lines[2]}</div>
                    <div class="alert alert-warning">{lines[3]}</div>
                    <div class="alert alert-danger">{lines[4]}</div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, world!'


@app.route('/info')
def info():
    return 'This is an informational page.'


@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1, num2):
    result = num1 + num2
    return f'The sum of {num1} and {num2} is {result}.'


@app.route('/calc/<path:invalid_data>')
def calc_error(invalid_data):
    return ('Error: both parameters must be numbers. Example:'
            ' /calc/3/5'), 400


@app.route('/reverse/<text>')
def reverse(text):
    # убираем пробелы и проверяем, не пустая ли строка
    if not text.strip():
        return 'Error: text must contain at least one non-space character.', 400

    reversed_text = text[::-1]
    return reversed_text


# Если /reverse/ вызван без текста
@app.route('/reverse/')
def reverse_empty():
    return 'Error: no text provided. Example: /reverse/hello', 400


# @app.route('/user/<name>/<int:age>')
# def user(name, age):
#     return f'Hello, {name}. You are {age} years old.'


# вроде этот вариант функции отрабатывает лучше
@app.route('/user/<name>/<age>')
def user(name, age):
    try:
        age_int = int(age)
    except ValueError:
        return "Error: age must be a number.", 400

    if age_int < 0:
        return "Error: age cannot be negative.", 400

    return f'Hello, {name}. You are {age} years old.'


@app.errorhandler(404)
def not_found(e):
    return 'Error 404: The page you requested does not exist.', 404


if __name__ == '__main__':
    app.run(debug=True)

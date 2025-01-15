#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route ('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route ('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p>{parameter}</p>'

@app.route ('/count/<int:parameter>')
def count(parameter):
    numbers = ''.join(f'{i}<br>' for i in range(parameter + 1))
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math (num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero is not allowed!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation!'

    return f'<p>The result of {num1} {operation} {num2} is: {result}</p>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

# Implement a solution using Flask that shows the message:
# 1. "Hello, developers!" on the web page root address and shows up the message "Insert two numbers";
# 2. "0.0" on the "/sum/" address;
# 3. "30.0" on the "/sum/10/20" address;
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    welcome = '<h1>Hello, developers!</h1>'
    message = '<p>Insert two numbers</p>'
    return welcome + message

@app.route('/sum/')
@app.route('/sum/<num1>/<num2>')
def sum_func(num1=0, num2=0):
    result = float(num1)+float(num2)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)

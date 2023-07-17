# Implement a solution using Flask that shows the message:
# 1. "Hello, developers!" on the web page root address and shows up the "/user/User" link;
# 2. "Hello, User!" on the "/user/" url and shows the message "change the browser address and reload the page";
# 3. "Hello, username!" on the "/user/username" address;
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    welcome = '<h1>Hello, developers!</h1>'
    link = '<p><a href="user/user">Click here!</a></p>'
    return welcome + link

@app.route('/user/')
@app.route('/user/<username>')
def user(username="User"):
    personalized = f'<h1>Hello, {username}!</h1>'
    instruction = '<p>Change the <em>browser address</em> name and reload the page.</p>'
    return personalized + instruction

if __name__ == '__main__':
    app.run(debug=True)

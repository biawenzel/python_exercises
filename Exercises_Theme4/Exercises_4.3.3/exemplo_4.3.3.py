# Implement a solution using Flask that shows the message "Main page" on the web page root address, "Hello, world!" on
# the "/hello/" address and "Hello, user!" on the "/hello/username" address
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Main page"

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world(username="world"):
    return "Hello, " + username + "!"

if __name__ == '__main__':
    app.run()

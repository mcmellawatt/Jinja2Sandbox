from flask import Flask, flash, redirect, render_template, request
from random import randint
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/user/")
def hello():
 
    users = [ "Frank", "Steve", "Alice", "Bruce" ]
    return render_template(
        'user.html', **locals())
 
@app.route("/template/")
def template():
    return render_template('child.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

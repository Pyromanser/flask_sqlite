import os
import sqlite3

from flask import Flask, render_template

from database import exec_query

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), 'db.sqlite3')


@app.route('/')
def index():
    users = []
    with sqlite3.connect(DATABASE) as conn:
        with conn as cursor:
            for row in cursor.execute("SELECT id,username,email,age FROM users"):
                users.append(row)
    return render_template("index.html", users=users)


@app.route('/users/<int:age>')
def users(age):
    users_qs = exec_query("SELECT id,username,email,age FROM users WHERE age=?", age)
    return render_template("index.html", users=users_qs)


if __name__ == '__main__':
    app.run(debug=True)

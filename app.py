from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URL'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))
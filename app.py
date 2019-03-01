from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/demo')
def index():
    return redirect(url_for('foo'))


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    return request.form['login']


app.run()

from flask import Flask, render_template, request, redirect, url_for, session
from scheme import User


app = Flask(__name__)
admin = User('admin', '123')
all_users = [admin]

@app.route('/')
def index():
    if 'current_user' in session:
        return render_template('logged.html')
    else:
        return redirect(url_for('login_page'))


@app.route('/login')
def login_page():
    return render_template('login.html', mode='LOGIN')


@app.route('/register')
def register_page():
    return render_template('login.html', mode='REGISTER')


@app.route('/auth', methods=['POST'])
def auth():
    login_user = User(request.form['login'], request.form['password'])
    if login_user in all_users:
        session['current_user'] = login_user
        return redirect(url_for('index'))
    else:
        return render_template('error.html')


@app.route('/logout')
def logout():
    session.pop('current_user', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3sdfsdfW@@@!dfsfskkmkmvkkyX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run()

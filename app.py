from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('logged.html')
    else:
        return redirect(url_for('login_page'))


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    session['username'] = request.form['login']
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3sdfsdfW@@@!dfsfskkmkmvkkyX R~XHH!jmN]LWX/,?RT'
app.run()

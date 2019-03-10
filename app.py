from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from scheme import User
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
admin = User('admin', '123')
all_users = [admin]


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = ('txt', 'jpg', 'jpeg')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_extensions(filename):
    file_ext = filename[filename.rfind('.') + 1:]
    if file_ext in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.route('/')
def index():
    if 'current_login' in session:
        return render_template('logged.html')
    else:
        return redirect(url_for('login_page'))


@app.route('/go')
def go_form():
    if 'current_login' in session:
        return render_template('go_form.html')
    else:
        return redirect(url_for('login_page'))


@app.route('/login')
def login_page():
    return render_template('login.html', mode='LOGIN')


@app.route('/register')
def register_page():
    return render_template('login.html', mode='REGISTER')


@app.route('/go', methods=['POST'])
def go():
        if 'file' not in request.files:
            flash('Вы не загрузили файл!')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Вы не выбрали файл для загрузки!')
            return redirect(request.url)
        if file and allowed_extensions(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
        else:
              flash('Разрешенные типы файлов: txt, jpg')
              return redirect(request.url)
              
                                  
 
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
                               
                               

@app.route('/auth', methods=['POST'])
def auth():
    login_user = User(request.form['login'], request.form['password'])
    if login_user in all_users:
        session['current_login'] = login_user.username
        return redirect(url_for('index'))
    else:
        return render_template('error.html')


@app.route('/logout')
def logout():
    session.pop('current_login', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3sdfsdfW@@@!dfsfskkmkmvkkyX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run()

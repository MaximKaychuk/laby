import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="M10112004g",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service1.users2 WHERE login=\'{0}\' AND password=\'{1}\';".format(str(username),
                                                                                                          str(password)))
            if username == '' or password == '':
                return render_template("login.html", error="Строки не должны быть пустыми")
            records = list(cursor.fetchall())

            if records == []:
                return render_template("login1_error.html")

            return render_template('account.html', full_name=records[0][1], username=records[0][2],
                                   password=records[0][3])

        elif request.form.get("registration"): #возвращает данные HTML-формы
            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        cursor.execute('SELECT * FROM service1.users2 WHERE login=\'{0}\''.format(str(login))) #индикатор для метода format, чтобы он был заменен первым (нулевым индексом) параметром format
        record = list(cursor.fetchall())
        if record:
            return render_template('username_exist.html')
        cursor.execute('INSERT INTO service1.users2 (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()

        return redirect('/login/')

    return render_template('registration.html')

#render_template = отображает шаблон template_name_or_list из папки шаблонов
app.run()




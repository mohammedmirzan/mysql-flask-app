from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="mrn@1234"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql = MySQL(app)

@app.route('/')
def Home():
    return render_template('welcome.html')

# Loading Homepage
@app.route('/data')
def data():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM users"
    con.execute(sql)
    res = con.fetchall()
    #flash("User details added")
    return render_template('data.html',datas=res)

# New User
@app.route('/addUsers', methods=['POST','GET'])
def newUser():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        phone = request.form['phone_number']
        con = mysql.connection.cursor()
        sql = "insert into users (NAME,AGE,CITY,PHONE_NUMBER) values (%s,%s,%s,%s)"
        con.execute(sql,[name, age, city, phone])
        mysql.connection.commit()
        con.close()
        flash("New user added")
        return redirect(url_for("data"))
    return render_template('addUsers.html')

#update user
@app.route('/editUser/<string:id>', methods=['POST','GET'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        phone = request.form['phone_number']
        sql = "update users set NAME=%s, AGE=%s, CITY=%s, PHONE_NUMBER=%s where ID=%s"
        con.execute(sql, [name,age,city,phone,id])
        mysql.connection.commit()
        con.close()
        flash("User details updated")
        return redirect(url_for('data'))
        con = mysql.connection.cursor()
    sql = "SELECT * from users where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template('editUser.html', datas=res)

# Delete User
@app.route('/deleteuser/<string:id>', methods=['GET'])
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "delete from users where id=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    flash("User details deleted")
    return redirect(url_for('data'))

if __name__ == '__main__':
    app.secret_key='mrn'
    app.run(debug=True, port=5000)
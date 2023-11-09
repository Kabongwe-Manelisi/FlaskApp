import mysql.connector as mysql
from flask import Flask, render_template, request, redirect
from tabulate import tabulate 

HOST = 'localhost'
DATABASE = 'appTest1'
USER = 'app1.0.0'
PASSWORD = ''

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print(db_connection.get_server_info())

cursor = db_connection.cursor(buffered=True)
cursor.execute('select database();')
database_name = cursor.fetchone()
print('[+] you are connected to the database:', database_name)




app = Flask(__name__)

cursor.execute('select * from Todo')
table = cursor.fetchall()
Todo = table

task_dictionary = { }

def ___repr__(self):
        
        return '<Task %r>' % self.id

            
@app.route('/', methods=['POST' , 'GET'])


def index():
    if request.method =='POST':
        task_content =request.form['content']
        def new_content(task_dictionary):
             task_dictionary['content'] = task_content
        new_content(task_dictionary)

        print(task_dictionary)


    else:
         return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
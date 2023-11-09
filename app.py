import mysql.connector as mysql
from flask import Flask, render_template, request, redirect
from tabulate import tabulate 

# database information
HOST = 'localhost'
DATABASE = 'appTest1'
USER = 'app1.0.0'
PASSWORD = ''

# database connection
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print(db_connection.get_server_info())

# database cursor
cursor = db_connection.cursor(buffered=True)
cursor.execute('select database();')
database_name = cursor.fetchone()
print('[+] you are connected to the database:', database_name)

app = Flask(__name__)

# fetch table data 
cursor.execute('select * from Todo')
table = cursor.fetchall()
Todo = table

# data source 
task_dictionary = { }

def ___repr__(self):
        
        return '<Task %r>' % self.id

            
@app.route('/', methods=['POST' , 'GET'])

# request function
def index():
    if request.method =='POST':
        task_content =request.form['content']

        # send data to data source
        def new_content(task_dictionary):
             task_dictionary[''] = task_content
        new_content(task_dictionary)
        print(task_dictionary)

        # iterate data in source
        for key in task_dictionary:
            content = key, task_dictionary[key]

            # push data to database
            cursor.execute ("""insert into Todo (content) values (
                            %s %s
             )""", params=(content))
            db_connection.commit()
            print('successfully added to database')

        return redirect('/')


    else:
         return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
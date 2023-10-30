import mysql.connector as mysql
from flask import Flask, render_template, request, redirect
from tabulate import tabulate 

HOST = 'localhost'
DATABASE = 'appTest1'
USER = 'app1.0.0'
PASSWORD = ''

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print(db_connection.get_server_info())

cursor = db_connection.cursor()
cursor.execute('select database();')
database_name = cursor.fetchone()
print('[+] you are connected to the database:', database_name)




app = Flask(__name__)


Todo = cursor.fetchone()

def ___repr__(self):
        
        return '<Task %r>' % self.id

            
@app.route('/', methods=['POST' , 'GET'])
def index():
    if request.method =='POST':
        task_content =request.form['content']
        new_task = Todo (content=task_content)

        try:
            cursor.execute("""
insert into Todo (id, content) values (
                           %s,%s
)
""", params=(id))
            db_connection.add(new_task)
            db_connection.commit()
            return redirect('/')
        except:
            return 'there was an issue adding your task'
        
    else:
        sql_statement = 'select * from Todo order by id'
        cursor.execute(sql_statement)
        tasks=cursor.fetchall()
        # tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
if __name__ == '__main__':
    app.run(debug=True)
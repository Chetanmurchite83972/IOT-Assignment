from flask import Flask,jsonify,request
from dbutils.execute import execute_select_query, execute_query

app = Flask(__name__)

@app.get('/')
def homepage():
    return "welcome to iot application"

@app.get('/salary')
def get_salary():
    query = f"select * from employee where salary = 45000;"

    salary = execute_select_query(query)

    return jsonify(salary)  

@app.post('/salary')
def insert_salary():
    salary = request.form.get('salary')

    query = f"insert into employee(empid,name,salary) values(10,'ddd',{30000})"

    execute_query(query)

    return"Salary added"



app.run(host='0.0.0.0', port=4000, debug=True)    

#Write a python program to print all employees,
#employees of given department, employee with highest and lowest salary
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb"
)


query = select * from employee column2,column3 where column5 desc; 

cursor = connection.cursor()

cursor.execute(query,val)

connection.commit()

cursor.close()
connection.close()
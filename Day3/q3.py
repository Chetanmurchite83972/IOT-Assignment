import mysql.connector

def delete_employee(empid): 
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb"
    )

    query = f"delete from employee where empid = %s;"
    val = (empid, )

    cursor = connection.cursor()

    cursor.execute(query, val)
    
    connection.commit()

    cursor.close()

    connection.close()

delete_employee(9)



import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb"
    )

def update_employee(empid,department):
    conn = get_connection()

    query = f"update employee SET department = %s where empid = %s;"
    val = (department,empid) 

    cursor = conn.cursor()

    cursor.execute(query,val)

    conn.commit()

    cursor.close()
    conn.close()

update_employee(9,"adc")      
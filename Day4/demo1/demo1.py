from dbutils.execute import execute_query
#from dbutils.execute import execute_select_query

def insert_value(uid, name, age):
    # type, location, value
    query = f"insert into persons(uid,name,age) values({uid}, '{name}', {age});"

    execute_query(query)

    print(f"{uid} Sensor's Value is inserted into table successfully")

 insert_value(1,"www",32)

# def get_age():
#     query = f"select * from persons where age= 23;"

#     age = execute_select_query(query)

    
#         print(f"name = {1}, age = {3}, mobile = {4}")

# get_age()


# create python environment :-
#   1. python -m venv myevn
#   2. .\myevn\Scripts\activate
# install package :- pip install psycopg2-binary

import psycopg2
from datetime import date

# make connnection
connection = psycopg2.connect(
    database='bankdb',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)

# get pointer or cursor
cursor = connection.cursor()
print("Database connected successfully")

# Insert data into table
# insert_query = """
# INSERT INTO employee (emp_id, fname, lname, email, dept, salary, hire_date)
# VALUES (%s, %s, %s, %s, %s, %s, %s)
# """
# cursor.execute(insert_query,(12,"Tejas","deshmukh","tejasdeshmukh123@gmail.com","Singing",90000,date(2024, 6, 1)))
# connection.commit()

# Update data of table
# update_query = """
# update employee
# set emp_id=%s
# where fname=%s
# """
# cursor.execute(update_query,(8,"Tejas"))
# connection.commit()

# delete data of table
# delete_query = """
# delete from employee
# where fname=%s
# """
# cursor.execute(delete_query,("Rahul",))
# connection.commit()

# get data from table
# select_query = "select * from employee order by emp_id"
# cursor.execute(select_query)
# records=cursor.fetchall()
# for row in records:
#     print(row)

# close connection
cursor.close()
connection.close()
print("Database connnection closed")
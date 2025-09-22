#excute-->this is method available in cusrsor helps to excute the sql queries.
#commit() --> to save the queries or changes
#close() -->

import mysql.connector
from db import info


#first conection established
try:
    conn=mysql.connector.connect(**info)
    print("connection established")
except:
    print('not able to connect')
cursor=conn.cursor()

#2.Create database
try:
    query='create database if not exists 1000coders_new2'
    cursor.execute(query)
    print('create database')
except:
    print('something wentwrong')

#3.use database
try:
    cursor.execute('use 1000coders_new1')
    print("now database is 10kcoders")
except:
    print('something went wrong')

#4.creating a table with id,name,email,course,joined_date
try:
    create_table="""create table if not exists students(
    id int auto_increment primary key,name varchar(30),email varchar(22),course varchar(10),joined_date date) """
    cursor.execute(create_table)
    print("Table create successfully")
except:
    print("table not created")

#5.inserting a single row data
def insertSingleRow(data):
    try:
        insertdata=""" insert into  students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
        cursor.execute(insertdata,data)
        print('insert data successfully')
    except:    
        print("data not insert in single row")
insertSingleRow(('shannu','shannu@gamil.com','python','2025-03-02'))
conn.commit()

#6.# insert multiple rows at a time
def insertMulRow(data):
    try:
        insertdata=""" insert into students (name,email,course,joined_date) values(%s,%s,%s,%s) """
        cursor.executemany(insertdata,data)
        print("data inserted multiple rows succefully at one")
    except Exception as e:
        print('Error inserting multiple rows:', e)

insertMulRow([('naveen','navven@gamil.com','java','2025-03-02'),
            ('tharun','tharun@gamil.com','ds','2025-03-02'),
             ('sathish','sathish@gamil.com','python','2025-03-02'),
             ('sharanya','sharanya@gamil.com','ds','2025-03-02')])
conn.commit()


#7.getrecords
def getrecords():
    try:
        qurey='select * from students'
        cursor.execute(qurey)
        results=cursor.fetchall()
        for row in results:
            print(row)
    except:
        print('error occured')
getrecords()

#8.getstudents by course
def getStudentByCourse(course_name):
    try:
        query="""select * from students where course=%s """
        cursor.execute(query,(course_name,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except Exception as e:
        print("something went wrong",e)
getStudentByCourse(('python'))


#9.updaterecordwithnewemail
def UpdateRecords(email):
    try:
        query2="update students set email=%s where name='tharun'"
        cursor.execute(query2,(email,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except Exception as e:
        print("Not a updated")
UpdateRecords("taruni123@gmail.com")

#10.deletesinglerecordbyemail
def getStudentByCourse(email):
    try:
        query="""delete from students where email=%s """
        cursor.execute(query,(email,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except Exception as e:
        print("not delated single row",e)
getStudentByCourse(('taruni123@gmail.com'))

# 10.deletemultipleeecordbyemail
def delMulRow(course):
    try:
        query="""delete from students where course=%s """
        cursor.execute(query,(course,))
        results=cursor.fetchall()
        for x in results:
            print(x)
    except Exception as e:
        print("not delated multiplesingle row",e)
delMulRow(('ds'))

conn.commit()
cursor.close()
conn.close()

'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
#for floating type we use real in database
cursor.execute("""CREATE TABLE courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("""INSERT INTO courses VALUES("02820","Python programming",5);""")
conn.commit()
conn.close()    #close the connection
'''
#TABLE ONCE CREATED DOBARA CHALAYA TO ERROR AS TABLE ALREADY EXISTS'''
#to avoid,
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
#for floating type we use real in database
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")

#cursor.execute("""INSERT INTO courses VALUES("02821","Python programming new",6);""") #enter new row

courses=('02457','Nonlinear Signal Processing',10)  #tuple
cursor.execute("INSERT INTO courses VALUES(?,?,?);",courses)    #tuple ko kaise daale? is format se dalta h
conn.commit()
conn.close()          
'''
#since pehli me starting me 0 hai to "" use kia h
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
#for floating type we use real in database
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")

courses=[('02454','Introduction to Cognitive Science',5),("02451",'Digital Signal Processing',10)]  #tuples in list
cursor.executemany("INSERT INTO courses VALUES(?,?,?);",courses)    # to execute many rows at a time we use executemany
conn.commit()
conn.close()          
'''
#to fetch data
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("SELECT * FROM courses;")
print(cursor.fetchone()) #return one row at a time with fetchone:
conn.commit()
conn.close()      
'''
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("SELECT * FROM courses;")
for row in cursor:          #if fetchall kr dete to ek line m aajaata
    print(row)
conn.commit()
conn.close()      
'''
#get all data returned into a python variable
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")    #limit krdeta h ki kitni rows chahiye
c=cursor.fetchall()
print(c)
conn.commit()               
conn.close()
'''
#python sql search data
'''
#jitni hogi sb aa jaygi
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("SELECT * FROM courses WHERE number=? OR name=? OR ects=?",('2451',None,None))   #jha kuch ni dena wha None
rows=cursor.fetchall()
print(rows)
conn.commit() 
conn.close()
'''
#parameterized search data into a python variable
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
param={'ects':10.0}
cursor.execute('SELECT number FROM courses WHERE ects = ?',(param['ects'],) )    #',' lagaya kyuki tuple dena h.. if na lagaate to string reh jaata
rows=cursor.fetchall()
print(rows)
conn.commit()     #jab changes hore h to krna h ni to ni
conn.close()
'''
#updating data 
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("UPDATE courses SET name=?, ects=? WHERE number=?",('Something new',10,'02457'))
cursor.execute("SELECT * FROM courses")
rows=cursor.fetchall()
print(rows)
conn.commit()
conn.close()
'''

#delete from sqlite ( primary key ki help se hota h)
'''
import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,ects real);""")
cursor.execute("DELETE FROM courses WHERE number=?",(2451,))
cursor.execute("SELECT * FROM courses")
rows=cursor.fetchall()
print(rows)
conn.commit() 
conn.close()
'''

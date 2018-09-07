import sqlite3 as sq


def connect(name):
    con=sq.connect(name)
    return con

def insert(tup2):
     cursor.execute("INSERT INTO student VALUES(NULL,?,?,?)",tup2)
     print("inserted..")
     
def update(tup3):
    cursor.execute("UPDATE student SET name=?, age=?, aim=? WHERE id=?",tup3)
    print("updated...")
    
def delete(tup4):
    cursor.execute("DELETE FROM student WHERE id=?",tup4)
    print("deleted...")

def search(tup1):
    cursor.execute("SELECT * FROM student WHERE id=? OR name=? OR age=? OR aim=?",tup1)
    print(cursor.fetchall())
    

def view():
    cursor.execute("SELECT * FROM student")
    for row in cursor:
        print(row)    
        
conn=connect("database1.db")
cursor=conn.cursor()   
cursor.execute("""CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name text,age INTEGER,aim text);""")

    
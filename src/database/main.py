import sqlite3
# connect to the database
conn = sqlite3.connect("database/college.sqlite3")
# execute the commands
cursor = conn.cursor()
# create
def create_table():
    query=""" CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL    
    )"""
    cursor.execute(query)
    conn.commit()
    print("Table created successfully")

create_table()


def insert_data(name,email,address):
    query="""INSERT INTO students(name,email,address) VALUES(?,?,?)"""
    cursor.execute(query,(name,email,address))
    conn.commit()
    print("Data inserted successfully")
    

def show_students():
    query = """SELECT * FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)

def update(id,name,email,address):
    query = """UPDATE students SET name=?,email=?,address=? WHERE id=?"""
    cursor.execute(query,(name,email,address,id))
    conn.commit()
    print("Data updated successfully")


def delete(id):
    query = """DELETE FROM students WHERE id=?"""
    cursor.execute(query,(id,))
    conn.commit()
    print("Data deleted successfully")



print("1. Insert Data 2. Show Data 3. Update Data 4. Delete Data 5. Exit")
option = int(input("Enter your choice: "))
if option == 1:
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    insert_data(name,email,address)
elif option == 2:
    show_students()
elif option == 3:
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    update(id,name,email,address)
elif option == 4:
    id = int(input("Enter id: "))
    delete(id)
else:
    print("Invalid choice")



# product: name,price,quantity,total
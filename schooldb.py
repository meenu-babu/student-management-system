import sqlite3
connection=sqlite3.connect("school.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student (reg_no VARCHAR(10) PRIMARY KEY,name TEXT)")
#cursor.execute("DROP TABLE IF EXISTS subject")
cursor.execute("CREATE TABLE IF NOT EXISTS subject(sub_id VARCHAR(10) PRIMARY KEY,sub VARCHAR(40))")
cursor.execute("CREATE TABLE IF NOT EXISTS result(res_id VARCHAR(10) PRIMARY KEY,marks INTEGER,reg_no VARCHAR(10),sub_id VARCHAR(10), FOREIGN KEY (reg_no) REFERENCES student(reg_no),FOREIGN KEY (sub_id) REFERENCES subject(sub_id))")
def addStudent():
    reg_no=input("Enter register number:")
    name = input("Enter student name: ")
    cursor.execute("INSERT INTO student(reg_no,name) VALUES (?,?)", (reg_no,name))
    connection.commit()
    print("New student added successfully...")
def editStudent():
    reg_no=input("Enter register number:")
    name = input("Enter student name: ")
    cursor.execute("UPDATE student SET name=? WHERE reg_no=?",(name,reg_no))
    connection.commit()
    print("student name updated successfully...")
def addSubject():
    sub_id=input("Enter subject ID:")
    sub=input("Enter subject name: ")
    cursor.execute("INSERT INTO subject(sub_id,sub) VALUES (?,?)", (sub_id,sub))
    connection.commit()
    print("New subject added successfully...")
def addMark():
    res_id=input("Enter result ID:")
    reg_no= input("Enter register number: ")
    sub_id=input("Enter the subject ID:")
    marks=input("Enter the mark : ")
    cursor.execute("INSERT INTO result(res_id,marks,reg_no,sub_id) VALUES (?,?,?,?)", (res_id,marks,reg_no,sub_id))
    connection.commit()
    print("Student mark added successfully...")
def viewMark():
    reg_no= input("Enter register number: ")
    view=cursor.execute("SELECT * FROM result WHERE reg_no=?",(reg_no,)).fetchall()
    if view:
        for row in view:
            print(row)
    else:
        print("No results found.")
    connection.commit()
def topper():
    sub_id =input("Enter subject ID: ")
    top=cursor.execute("SELECT s.name, r.Marks FROM student s JOIN result r ON s.reg_no = r.reg_no WHERE r.sub_id =? ORDER BY r.marks DESC LIMIT 1", (sub_id,)).fetchall()
    if top:
        for row in top:
            print(row)
    else:
        print("No results found.")
def avgMarkBySubject():
    sub_id = input("Enter subject ID: ")
    avg=cursor.execute("SELECT AVG(marks) FROM result WHERE sub_id = ?", (sub_id,)).fetchall()
    if avg:
        for row in avg:
            print(row)
    else:
        print("No results found.")
    connection.commit()
def topFive(): 
    top=cursor.execute("SELECT s.name , r.marks, su.sub FROM student s JOIN result r ON s.reg_no = r.reg_no JOIN subject su ON r.sub_id = su.sub_id ORDER BY r.marks DESC LIMIT 5").fetchall()
    print(top)
    connection.commit()
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Edit student name")
    print("3. Add subject")
    print("4. Add Marks")
    print("5. View Marks")
    print("6. Toppers by Subject")
    print("7. Average Marks by Subject")
    print("8. Top 5 Students")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        addStudent()
    elif choice == '2':
        editStudent()
    elif choice == '3':
        addSubject()
    elif choice == '4':
        addMark()
    elif choice == '5':
        viewMark()
    elif choice == '6':
        topper()
    elif choice == '7':
        avgMarkBySubject()
    elif choice == '8':
        topFive()
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice.....")
connection.close()
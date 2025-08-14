import sqlite3

# ------------------- DATABASE SETUP -------------------
def create_database():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()

    # Students table
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')

    # Teachers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject_expertise TEXT
        )
    ''')

    # Subjects table
    c.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')

    conn.commit()
    conn.close()

# ------------------- CRUD FUNCTIONS -------------------
# STUDENT CRUD
def add_student(name, age, grade):
    with sqlite3.connect("school.db") as conn:
        conn.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))

def view_students():
    with sqlite3.connect("school.db") as conn:
        return conn.execute('SELECT * FROM students').fetchall()

def update_student(student_id, name, age, grade):
    with sqlite3.connect("school.db") as conn:
        conn.execute('UPDATE students SET name=?, age=?, grade=? WHERE id=?', (name, age, grade, student_id))

def delete_student(student_id):
    with sqlite3.connect("school.db") as conn:
        conn.execute('DELETE FROM students WHERE id=?', (student_id,))

# TEACHER CRUD
def add_teacher(name, subject_expertise):
    with sqlite3.connect("school.db") as conn:
        conn.execute('INSERT INTO teachers (name, subject_expertise) VALUES (?, ?)', (name, subject_expertise))

def view_teachers():
    with sqlite3.connect("school.db") as conn:
        return conn.execute('SELECT * FROM teachers').fetchall()

def update_teacher(teacher_id, name, subject_expertise):
    with sqlite3.connect("school.db") as conn:
        conn.execute('UPDATE teachers SET name=?, subject_expertise=? WHERE id=?', (name, subject_expertise, teacher_id))

def delete_teacher(teacher_id):
    with sqlite3.connect("school.db") as conn:
        conn.execute('DELETE FROM teachers WHERE id=?', (teacher_id,))

# SUBJECT CRUD
def add_subject(name, teacher_id):
    with sqlite3.connect("school.db") as conn:
        conn.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))

def view_subjects():
    with sqlite3.connect("school.db") as conn:
        return conn.execute('''
            SELECT subjects.id, subjects.name, teachers.name 
            FROM subjects 
            LEFT JOIN teachers ON subjects.teacher_id = teachers.id
        ''').fetchall()

def update_subject(subject_id, name, teacher_id):
    with sqlite3.connect("school.db") as conn:
        conn.execute('UPDATE subjects SET name=?, teacher_id=? WHERE id=?', (name, teacher_id, subject_id))

def delete_subject(subject_id):
    with sqlite3.connect("school.db") as conn:
        conn.execute('DELETE FROM subjects WHERE id=?', (subject_id,))

# ------------------- MENU SYSTEM -------------------
def menu():
    create_database()

    while True:
        print("\n====== SCHOOL MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Teacher")
        print("6. View Teachers")
        print("7. Update Teacher")
        print("8. Delete Teacher")
        print("9. Add Subject")
        print("10. View Subjects")
        print("11. Update Subject")
        print("12. Delete Subject")
        print("13. Exit")

        choice = input("Enter your choice: ")

        # Student
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
            print("Student added.")

        elif choice == "2":
            for s in view_students():
                print(f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Grade: {s[3]}")

        elif choice == "3":
            sid = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(sid, name, age, grade)
            print("Student updated.")

        elif choice == "4":
            sid = int(input("Enter student ID: "))
            delete_student(sid)
            print("Student deleted.")

        # Teacher
        elif choice == "5":
            name = input("Enter teacher name: ")
            expertise = input("Enter subject expertise: ")
            add_teacher(name, expertise)
            print("Teacher added.")

        elif choice == "6":
            for t in view_teachers():
                print(f"ID: {t[0]}, Name: {t[1]}, Expertise: {t[2]}")

        elif choice == "7":
            tid = int(input("Enter teacher ID: "))
            name = input("Enter new name: ")
            expertise = input("Enter new expertise: ")
            update_teacher(tid, name, expertise)
            print("Teacher updated.")

        elif choice == "8":
            tid = int(input("Enter teacher ID: "))
            delete_teacher(tid)
            print("Teacher deleted.")

        # Subject
        elif choice == "9":
            name = input("Enter subject name: ")
            teacher_id = int(input("Enter teacher ID (or leave blank for none): ") or 0)
            add_subject(name, teacher_id if teacher_id != 0 else None)
            print("Subject added.")

        elif choice == "10":
            for sub in view_subjects():
                print(f"ID: {sub[0]}, Name: {sub[1]}, Teacher: {sub[2] or 'Unassigned'}")

        elif choice == "11":
            sid = int(input("Enter subject ID: "))
            name = input("Enter new subject name: ")
            teacher_id = int(input("Enter new teacher ID (or 0 for none): ") or 0)
            update_subject(sid, name, teacher_id if teacher_id != 0 else None)
            print("Subject updated.")

        elif choice == "12":
            sid = int(input("Enter subject ID: "))
            delete_subject(sid)
            print("Subject deleted.")

        elif choice == "13":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

# ------------------- RUN APP -------------------
if __name__ == "__main__":
    menu()

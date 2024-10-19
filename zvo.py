import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Surname TEXT,
    Department TEXT,
    DateOfBirth TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Teachers (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Surname TEXT,
    Department TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    ID INTEGER PRIMARY KEY,
    Title TEXT,
    Description TEXT,
    TeacherID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Exams (
    ID INTEGER PRIMARY KEY,
    Date TEXT,
    CourseID INTEGER,
    MaxScore INTEGER,
    FOREIGN KEY (CourseID) REFERENCES Courses(ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Grades (
    ID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    ExamID INTEGER,
    Score INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Students(ID),
    FOREIGN KEY (ExamID) REFERENCES Exams(ID)
)
''')

# Сохранение изменений
conn.commit()
conn.close()

print("База данных и таблицы успешно созданы!")
def create_connection():
    conn = sqlite3.connect('university.db')
    return conn

def add_student(conn, name, surname, Department, DateOfBirth):
    cursor = conn.cursor
    cursor.execute('''INSERT INTO Students (name, surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)''', (name, surname, Department, DateOfBirth))
    conn.commit()

def add_teacher(conn, name, surname, Department):
    cursor = conn.cursor
    cursor.execute('''INSERT INTO Teachers (name, surname, Department) VALUES (?, ?, ?)''', (name, surname, Department))
    conn.commit()

def add_course(conn, title, description, teacher_id):
    cursor = conn.cursor
    cursor.execute('''INSERT INTO Courses (title, description, teacher_id) VALUES (?, ?, ?)''', (title, description, teacher_id))
    conn.commit()

def add_exam(conn, date, course_id, max_score):
    cursor = conn.cursor
    cursor.execute('''INSERT INTO Exams (date, course_id, max_score) VALUES (?, ?, ?)''', (date, course_id, max_score))
    conn.commit()

def add_grade(conn, student_id, exam_id, score):
    cursor = conn.cursor
    cursor.execute('''INSERT INTO Grades (student_id, exam_id, score) VALUES (?, ?, ?)''', (student_id, exam_id, score))
    conn.commit()

def update_student(conn, student_id, name, surname, department, date_of_birth):
    cursor = conn.cursor()
    cursor.execute('''UPDATE Students
                      SET Name = ?, Surname = ?, Department = ?, DateOfBirth = ?
                      WHERE ID = ?''', (name, surname, department, date_of_birth, student_id))
    conn.commit()

def update_teacher(conn, teacher_id, name, surname, department):
    cursor = conn.cursor()
    cursor.execute('''UPDATE Teachers
                      SET Name = ?, Surname = ?, Department = ?
                      WHERE ID = ?''', (name, surname, department, teacher_id))
    conn.commit()

def update_course(conn, course_id, title, description, teacher_id):
    cursor = conn.cursor()
    cursor.execute('''UPDATE Courses
                      SET Title = ?, Description = ?, TeacherID = ?
                      WHERE ID = ?''', (title, description, teacher_id, course_id))
    conn.commit()

def delete_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Students WHERE ID = ?''', (student_id,))
    conn.commit()

def delete_teacher(conn, teacher_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Teachers WHERE ID = ?''', (teacher_id,))
    conn.commit()

def delete_course(conn, course_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Courses WHERE ID = ?''', (course_id,))
    conn.commit()

def delete_exam(conn, exam_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Exams WHERE ID = ?''', (exam_id,))
    conn.commit()

def get_students_by_department(conn, department):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE Department = ?''', (department,))
    return cursor.fetchall()

def get_courses_by_teacher(conn, teacher_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Courses WHERE TeacherID = ?''', (teacher_id,))
    return cursor.fetchall()

def get_students_by_course(conn, course_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT Students.* FROM Students
                      JOIN Grades ON Students.ID = Grades.StudentID
                      JOIN Exams ON Grades.ExamID = Exams.ID
                      WHERE Exams.CourseID = ?''', (course_id,))
    return cursor.fetchall()

def get_grades_by_course(conn, course_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT Grades.* FROM Grades
                      JOIN Exams ON Grades.ExamID = Exams.ID
                      WHERE Exams.CourseID = ?''', (course_id,))
    return cursor.fetchall()

def get_average_grade_by_course(conn, student_id, course_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT AVG(Grades.Score) FROM Grades
                      JOIN Exams ON Grades.ExamID = Exams.ID
                      WHERE Grades.StudentID = ? AND Exams.CourseID = ?''', (student_id, course_id))
    return cursor.fetchone()[0]

def get_average_grade(conn, student_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT AVG(Score) FROM Grades WHERE StudentID = ?''', (student_id,))
    return cursor.fetchone()[0]

def get_average_grade_by_department(conn, department):
    cursor = conn.cursor()
    cursor.execute('''SELECT AVG(Grades.Score) FROM Grades
                      JOIN Students ON Grades.StudentID = Students.ID
                      WHERE Students.Department = ?''', (department,))
    return cursor.fetchone()[0]

def main():
    conn = create_connection()
    create_tables(conn)


while True:
        print("Выберите действие:")
        print("1. Добавить студика")
        print("2. Добавить препода")
        print("3. Добавить курс")
        print("4. Добавить экзамен")
        print("5. Добавить оценку")
        print("6. Изменить информацию о студенте")
        print("7. Изменить информацию о преподе")
        print("8. Изменить информацию о курсе")
        print("9. Удалить студента")
        print("10. Удалить препода")
        print("11. Удалить курс")
        print("12. Удалить экзамен")
        print("13. Получить список студентов по факультету")
        print("14. Получить список курсов, читаемых преподавателем")
        print("15. Получить список студентов, зачисленных на курс")
        print("16. Получить оценки студентов по курсу")
        print("17. Средний балл студента по курсу")
        print("18. Средний балл студента в целом")
        print("19. Средний балл по факультету")
        print("20. Выйти")

        choice = input("Введите номер действия: ")

if choice == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            department = input("Введите факультет: ")
            date_of_birth = input("Введите дату рождения (YYYY-MM-DD): ")
            add_student(conn, name, surname, department, date_of_birth)
        elif choice == '2':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            department = input("Введите кафедру: ")
            add_teacher(conn, name, surname, department)
        elif choice == '3':
            title = input("Введите название курса: ")
            description = input("Введите описание курса: ")
            teacher_id = input("Введите ID преподавателя: ")
            add_course(conn, title, description, teacher_id)
        elif choice == '4':
            date = input("Введите дату экзамена (YYYY-MM-DD): ")
            course_id = input("Введите ID курса: ")
            max_score = input("Введите максимальный балл: ")
            add_exam(conn, date, course_id, max_score)
        elif choice == '5':
            student_id = input("Введите ID студента: ")
            exam_id = input("Введите ID экзамена: ")
            score = input("Введите оценку: ")
            add_grade(conn, student_id, exam_id, score)
        elif choice == '6':
            student_id = input("Введите ID студента: ")
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            department = input("Введите факультет: ")
            date_of_birth = input("Введите дату рождения (YYYY-MM-DD): ")
            update_student(conn, student_id, name, surname, department, date_of_birth)
        elif choice == '7':
            teacher_id = input("Введите ID преподавателя: ")
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            department = input("Введите кафедру: ")
            update_teacher(conn, teacher_id, name, surname,department)
        elif choice == '8':
            course_id = input("Введите ID курса: ")
            title = input("Введите название курса: ")
            description = input("Введите описание курса: ")
            teacher_id = input("Введите ID преподавателя: ")
            update_course(conn, course_id, title, description, teacher_id)
        elif choice == '9':
            student_id = input("Введите ID студента: ")
            delete_student(conn, student_id)
        elif choice == '10':
            teacher_id = input("Введите ID преподавателя: ")
            delete_teacher(conn, teacher_id)
        elif choice == '11':
            course_id = input("Введите ID курса: ")
            delete_course(conn, course_id)
        elif choice == '12':
            exam_id = input("Введите ID экзамена: ")
            delete_exam(conn, exam_id)
        elif choice == '13':
            department = input("Введите факультет: ")
            students = get_students_by_department(conn, department)
            for student in students:
                print(student)
        elif choice == '14':
            teacher_id = input("Введите ID преподавателя: ")
            courses = get_courses_by_teacher(conn, teacher_id)
            for course in courses:
                print(course)
        elif choice == '15':
            course_id = input("Введите ID курса: ")
            students = get_students_by_course(conn, course_id)
            for student in students:
                print(student)
        elif choice == '16':
            course_id = input("Введите ID курса: ")
            grades = get_grades_by_course(conn, course_id)
            for grade in grades:
                print(grade)
        elif choice == '17':
            student_id = input("Введите ID студента: ")
            course_id = input("Введите ID курса: ")
            avg_grade = get_average_grade_by_course(conn, student_id, course_id)
            print(f"Средний балл студента по курсу: {avg_grade}")
        elif choice == '18':
            student_id = input("Введите ID студента: ")


avg_grade = get_average_grade(conn, student_id)
            print(f"Средний балл студента в целом: {avg_grade}")
        elif choice == '19':
            department = input("Введите факультет: ")
            avg_grade = get_average_grade_by_department(conn, department)
            print(f"Средний балл по факультету: {avg_grade}")
        elif choice == '20':
            print("Выход из программы.")
            break
        else:
            print("Неккоректынй выбор")

    conn.close()


if name == "__main__":
    main()


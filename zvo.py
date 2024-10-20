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

def create_connection():
    conn = sqlite3.connect('university.db')
    return conn

def add_student(conn, name, surname, department, date_of_birth):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Students (Name, Surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)''', (name, surname, department, date_of_birth))
        conn.commit()
        print("Студент добавлен успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления студента: {e}")

def add_teacher(conn, name, surname, department):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)''', (name, surname, department))
        conn.commit()
        print("Преподаватель добавлен успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления преподавателя: {e}")

def add_course(conn, title, description, teacher_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Courses (Title, Description, TeacherID) VALUES (?, ?, ?)''', (title, description, teacher_id))
        conn.commit()
        print("Курс добавлен успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления курса: {e}")

def add_exam(conn, date, course_id, max_score):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Exams (Date, CourseID, MaxScore) VALUES (?, ?, ?)''', (date, course_id, max_score))
        conn.commit()
        print("Экзамен добавлен успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления экзамена: {e}")

def add_grade(conn, student_id, exam_id, score):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Grades (StudentID, ExamID, Score) VALUES (?, ?, ?)''', (student_id, exam_id, score))
        conn.commit()
        print("Оценка добавлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления оценки: {e}")

def update_student(conn, student_id, name, surname, department, date_of_birth):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE Students
                          SET Name = ?, Surname = ?, Department = ?, DateOfBirth = ?
                          WHERE ID = ?''', (name, surname, department, date_of_birth, student_id))
        conn.commit()
        print("Информация о студенте обновлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка обновления информации о студенте: {e}")

def update_teacher(conn, teacher_id, name, surname, department):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE Teachers
                          SET Name = ?, Surname = ?, Department = ?
                          WHERE ID = ?''', (name, surname, department, teacher_id))
        conn.commit()
        print("Информация о преподавателе обновлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка обновления информации о преподавателе: {e}")

def update_course(conn, course_id, title, description, teacher_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE Courses
                          SET Title = ?, Description = ?, TeacherID = ?
                          WHERE ID = ?''', (title, description, teacher_id, course_id))
        conn.commit()
        print("Информация о курсе обновлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка обновления информации о курсе: {e}")

def delete_student(conn, student_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Students WHERE ID = ?''', (student_id,))
        conn.commit()
        print("Студент удален успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления студента: {e}")

def delete_teacher(conn, teacher_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Teachers WHERE ID = ?''', (teacher_id,))
        conn.commit()
        print("Преподаватель удален успешно!")
    except sqlite3.Error as e :
        print(f"Ошибка удаления преподавателя: {e}")

def delete_course(conn, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Courses WHERE ID = ?''', (course_id,))
        conn.commit()
        print("Курс удален успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления курса: {e}")

def delete_exam(conn, exam_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Exams WHERE ID = ?''', (exam_id,))
        conn.commit()
        print("Экзамен удален успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления экзамена: {e}")

def get_students_by_department(conn, department):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Students WHERE Department = ?''', (department,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения списка студентов по факультету: {e}")
        return []

def get_courses_by_teacher(conn, teacher_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Courses WHERE TeacherID = ?''', (teacher_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения списка курсов преподавателя: {e}")
        return []

def get_students_by_course(conn, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT Students.* FROM Students
                          JOIN Grades ON Students.ID = Grades.StudentID
                          JOIN Exams ON Grades.ExamID = Exams.ID
                          WHERE Exams.CourseID = ?''', (course_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения списка студентов по курсу: {e}")
        return []

def get_grades_by_course(conn, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT Grades.* FROM Grades
                          JOIN Exams ON Grades.ExamID = Exams.ID
                          WHERE Exams.CourseID = ?''', (course_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения списка оценок по курсу: {e}")
        return []

def get_average_grade_by_course(conn, student_id, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT AVG(Grades.Score) FROM Grades
                          JOIN Exams ON Grades.ExamID = Exams.ID
                          WHERE Grades.StudentID = ? AND Exams.CourseID = ?''', (student_id, course_id))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка получения среднего балла студента по курсу: {e}")
        return None

def get_average_grade(conn, student_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT AVG(Score) FROM Grades WHERE StudentID = ?''', (student_id,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка получения среднего балла студента: {e}")
        return None

def get_average_grade_by_department(conn, department):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT AVG(Grades.Score) FROM Grades
                          JOIN Students ON Grades.StudentID = Students.ID
                          WHERE Students.Department = ?''', (department,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка получения среднего балла по факультету: {e}")
        return None

def main():
    conn = create_connection()
    while True:
        print("Выберите действие:")
        print("1. Добавить студента")
        print("2. Добавить преподавателя")
        print("3. Добавить курс")
        print("4. Добавить экзамен")
        print("5. Добавить оценку")
        print("6. Изменить информацию о студенте")
        print("7. Изменить информацию о преподавателе")
        print("8. Изменить информацию о курсе")
        print("9. Удалить студента")
        print("10. Удалить преподавателя")
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
            update_teacher(conn, teacher_id, name, surname, department)
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
            if avg_grade is not None:
                print(f"Средний балл студента по курсу: {avg_grade}")
            else:
                print("Ошибка получения среднего балла студента по курсу")
        elif choice == '18':
            student_id = input("Введите ID студента: ")
            avg_grade = get_average_grade(conn, student_id)
            if avg_grade is not None:
                print(f"Средний балл студента в целом: {avg_grade}")
            else:
                print("Ошибка получения среднего балла студента")
        elif choice == '19':
            department = input("Введите факультет: ")
            avg_grade = get_average_grade_by_department(conn, department)
            if avg_grade is not None:
                print(f"Средний балл по факультету: {avg_grade}")
            else:
                print("Ошибка получения среднего балла по факультету")
        elif choice == '20':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор")

    conn.close()

if __name__ == "__main__":
    main()


students = []

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

def get_students():
    for i in range(3):
        print("Enter student", i + 1)

        name = input("Name: ")
        age = input("Age: ")
        student_id = input("Student ID: ")

        student = Student(name, age, student_id)
        students.append(student)

def show_students():
    print("\nStudent List:")

    for s in students:
        print(s.name, "-", s.age, s.student_id)

if __name__ == "__main__":
    get_students()
    show_students()
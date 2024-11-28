#This lesson is about class methods in Python. They use cls as an argument

class Student:

    count: int = 0

    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"Name: {self.name} \nGPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f'Number of students: {cls.count}'


student1 = Student("Eric Rogers", 3.1)
student2 = Student("Sandy Richars", 2.3)

""" student_list: list[Student] = [student1, student2]
for student in student_list:
    print(student.get_info()) """

print(Student.get_count())

    

    
class Student:

    

    def __init__(self, name: str, dept: str, gpa: float):
        self.name = name
        self.dept = dept
        self.gpa = gpa
    
    def get_info(self):
        return f"Name: {self.name}\n Dept: {self.dept}\n GPA: {self.gpa}"
        

    @staticmethod
    def is_valid_dept(department):
        valid_depts = ["Biology", "Computer Science", "Maths"]
        return department in valid_depts




student1 = Student("George", "Biology", 4.5)
student2 = Student("Kevin", "Maths", 4.2)

print(student1.get_info())
print(student2.get_info())

print(Student.is_valid_dept("Computer Science"))
print(Student.is_valid_dept("Carpentry"))
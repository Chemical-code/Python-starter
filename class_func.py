# Declare class
from types import ClassMethodDescriptorType


class Student:
    # Class variables
    count = 0
    students = []

    # Class function
    @classmethod
    def print(cls):
        print("------ Student List ------")
        print("name\ttotal\taverage")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")
    
    # Instant function
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# Declare student list
Student("Yoon", 87, 98, 88, 95)
Student("Yeon", 92, 98, 96, 98)
Student("Goo", 76, 96, 94, 90)
Student("Na", 98, 92, 96, 92)
Student("Park", 95, 98, 98, 98)
Student("Lee", 64, 88, 92, 92)
Student("Kim", 82, 86, 98, 88)
Student("Seo", 88, 74, 78, 92)
Student("Jung", 97, 92, 88, 95)
Student("Kang", 45, 52, 72, 78)

# Print every student who formed
Student.print()
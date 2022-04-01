# Declare class
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

# Declare student list
students = [
    Student("Yoon", 87, 98, 88, 95),
    Student("Yeon", 92, 98, 96, 98),
    Student("Goo", 76, 96, 94, 90),
    Student("Na", 98, 92, 96, 92),
    Student("Park", 95, 98, 98, 98),
    Student("Lee", 64, 88, 92, 92)
]

# Declare student
student_a = Student("Yoon", 87, 98, 88, 95),
student_b = Student("Yeon", 92, 98, 96, 98),

# Repeat one by one
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a >  student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a <  student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)
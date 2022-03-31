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
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# Declare student list
students = [
    Student("Yoon", 87, 98, 88, 95),
    Student("Yeon", 92, 98, 96, 98),
    Student("Goo", 76, 96, 94, 90),
    Student("Na", 98, 92, 96, 92),
    Student("Park", 95, 98, 98, 98),
    Student("Lee", 64, 88, 92, 92)
]

# Repeat one by one
print("name", "total", "average", sep="\t")
for student in students:
    # Print
    print(student.to_string())
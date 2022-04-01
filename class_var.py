# Declare class
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # Reset instant variable
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # Add class parameter
        Student.count += 1
        print("{}th student is formed".format(Student.count))
    
# Declare student list
students = [
    Student("Yoon", 87, 98, 88, 95),
    Student("Yeon", 92, 98, 96, 98),
    Student("Goo", 76, 96, 94, 90),
    Student("Na", 98, 92, 96, 92),
    Student("Park", 95, 98, 98, 98),
    Student("Lee", 64, 88, 92, 92)
]

# Print
print()
print("The number of formed student is {} now.".format(Student.count))
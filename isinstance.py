# Declare student class
class Student:
    def study(self):
        print("Study")

# Declare teacher calss
class Teacher:
    def teach(self):
        print("Teach")

# Form object list inside the class
classroom = [Student(), Student(), Teacher(), Student(), Student()]

# Recall repeating proper function
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
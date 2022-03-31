# Declare function that returns dictionary
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# Declare student list
students = [
    create_student("Yoon", 87, 98, 88, 95),
    create_student("Yeon", 92, 98, 96, 98),
    create_student("Goo", 76, 96, 94, 90),
    create_student("Na", 98, 92, 96, 92),
    create_student("Park", 95, 98, 98, 98),
    create_student("Lee", 64, 88, 92, 92)
]

# Repeat one by one
print("name", "total", "average", sep="\t")
for student in students:
    # Calculate total and average
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    # Print
    print(student["name"], score_sum, score_average, sep="\t")
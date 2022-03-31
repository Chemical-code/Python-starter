# Declare student list
students = [
    {"name":"Yoon", "korean":87, "math":98, "english":88, "science":95},
    {"name":"Yeon", "korean":92, "math":98, "english":96, "science":98},
    {"name":"Goo", "korean":76, "math":96, "english":94, "science":90},
    {"name":"Na", "korean":98, "math":92, "english":96, "science":92},
    {"name":"Park", "korean":95, "math":98, "english":98, "science":98},
    {"name":"Lee", "korean":64, "math":88, "english":92, "science":92}
]

# Repeat one by one
print("name", "total", "average", sep="\t")
for student in students:
    # Calculate total and average
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    # Print
    print(student["name"], score_sum, score_average, sep="\t")
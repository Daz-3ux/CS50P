students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    # 表达式 \ 循环 \ 条件  
    student["name"] for student in students if student["house"] == "Gryffindor"
]
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
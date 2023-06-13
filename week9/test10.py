# filter

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# filter function
def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor)
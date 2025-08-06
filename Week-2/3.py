students = {
    'Vansh': 20,
    'Priyanshu': 20,
    'Kritika': 21,
    'Arpit': 20,
    'Yash': 19
}
print("Students with age greater than 20:")
for name, age in students.items():
    if age > 20:
        print(f"{name}: {age}")

students['Shaurya'] = 22
print(students.items())

students.pop('Shaurya')
print(students)
avg=0
for age in students.values():
    avg += age
avg /= len(students)
print(f"Average age of students: {avg}")
students=('Vansh', 'Priyanshu', 'Kritika', 'Arpit', 'Yash')
print(students)
temp=list(students)
temp.append('Shaurya')
students=tuple(temp)
print(students)
temp.remove('Shaurya')
students=tuple(temp)
print(students)
print(students[:4])

# no tuple values can not be modified directly but can be converted to list and then modified

temp[1] = 'Soumya'
students = tuple(temp)
print(students)
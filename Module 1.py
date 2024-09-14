grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
l_students = list(students)
l_students.sort()
grades[0]=sum(grades[0])/grades[0].__len__()
grades[1]=sum(grades[1])/grades[1].__len__()
grades[2]=sum(grades[2])/grades[2].__len__()
grades[3]=sum(grades[3])/grades[3].__len__()
grades[4]=sum(grades[4])/grades[4].__len__()
dict_students = {l_students[0]:grades[0], l_students[1]:grades[1], l_students[2]:grades[2],
                 l_students[3]:grades[3],l_students[4]:grades[4]}
print(dict_students)
    
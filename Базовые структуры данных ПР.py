def average(grades, students):
    student = list(students)
    count = {}
    for i in range(len(grades)):
        shift = sum(grades[i]) / len(grades[i])
        count[student[i]] = round(shift, 2)
    return count

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

print(average(grades, students))

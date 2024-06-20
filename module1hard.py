grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
students = list(students)  # преобразовываем множество в список
students.sort()  # сортируем список по алфавиту
av_grades = [(sum(grades[0])/len(grades[0])), (sum(grades[1])/len(grades[1])), (sum(grades[2])/len(grades[2])),
             (sum(grades[3])/len(grades[3])), (sum(grades[4])/len(grades[4]))]  # список со средними оценками
print(students[0])
print(av_grades[0])
st_grades = {students[0]: av_grades[0], students[1]: av_grades[1], students[2]: av_grades[2], students[3]: av_grades[3],
             students[4]: av_grades[4]}
print(st_grades)  # итоговый словарь
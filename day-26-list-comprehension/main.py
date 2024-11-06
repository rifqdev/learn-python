# numbers = [n * 2 for n in range(1, 5)]
# print(numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# short_name = [item for item in names if len(item) < 5]
# long_name = [item.upper() for item in names if len(item) > 5]
# print(short_name)

import random

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)
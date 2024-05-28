def insertion_sort_students(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0 and students[j]['grade'] > key['grade']:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key

# Example usage:
students = [
    {"name": "Hasham", "grade": 85},
    {"name": "Ehtesham", "grade": 70},
    {"name": "Maratib", "grade": 95},
    {"name": "Usman", "grade": 60},
    {"name": "Hassan", "grade": 80}
]

insertion_sort_students(students)
print("Sorted students by grade:")
for student in students:
    print(f"{student['name']}: {student['grade']}")

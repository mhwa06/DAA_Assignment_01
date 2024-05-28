def binary_search_students(students, target_grade):
    low = 0
    high = len(students) - 1
    while low <= high:
        mid = (low + high) // 2
        if students[mid]['grade'] == target_grade:
            return mid
        elif students[mid]['grade'] < target_grade:
            low = mid + 1
        else:
            high = mid - 1
    return -1
students = [
    {"name": "Usman", "grade": 60},
    {"name": "Ehtesham", "grade": 70},
    {"name": "Hassan", "grade": 80},
    {"name": "Hasham", "grade": 85},
    {"name": "Maratib", "grade": 95}
]

# Prompt the user to enter the grade to search for
target_grade = int(input("Enter the grade you want to search for: "))

index = binary_search_students(students, target_grade)
if index != -1:
    print(f"Student with grade {target_grade} found: {students[index]['name']}")
else:
    print(f"No student found with grade {target_grade}")

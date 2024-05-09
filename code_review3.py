# students = [
# #         {"name": "Bob", "info": {"grade": 95, "age": 22, "gpa": 3.9}},
#         {"name": "Alice", "info": {"grade": 90, "age": 20, "gpa": 3.8}},
#         {"name": "David", "info": {"grade": 95, "age": 20, "gpa": 3.95}},
        # {"name": "Charlie", "info": {"grade": 85, "age": 21, "gpa": 3.7}},
#         {"name": "Eve", "info": {"grade": 85, "age": 22, "gpa": 3.6}}
#     ]


def sort_students(students):
    n = len(students)#4
    swapped = True
    while swapped:
        swapped = False
        i = 0#0
        while i < n - 1:#3
            if compare_students(students[i + 1], students[i]):# stud[4] stud[3] => true
                students[i], students[i + 1] = students[i + 1], students[i]
                swapped = True
            i += 1
        n -= 1
    return students

def compare_students(student1, student2):
    #         {"name": "Eve", "info": {"grade": 85, "age": 22, "gpa": 3.6}}
    #         {"name": "Charlie", "info": {"grade": 85, "age": 21, "gpa": 3.7}},
    if student1['info']['grade'] > student2['info']['grade']:
        return True
    elif student1['info']['grade'] == student2['info']['grade']:
        if student1['info']['age'] < student2['info']['age']:
            return True
        elif student1['info']['age'] == student2['info']['age']:
            if student1['info']['gpa'] > student2['info']['gpa']:
                return True
    return False

def main():
    students = [
        {"name": "Alice", "info": {"grade": 90, "age": 20, "gpa": 3.8}},
        {"name": "Bob", "info": {"grade": 95, "age": 22, "gpa": 3.9}},
        {"name": "Charlie", "info": {"grade": 85, "age": 21, "gpa": 3.7}},
        {"name": "David", "info": {"grade": 95, "age": 20, "gpa": 3.95}},
        {"name": "Eve", "info": {"grade": 85, "age": 22, "gpa": 3.6}}
    ]
    sorted_students = sort_students(students)
    print("Sorted students:", sorted_students)

if __name__ == "__main__":
    main()

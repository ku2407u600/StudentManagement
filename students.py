students = [
    {'name': 'Aarav', 'enrollment': 'BCA101', 'marks': 85},
    {'name': 'Diya', 'enrollment': 'BCA102', 'marks': 72},
    {'name': 'Kabir', 'enrollment': 'BCA103', 'marks': 91},
]


def display_students(student_list):
    if not student_list:
        print('No student records available.')
        return
    print('Student Information')
    for student in student_list:
        print(f"Name: {student['name']}, Enrollment: {student['enrollment']}, Marks: {student['marks']}")


def average_marks(student_list):
    if not student_list:
        return 0
    total = sum(student['marks'] for student in student_list)
    return total / len(student_list)


def search_student(student_list, enrollment):
    for student in student_list:
        if student['enrollment'].lower() == enrollment.lower():
            return student
    return None

students = [
    {'name': 'Aarav', 'enrollment': 'BCA101', 'marks': 85},
    {'name': 'Diya', 'enrollment': 'BCA102', 'marks': 72},
    {'name': 'Kabir', 'enrollment': 'BCA103', 'marks': 91},
]


def display_students(student_list):
    if not student_list:
        print('No student records available.')
        return
    print('Student Records - Grade Management System')
    for student in student_list:
        print(f"Name: {student['name']}, Enrollment: {student['enrollment']}, Marks: {student['marks']}")


def validate_marks(marks):
    return 0 <= marks <= 100


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


def calculate_grade(marks):
    if not validate_marks(marks):
        return 'Invalid'
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    return 'F'

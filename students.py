students = []


def display_students(student_list):
    if not student_list:
        print('No student records available.')
        return
    print('Student Information')
    for student in student_list:
        print(f"Name: {student['name']}, Enrollment: {student['enrollment']}, Marks: {student['marks']}")

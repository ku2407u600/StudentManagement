from students import students, display_students, average_marks, search_student


def main():
    display_students(students)
    print(f'Average Marks: {average_marks(students):.2f}')
    result = search_student(students, 'BCA102')
    print('Search Result:', result if result else 'Student not found')


if __name__ == '__main__':
    main()

from students import students, display_students, average_marks


def main():
    display_students(students)
    print(f'Average Marks: {average_marks(students):.2f}')


if __name__ == '__main__':
    main()

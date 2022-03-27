import student_pb2


def main():
    students = student_pb2.StudentsDb()
    with open('students_db.bin', "rb") as f:
        students.ParseFromString(f.read())
    for s in students.students:
        print(s)


if __name__ == '__main__':
    main()

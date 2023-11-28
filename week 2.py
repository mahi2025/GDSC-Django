#simple student database program
students = {}  

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    section = input("Enter student's section: ")

    students[name] = {
        'age': age,
        'grade': grade,
        'section': section,
    }
    print('\n')
    print("The Student is added successfully.\n")

def view_student():
    name = input("Enter student's name: ")
    if name in students:  
        student = students[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        print("Section:", student['section'])
    else:
        print("The Student is not found.\n")

def list_students():
    if len(students) == 0:  
        print("There is no students in the database.\n")
    else:
        print("List of all students:")
        for name, student in students.items():  
            print("Name:", name)
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            print("Section:", student['section'])
        print()

def update_student():
    name = input("Enter student's name: ")
    if name in students:  
        print("The student information:")
        print("Name:", name)
        print("Age:", students[name]['age'])
        print("Grade:", students[name]['grade'])
        print("Section:", students[name]['section'])

        age = int(input("Enter updated age: "))
        grade = input("Enter updated grade: ")
        section = input("Enter the updated section: ")

        students[name]['age'] = age
        students[name]['grade'] = grade
        students[name]['section'] = section

        print("The Student's information is updated successfully.\n")
    else:
        print("The Student is not found.\n")

def delete_student():
    name = input("Enter student's name: ")
    if name in students:  
        del students[name]  
        print("The Student is deleted successfully.\n")
    else:
        print("The Student is not found.\n")

def display_menu():
    print("The Student Database Program")
    print("1. To add Student")
    print("2. To view Student")
    print("3. To list All Students")
    print("4. To update Student Information")
    print("5. To delete Student")
    print("6. To exit\n")

def main():
    print("Welcome ")
    
    while True:
        display_menu()
        choice = input("Enter your choice from 1-6: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("The program closed")
            break
        else:
            print("Invalid choice\n")

if __name__ == '__main__':
    main()
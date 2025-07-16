# SCHOOL MANAGEMENT SYSTEM

class Student:
    def _init_(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def update_grade(self, new_grade):
        self.grade = new_grade

    def display_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Grade:", self.grade)
        print("Marks:")
        if self.marks:
            for subject, mark in self.marks.items():
                print(f"  {subject}: {mark}")
        else:
            print("  No marks added yet.")
        print("-" * 30)

# Main program
students = []

def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    grade = input("Enter grade: ")
    s = Student(name, roll, grade)
    students.append(s)
    print("Student added successfully!\n")

def add_marks_to_student():
    roll = int(input("Enter roll number to add marks: "))
    found = False
    for student in students:
        if student.roll_no == roll:
            subject = input("Enter subject name: ")
            mark = int(input("Enter marks: "))
            student.add_marks(subject, mark)
            print("Marks added!\n")
            found = True
            break
    if not found:
        print("Student not found!\n")

def update_grade():
    roll = int(input("Enter roll number to update grade: "))
    for student in students:
        if student.roll_no == roll:
            new_grade = input("Enter new grade: ")
            student.update_grade(new_grade)
            print("Grade updated!\n")
            return
    print("Student not found!\n")

def show_all_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        student.display_info()

# Menu
while True:
    print("\n====== School Management Menu ======")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Update Grade")
    print("4. View All Students")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_marks_to_student()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        print("Exiting School Management System.")
        break
    else:
        print("Invalid choice. Try again.")
# student_grades.py
# Program to manage students' marks and calculate their average

def student_grade_system():
    num_students = int(input("Enter number of students: "))
    students = []

    for _ in range(num_students):
        name = input("\nEnter student name: ")
        marks = []

        # Collect marks for 3 subjects
        for i in range(1, 4):
            mark = float(input(f"Enter marks for Subject {i}: "))
            marks.append(mark)

        # Calculate average
        average = sum(marks) / 3
        students.append((name, marks, average))

    # Display results
    print("\n--- Student Grades ---")
    for student in students:
        print(f"Name: {student[0]}, Marks: {student[1]}, Average: {student[2]:.2f}")

# Run the program
if __name__ == "__main__":
    student_grade_system()

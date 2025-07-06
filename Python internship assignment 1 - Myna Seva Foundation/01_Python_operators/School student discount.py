age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
eligible = age <=18 or is_student
print("Eligible for discount?", eligible)

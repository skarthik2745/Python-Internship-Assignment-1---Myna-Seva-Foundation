n = input("Enter 2-digit number: ")
if len(n) == 2:
    s = int(n[0]) + int(n[1])
    print("Even sum" if s % 2 == 0 else "Odd sum")
else:
    print("Not a 2-digit number")

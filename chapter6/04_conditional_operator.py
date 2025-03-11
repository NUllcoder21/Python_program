marks = int(input("Enter your marks: "))

grade = "A" if marks >= 90 else ("B" if marks >= 70 else ("C" if marks >= 50 else "F"))
print(f"Your grade is: {grade}")

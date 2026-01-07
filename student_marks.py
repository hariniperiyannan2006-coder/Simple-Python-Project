name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Result:", result)
student_name = input("Enter student name: ")
marks = float(input("Enter marks (0 - 100): "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
else:
    if marks >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print("\n--- Student Result ---")
    print("Student Name :", student_name)
    print("Marks        :", marks)
    print("Result       :", result)

students_marks = {
    "Alice": 85 
}
student_name = input("Enter the student's name: ")

if student_name in students_marks:
    print(f"{student_name}'s marks: {students_marks[student_name]}")
else:
    print("Error: The student not found.")

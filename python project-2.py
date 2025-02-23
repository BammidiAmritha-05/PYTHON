def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 85:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 50:
        return 'C'
    else:
        return 'Fail'

def save_grade_to_file(student_name, marks, grade):
    with open("student_grades.txt", "a") as file:
        file.write(f"{student_name:<15}{str(marks):<25}{grade}\n")

def display_summary(students):
    """Displays all student data in a formatted table after input is complete."""
    print("\nFinal Grade Summary:")
    print(f"{'Student Name':<15}{'Marks':<25}{'Grade'}")
    print("-" * 50)
    for student in students:
        print(f"{student['name']:<15}{str(student['marks']):<25}{student['grade']}")

def main():
    students = []  # List to store student records

    while True:
        student_name = input("\nEnter student name (or type 'exit' to stop): ")
        if student_name.lower() == 'exit':
            break

        marks_input = input("Enter marks separated by space: ").split()
        
        if all(m.isdigit() for m in marks_input):
            marks = list(map(int, marks_input))
        else:
            print("Error: Please enter only numeric values for marks.")
            continue  # Ask for input again

        grade = calculate_grade(marks)
        print(f"Student: {student_name}, Marks: {marks}, Grade: {grade}")

        save_grade_to_file(student_name, marks, grade)

        # Store student details for final display
        students.append({"name": student_name, "marks": marks, "grade": grade})
    
    # Display final summary table
    display_summary(students)
    print("\nAll grades saved successfully!")

if __name__ == "__main__":
    main()

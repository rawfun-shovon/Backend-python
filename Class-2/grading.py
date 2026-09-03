r'''Asks the user for their name and their marks.
First checks the marks are valid (0–100); if not, prints "Invalid marks" .
Otherwise prints the grade using if / elif / else'''

# 80+ → A+
# 70–79 → A
# 60–69 → A-
# 50–59 → B
# 40–49 → C
# <40 → F

# IN CLASS ASSIGNMENT 

print("--- Student Grading System ---")

student_name = input("Please enter your name: ")
while True:
    try:
        marks = float(input("Please enter your marks: "))
        if marks <0 or marks >100:
            print("Invalid marks! Please enter a number between 0 and 100.")
            continue
        break
    except ValueError:
        print("Something went wrong! Please enter a numeric value.")
        
print("")
print(f"Hello {student_name}. Your marks are {marks}.")

while True:
    if marks >79:
        grade = "A+"
    elif marks > 69 and marks < 80:
        grade = "A"
    elif marks > 59 and marks < 70:
        grade = "A-"
    elif marks > 49 and marks < 60:
        grade = "B"
    elif marks > 40 and marks < 50:
        grade = "C"
    else:
        grade = "F"
    break
print("")
print("Your grade is: ", grade)

list_of_courses=["Math", "Science", "English", "History", "Art", "Music", "Physical Education", "Computer Science"]
study_days=("sunday", "monday", "tuesday", "wednesday", "thursday")
Numbers_set={10, 20, 30, 40, 50,10, 20, 30, 40, 50}

print("\n            Welcome to the Student Information System!      \n")

yes_or_no=input("Do you want to enter the student's information? (yes/no): ")
while yes_or_no.lower() != "yes" and yes_or_no.lower() != "no":
    yes_or_no=input("Invalid input. Please enter 'yes' or 'no': ")

if yes_or_no.lower() == "no":
    print("\n        Thank you for using the Student Information System. Goodbye!\n")
    exit()

list_of_students=[]
while yes_or_no.lower() == "yes": 
    student_name=input("Enter the student's name: ")
    student_age=int(input("Enter the student's age: "))
    department=input("Enter the student's department: ")
    student_grade=int(input("Enter the student's grade: "))
    print('\n')
    result=""
    while student_grade < 0 or student_grade > 100:
        student_grade=int(input("Invalid grade. Please enter a grade between 0 and 100: "))
    if student_grade >= 90:
        result="A"
    elif student_grade >= 80:
        result="B"
    elif student_grade >= 70:
        result="C"
    elif student_grade >= 60:
        result="D"
    else:
        result="F"
    student_info={}
    student_info.update({"name": student_name, "age": student_age, "department": department, "score": student_grade, "result": result})
    list_of_students.append(student_info)
    print("          Student added successfully!   \n")
    print(f"Information of {student_name} is:")
    for key, value in student_info.items():
        print(f"{key}: {value}")
    print('\n')
    yes_or_no=input("Do you want to add another student? (yes/no): ")

print("\nAll the courses offered are:", list_of_courses)
print("The study days are:", study_days,'\n')
print("The unique numbers in the set are:  (Removal of duplicates) ", Numbers_set,'\n')
print("\n           Students Information Summary      \n")
for student in list_of_students:
    print(f"Information of {student['name']} is:")
    for key, value in student.items():
        print(f"{key}: {value}")
    print('\n')

print("Total number of students :", len(list_of_students),'\n')

failed=0
passed=0
for student in list_of_students:
    if student['result']=='F':
        failed+=1
    else:
        passed+=1

print("Total number of students who passed :", passed)
print("Total number of students who failed :", failed)

list_of_grades=[]
for student in list_of_students:
    list_of_grades.append(student['score'])

print("The highest grade is :", max(list_of_grades))
print("The lowest grade is :", min(list_of_grades))
print("The average grade is :", sum(list_of_grades)/len(list_of_grades),'\n')
print("             see you next time! \n\n")



# I am having the number of students. this part allows me to control first loop, I will get grades from user until we reach last student.

number_of_students = int(input("Number of students: "))

grades = [] # a list to store all student grades 

# collecting grades from the user 
for i in range(number_of_students):
    grade = int(input("Enter grade: "))
    grades.append(grade)

# counter for students who failed or passed.    
passed = 0
failed = 0

for grade in grades:
    if grade >= 50:
        passed += 1; # if grade equal or more than 50 we increase the counter by 1
    else:
        failed += 1;

average = sum(grades) / len(grades); # in order to calculete avarage grade. we need to know total of grades and  length of array

print("Average grade:", average)
print("Number of students who passed:", passed)
print("Number of students who failed:", failed)



import itertools


# asks for students name and repeatedly grade until a valid grade between 0 100
# once valid , it stores the grade in the dict as key=name,value=grade
def add_student_scores(students):
    name = input("Student name: ")
    while True:
        try:
            grade = int(input("Enter the grade: "))
            if 0 <= grade <= 100:
                students[name] = grade
                break
            else:
                print(" grade must be between 0 and 100.")
        except ValueError:
            print("enter a valid number")

def view_all_scores(students):
    # check if dict is empty, if it is print message and stops
    if not students:
        print("no student data exists")
        return
    #if not empty, loop thourgh each student name and prints name with its score
    for name in students:
        print(name, students[name])


def calculate_stats(students):
    if not students:
        print("no student data exists")
        return
    scores = list(students.values())
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("average : ", avg)
    print("highest: ", highest)
    print("lowest: ", lowest)

#check if exist in the dict and prints score if found
#   otherwise print error message
def search_student_score(students):
    name = input("Enter students name: ")
    if name in students:
        print("score: ", students[name])
    else:
        print("student not found")


def main():
    students = {}
    while True:
        print("\n1. Add student scores")
        print("2. View all student scores")
        print("3. Calculate statistics")
        print("4. Search student score")
        print("5. Exit")

        user_choice = input("Choose an option: ")

        if user_choice == "1":
            add_student_scores(students)
        elif user_choice == "2":
            view_all_scores(students)
        elif user_choice == "3":
            calculate_stats(students)
        elif user_choice == "4":
            search_student_score(students)
        elif user_choice == "5":
            print("exiting program")
            break
        else:
            print("choice must be 1 - 5, try again")

if __name__ == "__main__":
    main()
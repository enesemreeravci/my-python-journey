

def question_1():
    print("What is the capital of France?")
    print("1. London")
    print("2. Paris")
    print("3. Rome")

def question_2():
    print("What is 5 + 7?")
    print("1. 12")
    print("2. 11")
    print("3. 13")

def question_3():
    print("In what decade was the internet created?")
    print("1. 1970's")
    print("2. 1950's")
    print("3. 1960's")

def question_4():
    print("What’s the only even prime number?")
    print("1. 0")
    print("2. 2")
    print("3. 4")

def question_5():
    print("What is the term for harmful software such as viruses or ransomware?")
    print("1. Virus")
    print("2. Fish")
    print("3. Malware")

def rules():
    print("Welcome to the Quiz Game!")
    print("---------------------------")
    print("Here are the rules:")
    print("1. There are 5 questions in total.")
    print("2. Each question has 3 possible answers.")
    print("3. Type the number (1, 2, or 3) of your chosen answer.")
    print("4. Each correct answer gives you 1 point.")
    print("5. Try to get all answers correct — good luck!")
    print("---------------------------")

while True:
    print("Welcome to the Python Quiz Game!")
    print("1. Start Quiz")
    print("2. View Rules")
    print("3. Exit Quiz")

    store_correct_answers = 0
    choice = int(input("Choose an option: "))
    if choice == 1:
        question_1()
        answer = int(input("Your answer: "))
        if answer == 2:
            print("Correct!")
            store_correct_answers += 1
        else :
            print("Incorrect!")
        question_2()
        answer2 = int(input("Your answer: "))
        if answer2 == 1:
            print("Correct!")
            store_correct_answers += 1
        else :
            print("Incorrect!")
        question_3()
        answer3 = int(input("Your answer: "))
        if answer3 == 3:
            print("Correct!")
            store_correct_answers += 1
        else :
            print("Incorrect!")
        question_4()
        answer4 = int(input("Your answer: "))
        if answer4 == 2:
            print("Correct!")
            store_correct_answers += 1
        else :
            print("Incorrect!")
        question_5()
        answer5 = int(input("Your answer: "))
        if answer5 == 3:
            print("Correct!")
            store_correct_answers += 1
        elif answer5 == 4:
            print("Incorrect!")

        print("Thank you for using this quiz!")
        print("You answered " , str(store_correct_answers), "out of 5 questions correctly!")
        if store_correct_answers >= 4:
            print("Good job!")
        elif store_correct_answers <= 3:
            print("Keep practicing!")
        print("Do you want to play again?")
        choice_last = str(input("yes/no: "))
        if choice_last == "yes":
            continue # goes back to the beginning of whilelopp
        elif choice_last == "no":
            print("Thank you for playing!")
            break
    if choice == 2:
        rules()
    if choice == 3:
        print("End Quiz! Bye")
        break
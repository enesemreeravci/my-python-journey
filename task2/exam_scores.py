

score1 = int(input("Enter your score for subject 1: "))
score2 = int(input("Enter your score for subject 2: ")) # i could put these are in a loop, but deadline is so close.
score3 = int(input("Enter your score for subject 3: "))

average_score = (score1 + score2 + score3) / 3;

print("Your avarage score is:", average_score)

if (average_score >= 85):
    print("Feedback: Excellent")
elif(average_score <= 84 and average_score >= 70):
    print("Feedback: Good")
else:
    print("Feedback: Need Improvment")
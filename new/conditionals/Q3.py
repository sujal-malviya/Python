#Grade Calculator
score = int(input("say me the score : "))
if (score>=101):
    print("Enter valid score ")
    exit()  
if (score>=90 and score <=100):
    print("Grade = A")
elif(score>=80):
    print("Grade = B")
elif (score>=70):
    print("Grade = C")
elif (score >= 60):
    print("Grade = D")
else:
    print("Grade = F")
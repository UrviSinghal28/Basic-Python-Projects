quizBegin=input('Are you ready for the quiz?\n')

if quizBegin.lower() not in (['yes','y']):
    quit()

print("To quit the game at any moment just type 'quit' as the answer to any question")
print("Great! Let's Begin")
score=0
ques=0

question=input("Question 1: What is the name of the main antagonist in the Shakespeare play Othello?\n")
ques+=1
if question.lower()=='lago':
    print('Correct!')
    score+=1
elif question.lower()=='quit':
    print('Thank you for playing!')
    quit()
else:
    print('Incorrect!')

question=input("Question 2: What element is denoted by the chemical symbol Sn in the periodic table?\n")
ques+=1
if question.lower()=='tin':
    print('Correct!')
    score+=1
elif question.lower()=='quit':
    print('Thank you for playing!')
    quit()
else:
    print('Incorrect!')

question=input("Question 3: What is the smallest planet in our solar system?\n")
ques+=1
if question.lower()=='mercury':
    print('Correct!')
    score+=1
elif question.lower()=='quit':
    print('Thank you for playing!')
    quit()
else:
    print('Incorrect!')

question=input("Question 4: From what grain is the Japanese spirit Sake made?\n")
ques+=1
if question.lower()=='rice':
    print('Correct!')
    score+=1
elif question.lower()=='quit':
    print('Thank you for playing!')
    quit()
else:
    print('Incorrect!')

question=input("Question 5: Which Disney Princess called Gus and Jaq friends?\n")
ques+=1
if question.lower()=='cinderella':
    print('Correct!')
    score+=1
elif question.lower()=='quit':
    print('Thank you for playing!')
    quit()
else:
    print('Incorrect!')

print(f"You got {score} questions correct out of {ques} questions\nThank you for playing!")



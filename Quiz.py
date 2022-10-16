print("Welcome my quiz!")

starting = input("Are you ready for the quiz? ")
print(starting)

if starting.lower() != "yes":
    quit()
print("Okay! Let's play it!!!")
score=0

answer = input("What does pwd stand for ? ")
if answer.lower() =="print working directory" : 
    print("Correct!")
    score +=1
else: print("Opps!!! Incorrect!")

answer = input("What does commond 'chmond+x' meaning ? ")
if answer.lower() =="modified textfile" : 
    print("Correct!")
    score +=1
else: print("Opps!!! Incorrect!")

answer = input("What does commond 'nano' meaning ? ")
if answer.lower() =="text editor" : 
    print("Correct!")
    score +=1
else: print("Opps!!! Incorrect!")

answer = input("What does commond 'read' meaning in bash ? ")
if answer.lower() =="input" : 
    print("Correct!")
    score +=1
else: 
    print("Opps!!! Incorrect!")
print("You got "+ str(score) +" points! ")
print("You got "+ str(score/4 *100) +" %! ")
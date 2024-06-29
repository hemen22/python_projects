print("welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes": # .lower() to convert input to lower case
      quit()

print("okay! Let's play:)")  
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
     print('Correct!')
     score+=1
else:
    print('incorrect!')
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
     print('Correct!')
     score+=1
else:
    print('incorrect!')
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory": 
     print('Correct!')
     score+=1
else:
    print('incorrect!')
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
     print('Correct!') 
     score+=1
else:
    print('incorrect!')

print("You got " + str(score) +" questions correct !") # use space after got and before question to have a space in the output
print("You got " + str((score/4)*100) +"%.")
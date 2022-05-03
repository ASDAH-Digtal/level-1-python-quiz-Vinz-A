from tkinter.messagebox import YES


print("This quiz is about Demon Slayer  this is multiple choice. Choose one of the options and you will get points if you are correct.Then we will start the quiz, Are You ready?")

ready = input("\na) Yes\nb) No\n>>")

if ready == "Yes" or ready == "a":
    print("Good, Lets start")
elif ready == "No" or ready == "b":
    print("Too bad, Lets start")
else:
    print("I will take that as a yes")

score = 0 
q1 = input("Which of these is NOT one of the breathing forms?\na) Water\nb) Gravity\nc) Sound\nd) Wind\n>>") 

if q1 == "Gravity" or q1 == "b":
    print("Correct +1")
else:
    print("Incorrct")

q2 = input("What is the name of the main antagonist?\na) Akaza\nb) Nezuko Kamado\nc) Muzan Kibutsuji\nd) Michael Jackson\ne>>") 

if q2  == "Muzan Kibutsuji" or q2 == "c":
    print("Correct +1")
else:
    print("incorrect")

q3 = input("What is the name of the yellow-haired boy?\na) Tanjiro\nb) Nezuko\nc) Inosuke\nd) Zenistu\ne")  

if q3 == "Zenistu" or "d":
    print("Correct +1")
else:
    print("Incorrect")

q4 = input("What breathing form does Rengoku use?\na) Water\nb) Earth\nc) Fire\nd) Air/ne)")
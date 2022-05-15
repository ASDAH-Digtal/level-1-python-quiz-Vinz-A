from tkinter.messagebox import YES

# Introduction
print("This quiz is about Demon Slayer this is multiple choice. Choose one of the options and you will get points if you are correct. Then we will start the quiz, Are You ready?")

# Are you ready question
ready = input("\na) Yes\nb) No\n>>")

if ready == "Yes" or ready == "a" or ready == "yes":
    print("Good, Lets start")
elif ready == "No" or ready == "b" or ready == "no":
    print("Too bad, Lets start")
else:
    print("I will take that as a yes")


# Questions 1-12
score = 0 
q1 = input("Question 1: Which of these is NOT one of the breathing forms? (By the way just put the letter)\na) Water\nb) Gravity\nc) Sound\nd) Wind\n>>") 

if q1 == "b":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif q1 == "a" or q1 == "c" or q1 == "d":
    print("Incorrct")

q2 = input("Question 2: What is the name of the main antagonist?\na) Akaza\nb) Nezuko\nc) Muzan\nd) Michael Jackson\n>>") 

if  q2 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q3 = input("Question 3: What is the name of the yellow-haired boy?\na) Tanjiro\nb) Nezuko\nc) Inosuke\nd) Zenistu\n>>")  

if  q3 == "d":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q4 = input("Question 4: What breathing form does Rengoku use?\na) Water\nb) Earth\nc) Fire\nd) Air\n>>")

if  q4 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q5 = input("Question 5: What do demons have?\na) Regeneration\nb) Fire Resistance\nc) Love\nd) Nothing\n>>")

if  q5 == "a" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q6 = input ("Question 6: Who is the most powerful Demon slayer?\na) Tanjiro\nb) Muzan\nc) Gyomei\nd) Yorrichi\n>>")  

if  q6 == "d" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q7 = input("Question 7: Which is the most powerful Hashira?\na) Shinobu\nb) Gyomei\nc) Rengoku\nd) Giyu\n>>")
if  q7 == "b" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q8 = input("Question 8: What year was the Demon slayer movie released in?\na) 2018\nb) 2019\nc) 2020\nd) 2021\n>>")  

if q8 == "2020" or q8 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q9 = input("Question 9: Which of these is the most powerful demon?\na) Kokushibo\nb) Akaza\nc) Douma\nd) Daki\n>>")

if  q9 == "a" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q10 = input("Question 10: What are demons scared of?\na) Homework\nb) Grass\nc) Wifi\nd) Sunlight\n>>")

if  q10 == "d" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q11 = input("Question 11: Do demons talk?\na) Yes\nb) No\nc) Spanish\nd) Ancient Demonic Language\n>>")  

if  q11 == "a" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

q12 = input("Final question: How many Wives does Tengan Uzui have?\na) 1\nb) 2\nc) 3\nd) 4\n>>") 

if q12 == "1" or "a":
    score += 1
    print("Correct\nTotal Score: " + str(score))
elif:
    print("Incorrect")

# Finalise score
if str(score) == "12":
    print("You are Amazing, You really know your things")

elif score >= 7 and score < 12:
    print("You did well, Hopefully you get a perfect score next time")

else:
    print("Good Try, Hopefully you do better next time")
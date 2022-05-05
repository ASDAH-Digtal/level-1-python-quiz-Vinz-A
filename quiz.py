from tkinter.messagebox import YES


print("This quiz is about Demon Slayer this is multiple choice. Choose one of the options and you will get points if you are correct. Then we will start the quiz, Are You ready?")

ready = input("\na) Yes\nb) No\n>>")

if ready == "Yes" or ready == "a" or ready == "yes":
    print("Good, Lets start")
elif ready == "No" or ready == "b" or ready == "no":
    print("Too bad, Lets start")
else:
    print("I will take that as a yes")

score = 0 
q1 = input("Question 1: Which of these is NOT one of the breathing forms?\na) Water\nb) Gravity\nc) Sound\nd) Wind\n>>") 

if q1 == "Gravity" or q1 == "b" or q1 == "gravity":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrct")

q2 = input("Question 2: What is the name of the main antagonist?\na) Akaza\nb) Nezuko\nc) Muzan\nd) Michael Jackson\n>>") 

if q2  == "Muzan" or q2 == "c" or q2 == "muzan":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q3 = input("Question 3: What is the name of the yellow-haired boy?\na) Tanjiro\nb) Nezuko\nc) Inosuke\nd) Zenistu\n>>")  

if q3 == "Zenistu" or q3 =="d" or q3 == "zenistu":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q4 = input("Question 4: What breathing form does Rengoku use?\na) Water\nb) Earth\nc) Fire\nd) Air\n>>")

if q4 == "Fire" or q4 == "c" or q4 == "fire":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q5 = input("Question 5: What do demons have?\na) Regeneration\nb) Fire Resistance\nc) Love\nd) Nothing\n>>")

if q5 == "Regeneration" or q5 == "a" or q5 == "regeneration":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q6 = input ("Question 6: Who is the most powerful Demon slayer?\na) Tanjiro\nb) Muzan\nc) Gyomei\nd) Yorrichi\n>>")  

if q6 == "Yorrichi" or q6 == "d" or q6 == "yorrichi":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q7 = input("Question 7: Which is the most powerful Hashira?\na) Shinobu\nb) Gyomei\nc) Rengoku\nd) Giyu\n>>")
if q7 == "Gyomei" or q7 == "b" or q7 == "gyomei":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q8 = input("Question 8: What year was the Demon slayer movie released in?\na) 2018\nb) 2019\nc) 2020\nd) 2021\n>>")  

if q8 == "2020" or q8 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q9 = input("Question 9: Which of these is the most powerful demon?\na) Kokushibo\nb) Akaza\nc) Douma\nd) Daki\n>>")

if q9 == "Kokushibo" or q9 == "a" or q9 == "kokushibo":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q10 = input("Question 10: What are demons scared of?\na) Homework\nb) Grass\nc) Wifi\nd) Sunlight\n>>")

if q10 == "Sunlight" or q10 == "d" or q10 == "sunlight":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q11 = input("Question 11: Do demons talk?\na) Yes\nb) No\nc) Spanish\nd) Ancient Demonic Language\n>>")  

if q11 == "Yes" or q11 == "a" or q11 == "yes":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

q12 = input("Final question: How many Wives does Tengan Uzui have?\na) 1\nb) 2\nc) 3\nd) 4\n>>") 

if q12 == "1" or "a":
    score += 1
    print("Correct\nTotal Score: " + str(score))
else:
    print("Incorrect")

if str(score) == "12":
    print("You are Amazing, You really know your things")

elif score >= 7 and score < 12:
    print("You did well, Hopefully you get a perfect score next time")

else:
    print("Good Try, Hopefully you do better next time")
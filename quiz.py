from tkinter.messagebox import YES

# Introduction
print("This quiz is about Demon Slayer this is multiple choice. Choose one of the options and you will get points if you are correct. Then we will start the quiz")

# Are you ready question
ready = input("Are you ready? (By the way just ONLY put the letter in lowercase. E.g 'a')\na) Yes\nb) No\n>>")
if ready == "a":
    print("Good, Lets start")
elif ready == "b":
    print("Too bad, Lets start")
else:
    print("I will take that as a yes")

score = 0 

# Questions 1-12
continuing = True
while(continuing):
 q1 = input("Question 1: Which of these is NOT one of the breathing forms? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Water\nb) Gravity\nc) Sound\nd) Wind\n>>") 

 if q1 == "b":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
 elif q1 == "a" or q1 == "c" or q1 == "d":
    print("Incorrect")
    continuing = False
 else:
    print("Invaid answer, try again")

continuing = True
while(continuing):
    
 q2 = input("Question 2: What is the name of the main antagonist? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Akaza\nb) Nezuko\nc) Muzan\nd) Michael Jackson\n>>") 

if  q2 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q2 == "a" or q2 == "b" or q2 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q3 = input("Question 3: What is the name of the yellow-haired boy? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Tanjiro\nb) Nezuko\nc) Inosuke\nd) Zenistu\n>>")  
continuing = True
while(continuing):

if  q3 == "d":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q3 == "a" or q3 == "b" or q3 == "c":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q4 = input("Question 4: What breathing form does Rengoku use? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Water\nb) Earth\nc) Fire\nd) Air\n>>")
continuing = True
while(continuing):

if  q4 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q4 == "a" or q4 == "b" or q4 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q5 = input("Question 5: What do demons have? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Regeneration\nb) Fire Resistance\nc) Love\nd) Nothing\n>>")
continuing = True
while(continuing):

if  q5 == "a":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q5 == "b" or q5 =="c" or q5 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q6 = input ("Question 6: Who is the most powerful Demon slayer? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Tanjiro\nb) Muzan\nc) Gyomei\nd) Yorrichi\n>>")  
continuing = True
while(continuing):

if  q6 == "d":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q6 == "a" or q6 == "b" or q6 == "c":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q7 = input("Question 7: Which is the most powerful Hashira? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Shinobu\nb) Gyomei\nc) Rengoku\nd) Giyu\n>>")
continuing = True
while(continuing):

if  q7 == "b":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q7 == "a" or q7 == "c" or q7 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q8 = input("Question 8: What year was the Demon slayer movie released in? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) 2018\nb) 2019\nc) 2020\nd) 2021\n>>")  
continuing = True
while(continuing):

if q8 == "c":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q8 == "a" or q8 == "b" or q8 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q9 = input("Question 9: Which of these is the most powerful demon? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Kokushibo\nb) Akaza\nc) Douma\nd) Daki\n>>")
continuing = True
while(continuing):

if  q9 == "a":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q9 == "b" or q9 == "c" or q9 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q10 = input("Question 10: What are demons scared of? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Homework\nb) Grass\nc) Wifi\nd) Sunlight\n>>")
continuing = True
while(continuing):

if  q10 == "d":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q10 == "a" or q10 == "b" or q10 == "c":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q11 = input("Question 11: Do demons talk? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) Yes\nb) No\nc) Spanish\nd) Ancient Demonic Language\n>>")  
continuing = True
while(continuing):

if  q11 == "a" :
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q11 == "b" or q11 == "c" or q11 =="d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

q12 = input("Final question: How many Wives does Tengan Uzui have? (By the way just put ONLY the letter in lowercase. E.g 'a')\na) 1\nb) 2\nc) 3\nd) 4\n>>") 
continuing = True
while(continuing):

if q12 == "a":
    score += 1
    print("Correct\nTotal Score: " + str(score))
    continuing = False
elif q12 == "b" or q12 == "c" or q12 == "d":
    print("Incorrect")
    continuing = False
else:
    print("Invaid answer, try again")

# Finalise score
if str(score) == "12":
    print("Total: {}/12, You are Amazing, You really know your things".format(str(score)))

elif score >= 7 and score < 12:
    print("Total: {}/12, You did well, Hopefully you get a perfect score next time".format(str(score)))

else:
    print("Total: {}/12, Good Try, Hopefully you do better next time".format(str(score)))
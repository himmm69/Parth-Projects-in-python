import random 
import sys
from Question_bank import Question_bank

def player(name):
   
    print(f"Hello Student {name}, Welcome to Tokyo Koudo Ikusei Senior High School.")
     
    print("Before we start, I will have to ask what your age is.")
    print()# This adds a blank line
    age = int(input("Enter your age: "))
    sections = ['A', 'B', 'C', 'D']
    sections = random.choice(sections)
   
    if age < 15:
        year = "Your too young for this school kid , go play roblox"
        Class = "nuh uh"
        print(f" {name}. As you are {age} years old. {year}")
        sys.exit()

    elif age <= 15:
        year = "Freshman"
        Class = F"1-{sections}"

    elif age <= 17:
        year = "Junior"
        Class = F"2-{sections}"

    elif age <= 20:
        year = "Senior"
        Class = F"3-{sections}"
    else:
        year = "You are too old for this school , put the fries in the bag"
        Class = "N/A"
        print(f" {name}. As you are {age} years old. {year}")
        sys.exit()

    print(f"Thank you, {name}. As you are  {age} years old. You will be a {year} and will be in {Class}. Enjoy your stay here.")
    print()






def subjects(name):

   print(f" Dear {name} Choose the subjects you wish to study, you have to choose a total of 4 subjects with 1 from each category") 
   print()
  
   Category1 = ['Maths', 'Art', 'Sports','Music']
   Category2 = ['Computer Science','Biology', 'Physics','home science']
   Category3 = ['English', 'Japanese', 'French', 'Spanish']
   Category4 = ['History', 'Geography', 'Philosophy', 'Psychology',]


 
   print(f"caterogy1: {Category1}")
   sub1 = input("The subject you have chosen from category 1 is : ")
   print()

   print(f"caterogy2: {Category2}")    
   sub2 =input("The subject you have chosen from category 2 is : ")
   print()
   
   print(f"caterogy3: {Category3}")
   sub3 = input("The subject you have chosen from category 3 is : ")
   print()

   print(f"caterogy4: {Category4}")
   sub4 = input("The subject you have chosen from category 4 is : ")
   print()

   print(f"Thank you {name}, You have chosen the following subjects : {sub1}, {sub2}, {sub3}, {sub4}")
   print()


   email = f"{name.upper()}@tokyokoudoikusei.edu"

   print(f"Dear {name}, We will shortly send you your timetable with the sibjects you have chosen in you schoolemail {email}")
   print()
   return sub1, sub2, sub3, sub4
 


def timetable(name,sub1, sub2, sub3, sub4):
   
   days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
   subjects = [sub1, sub2, sub3, sub4]
   print(f"{name}, your timetable is as follows:")
   for day, subject in zip(days, subjects):
       print(f"{day}: {subject}")

  
  
username = input("Enter your name: ")
player(username)
sub1, sub2, sub3, sub4 = subjects(username)
timetable(username, sub1, sub2, sub3, sub4)

def quiz(Username, question_bank, subjects):

  days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
  score = 0
  answer_log = {}
  for day, subject in zip(days, subjects):
      print(f"\n{day}: {subject}")
      answer_log[day] = []
      questions = question_bank.get(subject, [])
      for q in questions:
        print(q["Q"])
        for option in q["options"]:
          print(option)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        
        # Easter egg check
        if subject.strip().lower() == "philosophy" and q["Q"].startswith('who said the famous saying of "I think therefore I am"') and user_ans == "D":
          print("Easter Egg Found! +5 points for choosing Parth Gandhi 😄")
          score += 5

        correct = user_ans == q["Ans"]
        answer_log[day].append({
          "question": q["Q"],
          "your_answer": user_ans,
          "correct_answer": q["Ans"],
          "is_correct": correct
        })
        if correct:
          print("Correct!\n")
          score += 1
        else:
          print(f"Incorrect! The correct answer was {q['Ans']}.\n")
  print(f"\n{Username}, your total score is: {score}")

chosen_subjects = [sub1, sub2, sub3, sub4]
quiz(username, Question_bank, chosen_subjects)


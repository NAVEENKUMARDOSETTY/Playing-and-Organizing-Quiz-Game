import random
print("\n _ _ _ Quiz Game Organized by Globel Tech _ _ _ ")
name = input("\nEnter Your Name : ")
print(f"\nWelcome to the Quiz game {name} ..!!")
questions = ["Expand Pdf", "How Many Oceans are There (word)", "Expand DNA"]
answers = ["portable document file", "Five" ,"Deoxyribo Neuclic Acid"]
score = 0
option = input("\nEnter 'O' if you are an Organiser to add questions inthe quiz game, else press any other alphabet in the keyboard : ")
if option == "O" or option == "o":
	num = int(input("\nEnter The number of questions that you would like to Add : "))
	for i in range(1,num+1):
		que = input(f"Enter your Question {i} :")
		questions.append(que)
		ans = input(f"Enter answer for your question {i} :")
		answers.append(ans)
else: 
	print("You haven't opt to oraganise the quiz, possibly you are a player")
option = input("\nEnter 'P' if you are a player to answer questions in the quiz game : ")
if option == "P" or option == "p":
	print("\nPlease answer the following questions :\n")
	length = len(questions)
	temp = list(range(length))
	for j in range(length):
		n = random.choice(temp)
		temp.remove(n)
		sol = input(f"{questions[n]} : ").lower()
		if sol == answers[n].lower():
			print("Answered Correctly..!!\n")
			score += 1
		else:
			print("Wrong Answer..!!\n")
			continue
	print("\nQuiz is Completed..")
	print(f"\nYour have answered {score} questions correctly " )
	percentage = ((score/length)*100)
	print(f"\nYou have Successfully played the quiz game and secure a score of {percentage} \n\nplay the game again for more Fun and Knowledge..!!")
else:
	print("\nYou have choosen a wrong option, please choose either  'O' or 'P' and Restart the game ") 






		



#Python Quiz Game
questions=(" How many continents are there on Earth?: ",
           " How many elements are there in the periodic table?: ",  
           " Which planet is known as the Red Planet?: ",
           " What is the largest mammal in the world?: ",
           " What is the capital of France?: ")
options=((" A. 5"," B. 6"," C. 7"," D. 8"),
         (" A. 108"," B. 118"," C. 128"," D. 138"),
         (" A. Earth"," B. Mars"," C. Jupiter"," D. Saturn"),
         (" A. Elephant"," B. Blue Whale"," C. Giraffe"," D. Great White Shark"),
         (" A. Berlin"," B. Madrid"," C. Paris"," D. Rome"))

answers=("C","B","B","B","C")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is: {answers[question_num]}")
    question_num+=1

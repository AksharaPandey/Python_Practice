# while loop= a control flow statement that allows code to be executed repeatedly based on a given boolean condition.
# The while loop can be thought of as a repeating if statement.


name=input("Enter your name: ").strip()
"""if name=="":
    print("You didn't enter a name.")
else:
    print(f"Hello, {name}!")"""
while name=="":
    print("You didn't enter a name.")
    name=input("Enter your name: ").strip()
print(f"Hello, {name}!")
#The above code can be read as:
# while the name is empty
#     print a message
#     ask for the name again
# print a greeting message
#This loop will continue until the user enters a non-empty name.
#Note: Be careful with while loops, as they can create infinite loops if the condition is never met.


age=int(input("Enter your age: ").strip())
while age<0:
    print("Age cannot be negative.")
    age=int(input("Enter your age: ").strip())

print(f"You are {age} years old.")

food=input("Enter your favorite food: ").strip().lower()
while food not in ["pizza", "burger", "pasta", "sushi"]:
    print("We only have pizza, burger, pasta, and sushi.")
    food=input("Enter your favorite food: ").strip().lower()
print(f"You like {food}.")


num=input("Enter a number between 1 and 10: ").strip()
while num<1 or num>10 or not num.isdigit():
    print("Invalid input. Please enter a number between 1 and 10.")
    num=input("Enter a number between 1 and 10: ").strip()
num=int(num)
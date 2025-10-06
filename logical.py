#Logical Operator: Used on the conditional statements
# and= both conditions must be true
# or= at least one condition must be true
# not= reverses the logical state of its operand,true if condition is false


#and operator
temp=float(input("Enter the temperature in Fahrenheit: "))
if temp>32 and temp<212:
    print("The temperature is in the liquid state.")
else:
    print("The temperature is not in the liquid state.")

#or operator
day=input("Enter the day of the week: ").lower().strip()
if day=="saturday" or day=="sunday":
    print("It's a weekend!")
else:
    print("It's a weekday.")

#not operator
is_raining=input("Is it raining? (yes/no): ").lower().strip()
if not is_raining=="yes":
    print("You can go for a walk.")
else:
    print("Better to stay indoors.")

#Combined logical operators
age=int(input("Enter your age: "))
has_id=input("Do you have an ID? (yes/no): ").lower().strip()
if age>=18 and has_id=="yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

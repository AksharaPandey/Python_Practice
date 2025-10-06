#conditionalal statements
# if, elif, else
#A one line shortcut for if-else statement is called ternary operator
#print or assign a value based on a condition in a single line

num=float(input("Enter a number: "))
print("Positive") if num>=0 else print("Negative")
#The above line is equivalent to:
if num>=0:
    print("Positive")
else:
    print("Negative")


num1=float(input("Enter first number: "))
result="Even" if num1%2==0 else "Odd"
print(result)
#The above line is equivalent to:
if num1%2==0:
    result="Even"
else:    
    result="Odd"


user_role=input("Enter your role (admin/user): ").lower().strip()
access_level="Full Access" if user_role=="admin" else "Limited Access"
print(access_level)
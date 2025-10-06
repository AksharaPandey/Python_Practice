#Simple python calculator
operator=input("Enter operator (+, -, *, /): ")
#When we take any input from user it is considered as string
#therefore it is important to covert the numbers into float or string
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

if operator== "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator== "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator== "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator== "/":
    if num2!=0:
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")

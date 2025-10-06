#Python is a dynamically typed language
#Variables do not need explicit declaration to reserve memory space
#The declaration happens automatically when you assign a value to a variable
#The equal sign (=) is used to assign values to variables
#A variable can hold different data types
#Variable names can contain letters, digits, and underscores but cannot start with a digit
#Variable names are case-sensitive
#Python supports multiple data types including:
#1. Integer (int)
#2. Floating point (float)
#3. String (str)
#4. Boolean (bool)
#5. Complex (complex)
#6. List (list)
#7. Tuple (tuple)
#8. Dictionary (dict)
#9. Set (set)
#10. NoneType (None)
#Examples of variable declarations and assignments

name="Akshara"
age=22
height=5.5
is_student=True
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Data type of name:", type(name))
print(f"Your name is {name} and your age is {age}")


marks=95.5
print("Marks:", marks)
print("Data type of marks:", type(marks))

#integer
num1=10
num2=20
exp1=eval("10+20")
print("Sum:", num1+num2)

#string
str1="Hello"
str2="World"
print("Concatenated String:", str1 + " " + str2)
print("Repeating string:", (str1+" "+str2)*3)

#boolean
"""booleans works internally in the compiler as 1 and 0"""
is_raining=True
is_sunny=False
print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)

#float
pi=3.14159
radius=5.0
area=pi*radius*radius
print("Area of circle:", area)
print("Data type of area:", type(area))

#complex
comp1=2+3j
comp2=1+4j
comp_sum=comp1+comp2
print("Sum of complex numbers:", comp_sum)
print("Real part:", comp_sum.real)
print("Imaginary part:", comp_sum.imag)

#if else
num=15
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")

#Typecasting: The process of converting one data type to another
"""Explicitely and Implicitely"""
#Implicit typecasting: The compiler automatically converts one data type to another without any user intervention.
name="Akshara"
age=22
gpa=3.8
student=True

a=type(name)
b=type(age)
c=type(gpa)
d=type(student)
print(a)
print(b)   
print(c)
print(d)
print("**********")
age_as_float=age+0.0
print("Age as float:", age_as_float)
age=float(age)
print("Age after implicit typecasting:", age)
print("Data type of age after implicit typecasting:", type(age))
print("**********")

#Explicit typecasting: The user manually converts one data type to another using built-in functions.
gpa=3.8
gpa=int(gpa)
print("GPA after explicit typecasting:", gpa)
print("Data type of GPA after explicit typecasting:", type(gpa))

student=True
student=str(student)
print("Student after explicit typecasting:", student)
print("Data type of student after explicit typecasting:", type(student))


#if a number is conerted into boolean then as long as it is not 0 it is true
num=10
num=bool(num)
print(num)

num1=0
num1=bool(num1)
print(num1)
#similarly for string if it is empty it is false otherwise true
str1="Bob"
str2=""
str1=bool(str1)
str2=bool(str2)
print(str1)
print(str2)
print("**********")
#How would entering a string as boolean is useful?
#For example in a web form if a user enters something in a text box it is considered true otherwise false
user1_input="Hello"
user2_input=""
user1_input=bool(user1_input)
user2_input=bool(user2_input)
print(user1_input)
print("text box is filled")
print(user2_input)
print("text box is empty")
print("**********")

#Explicit typecasting: It is done using built-in functions like int(), float(), str(), bool(), complex()
#It is done by the user
num_str="100"
num=int(num_str)
print("Number after explicit typecasting:", num)
print("Data type of number after explicit typecasting:", type(num))


x=2
y=3.5
x=x/y
print(x)
print(type(x))


#User Inputs
#The input() function is used to take input from the user
name=input("Enter your name: ")
print("Hello, " + name + "!")
age=int(input("Enter your age: "))
age=age+1
print("Next year, you will be " + str(age) + " years old.")
print("*********")


#Note: The input() function always returns a string. If you need a different data type, you must explicitly convert it using typecasting.


#BMI Calculator
print("BMI Calculator")
height=float(input("Enter your height in feet: "))
print("Your height is " + str(height) + " feet.")
weight=float(input("Enter your weight in kg: "))
bmi=weight/(height*height)
print("Your BMI is " + str(bmi))
#BMI Categories:
#Underweight = <18.5
#Normal weight = 18.5–24.9 
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater
if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("You have a normal weight")
elif bmi>=25 and bmi<=29.9:
    print("You are overweight")
else:
    print("You are obese")

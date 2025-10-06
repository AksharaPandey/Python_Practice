#if : do some code if only the condition is true
#else : do some code if and only if the condition is false

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Nested if
marks=int(input("Enter your marks: "))
if marks>=90:
    print("You got A grade.")
else:
    if marks>=80:
        print("You got B grade.")
    else:
        if marks>=70:
            print("You got C grade.")
        else:
            if marks>=60:
                print("You got D grade.")
            else:
                print("You got F grade.")
#Better way to write nested if
#elif : else if : do some code if and only if the condition is true
marks=int(input("Enter your marks: "))
if marks>=90:
    print("You got A grade.")
elif marks>=80:
    print("You got B grade.")
elif marks>=70:
    print("You got C grade.")
elif marks>=60:
    print("You got D grade.")
else:
    print("You got F grade.")

print("**********")

response=input("Do you want to continue? (yes/no): ")
if response=="yes":
    print("You chose to continue.")
elif response=="no":
    print("You chose to exit.")
else:
    print("Invalid input. Please enter yes or no.")

print("**********")

#lower() : converts a string to lowercase
#upper() : converts a string to uppercase
#strip() : removes leading and trailing whitespace from a string

name=input("Enter your name: ")
if name=="":
    print("You did not enter your name.")
else:
    print(f"Hello, {name.capitalize()}!")


for_sale= True
if for_sale:
    print("The item is for sale.")
else:    
    print("The item is not for sale.")
price=100
if for_sale and price>0:
    print("The item is for sale and has a valid price.")
else:
    print("The item is either not for sale or does not have a valid price.")

#Python weight converter
#In kilograms or lbs

weight=float(input("Enter your weight: "))
unit=input("Enter the unit (kg/lbs): ").lower().strip()

#lower() : converts a string to lowercase
#strip() : removes leading and trailing whitespace from a string
if unit=="kg":
    converted_weight=weight*2.20462
    print(f"Your weight is {converted_weight} lbs.")
elif unit=="lbs":
    converted_weight=weight/2.20462
    print(f"Your weight is {converted_weight} kg.")
else:
    print("Invalid unit. Please enter kg or lbs.")
#Python Temperature Converter
#In Celsius or Fahrenheit
unit=input("Enter the unit you want to convert to (C/F): ").lower().strip()
temp=float(input("Enter the temperature: "))
if unit=="c":
    converted_temp=round((temp-32)*5/9,2)
    print(f"The temperature in Celsius is {converted_temp} °C.")
elif unit=="f":
    converted_temp=round((temp*9/5)+32,2)
    print(f"The temperature in Fahrenheit is {converted_temp} °F.")
else:  
    print("Invalid unit. Please enter C or F.")
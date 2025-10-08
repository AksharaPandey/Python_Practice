#Shopping cart program
foods=[]
prices=[]
total=0
while True:
    food=input("Enter the food item you want to add to your cart (or 'done' to finish): ")
    if food.lower()=='done':
        break
    price=float(input(f"Enter the price of {food}: "))
    foods.append(food)
    prices.append(price)
    total+=price
    print(f"{food} has been added to your cart.")
    print(f"Your current total is: ${total:.2f}")
print("\nYour shopping cart:")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
print(f"Total: ${total:.2f}")
print("Thank you for shopping with us!")
#This program allows the user to add food items and their prices to a shopping cart, calculates the total cost, and displays the contents of the cart when the user is done.
#The program uses a while loop to continuously prompt the user for input until they indicate they are done by typing 'done'.
#The program uses two lists to store the food items and their prices, and a variable to keep track of the total cost.
#The program uses formatted strings to display the prices with two decimal places.
#The program uses a for loop to iterate through the lists and display the contents of the cart at the end.
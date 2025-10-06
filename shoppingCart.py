#This is a simple shopping cart program that allows users to add items to their cart and view the total cost.

item=str(input("Enter the name of the item you want to add to your cart: "))
price=float(input(f"Enter the price of {item}: "))
quantity=int(input(f"Enter the quantity of {item}: "))
total_cost=price*quantity
print(f"You have added {quantity} {item}(s) to your cart. The total cost is: ${round(total_cost,2)}")
print("Thank you for shopping with us!")
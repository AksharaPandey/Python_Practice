#2D list is a list of lists. It is also known as a matrix or a table.
#Example of a 2D list
"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]"""

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
crops= ["wheat", "rice", "corn"]

groceries=[fruits, vegetables, crops]
fruits[0]="mango"

print(groceries[0][0])  # Output: mango
print(groceries[0][1])  # Output: broccoli

for category in groceries:
    for item in category:
        print(item)
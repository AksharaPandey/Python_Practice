#nested loops: a nested loop is a loop inside another loop.
# outer loop:
#            inner loop:

for x in range(4):
    for y in range(1,10):
       print( y, end=" " )
    print()


print("-----")

for x in range(5):
    for y in range(1,10):
         print("*", end=" " )
    print()
print("-----")
for x in range(1,6):
    for y in range(x):
         print("*", end=" " )
    print()
print("-----")

rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
for x in range(rows):
    for y in range(columns):
         print("*", end=" " )
    print()

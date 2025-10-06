import math
a=input("Enter side a: ")
a=float(a)
print("side a is:", a)
b=input("Enter side b: ")
b=float(b)
print("side b is:", b)
c=math.sqrt((pow(a,2)+pow(b,2)))
print("The length of the hypotenuse is:",round(c,2))
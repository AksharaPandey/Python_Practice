import math
radius=input("Enter the radius of the circle: ")
radius=float(radius)
print("radius is:", radius)
circumference=2*math.pi*radius
print("The circumference of the circle is:", round(circumference,2))
#Circumference of circle = 2 * pi * radius
area=math.pi*pow(radius,2)
print("The area of the circle is:", round(area,2))
#Area of circle = pi * radius^2
diameter=2*radius
print("The diameter of the circle is:", round(diameter,2))
#Diameter of circle = 2 * radius
print("**********")
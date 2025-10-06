#Basic arithmetic operations

import math
friends=100
#friends= friends + 1
##friends+=1 #Augmented assignment
#friends= friends - 1
#friends-=1
#friends= friends * 2
#friends*=2
#friends= friends / 2
#friends/=2
#friends=friends ** 2
#friends**=2
#friends=friends // 2
#friends//=2
#friends=friends % 3
friends%=3
print(friends)
print("**********")
#Order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

#Round
x=3.14
y=2.5
z=1.5

result=x+y*z
print(round(result,2))

print("**********")

#Absolute value
x=-2
absolute=abs(x)
print(absolute)
print("**********")

#Power
result=pow(3,2) #3^2
print(result)
print("**********")

#Max and Min
x=589
y=234
z=876
maximum=max(x,y,z)
minimum=min(x,y,z)
print("Maximum is:", maximum)   
print("Minimum is:", minimum)

#import math module

print("**********")
x=math.pi
print(round(x,2))
y=math.e
print(round(y,2))
z=math.sqrt(x)
print(round(z,2))
a=math.ceil(2.3) #Round up
b=math.floor(2.7) #Round down
print(a)
print(b)

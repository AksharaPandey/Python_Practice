#for loops: a for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
# for loop= a control flow statement that allows code to be executed repeatedly based on a given boolean condition.
# The for loop can be thought of as a repeating if statement.

#for variable in range(start,stop,step)

for i in range(5):
    print(i)
#output: 0 1 2 3 4
#The range() function generates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#The range() function can take 1, 2, or 3 arguments.
#1 argument: range(stop)
#2 arguments: range(start, stop)
#3 arguments: range(start, stop, step)
#The start argument is inclusive, while the stop argument is exclusive.
#The step argument is optional and defaults to 1.

for i in range(1, 10, 2):
    print(i)
#output: 1 3 5 7 9
print("-----")

#The for loop can also be reversed
for x in reversed(range(5)):
    print(x)
print("-----")

credit_card="1234-5678-9876-5432"
for digit in credit_card:
    if digit=="-":
        continue
    print(digit)

#output: 1234567898765432
print("-----")
#The continue statement is used to skip the current iteration of a loop and move to the next iteration.
for x in range(1,22):
    if x==13:
        continue
    else:
        print(x)

print("-----")

#break statement is used to exit a loop prematurely when a certain condition is met.
for x in range(1,22):
    if x==13:
        break
    else:
        print(x)    
#simple countdown timer

import time #import the time module

my_time = int(input("Enter the time in seconds: ")) #get user input for the countdown time in seconds

for x in range(my_time, 0, -1): #create a for loop that counts down from the user input to 1
    seconds=x % 60  #calculate the number of seconds
    minutes=(x // 60) % 60  #calculate the number of minutes
    hours=(x // 3600) % 24  #calculate the number of hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #print the current value of x
    time.sleep(1)  #pause the program for 1 second
#time.sleep(3)  #pause the program for a specified number of seconds
#here, the program will pause for 3 seconds before starting the countdown.

print("Time's up!") #print a message when the countdown is over

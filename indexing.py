#indexing: accessing element of a sequence using[] indexing operator
# [start : end : step]
# start: starting index (inclusive) 
#inclusive: including the start index
# end: ending index (exclusive)
# exclusive: excluding the end index
# step: step size (default is 1)
name="akshat dubey"
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
#-1 will give the last character
print(f"First 5 characters: {name[0:5]}")
print(f"Characters from index 3 to 8: {name[3:9]}")
print(f"Characters from index 3 to end: {name[3:]}")
print(f"Characters from start to index 5: {name[:6]}")
print(f"Every second character: {name[::2]}") #step size of 2
print(f"Reversed name: {name[::-1]}") #step size of -1 (reverses the string)

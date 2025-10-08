#collection= single 'variable' used to store multiple values
#list= collection of values that are ordered and changeable, allows duplicate members
#tuple= collection of values that are ordered and unchangeable, allows duplicate members
#set= collection of values that are unordered and unindexed, no duplicate members
#dictionary= collection of key-value pairs that are unordered, changeable, and indexed, no duplicate members
#Python Data Structures

#List
#fruits=["apple", "banana", "cherry"] #create a list of fruits
#print(fruits) #print the list of fruits
#to access a specific item in the list, use its index number
#print(fruits[::2]) #print the second item in the list

#for x in fruits: #loop through the list and print each item
   # print(x)
#print(fruits) #print the updated list
#print(dir(fruits)) #print the list of available methods for the list object
#print(help(fruits.append)) #print the help documentation for the append method

#print(len(fruits)) #print the number of items in the list
#fruits.remove("banana") #remove an item from the list
#print(fruits) #print the updated list
#fruits.pop() #remove the last item from the list
#print(fruits) #print the updated list
#fruits.clear() #remove all items from the list
#print(fruits) #print the updated list
#fruits=["apple", "banana", "cherry"] #recreate the list of fruits

#sets
fruits={"apple", "banana", "cherry"} #create a set of fruits
print(fruits) #print the set of fruits
fruits.add("orange") #add an item to the set
print(fruits) #print the updated set
#print(fruits[1]) #this will cause an error because sets are unordered and do not support indexing
fruits.remove("banana") #remove an item from the set

#tuples
fruits=("apple", "banana", "cherry") #create a tupleof fruits
print(fruits) #print the tuple of fruits
print(fruits[1]) #print the second item in the tuple
#fruits[1]="orange" #this will cause an error because tuples are immutable and do not support item assignment
print(fruits) #print the tuple of fruits
#fruits=("apple", "banana", "cherry", "orange") #this will cause an error because tuples are immutable and do not support item assignment
print(fruits) #print the tuple of fruits
print(len(fruits)) #print the number of items in the tuple
#fruits=("apple", "banana", "cherry") #recreate the tuple of fruits


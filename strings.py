#Useful string methods
#len() : returns the length of a string
#capitalize() : capitalizes the first letter of a string
#title() : capitalizes the first letter of each word in a string
#lower() : converts a string to lowercase
#upper() : converts a string to uppercase
#strip() : removes leading and trailing whitespace from a string
#replace() : replaces a substring with another substring
#find() : returns the index of the first occurrence of a substring
#index() : returns the index of the first occurrence of a substring (raises an error if not found)
#count() : returns the number of occurrences of a substring
#split() : splits a string into a list of substrings based on a delimiter
#join() : joins a list of strings into a single string with a delimiter

#Example usage of string methods
name="akshat dubey"
print(f"Length of your name: {len(name)}")
print(f"Capitalized name: {name.capitalize()}")
print(f"Title case name: {name.title()}")
print(f"Lowercase name: {name.lower()}")
print(f"Uppercase name: {name.upper()}")
print(f"Name with no leading or trailing spaces: '{name.strip()}'")
print(f"Name with replaced spaces: '{name.replace(' ', '_')}'")
print(f"Index of first occurrence of 'a': {name.find('a')}")
print(f"Index of first occurrence of 'z': {name.find('z')}") #returns -1 if not found
print(f"Index of first occurrence of 'd': {name.index('d')}")
print(f"Count of 'a' in name: {name.count('a')}")
print(f"Splitting name by space: {name.split(' ')}")
words=["Hello", "world", "from", "Python"]
print(f"Joining words with space: {' '.join(words)}")
#f-strings : formatted string literals
age=20
print(f"Hello, {name.title()}! You are {age} years old.")
#The above line is equivalent to:
print("Hello, {}! You are {} years old.".format(name.title(), age))
print("Hello, %s! You are %d years old." % (name.title(), age))

#isalpha() : returns True if all characters in the string are alphabetic
#isdigit() : returns True if all characters in the string are digits
#isalnum() : returns True if all characters in the string are alphanumeric
#isspace() : returns True if all characters in the string are whitespace
test_str1="HelloWorld"
test_str2="Hello123"
test_str3="Hello 123"
test_str4="   "
test_str5="12345"
print(f"Is '{test_str1}' alphabetic? {test_str1.isalpha()}")
print(f"Is '{test_str2}' alphanumeric? {test_str2.isalnum()}")
print(f"Is '{test_str3}' alphanumeric? {test_str3.isalnum()}")
print(f"Is '{test_str4}' whitespace? {test_str4.isspace()}")
print(f"Is '{test_str5}' digit? {test_str5.isdigit()}")
print(f"Is '{test_str1}' digit? {test_str1.isdigit()}")
print(f"Is '{test_str1}' lowercase? {test_str1.islower()}")

print("**********")

#validate user input for a username
# 1. Username must be no more than 12 charecters long
# 2. Username must not contain any spaces
# 3. Username must not contain any digits
username=input("Enter a username: ").strip()
if len(username)>12:
    print("Username must be no more than 12 characters long.")
elif " " in username:
    print("Username must not contain any spaces.")
elif any(char.isdigit() for char in username):
    print("Username must not contain any digits.")
else:
    print(f"Username '{username}' is valid.")
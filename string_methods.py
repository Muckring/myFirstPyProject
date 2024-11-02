# In this lesson, we are gonna be looking at 
# different string methods in Python

# first_name = str(input("How long is your name?: "))
# print(len(first_name))

# .find() method (indexOf()) finds the first occurence of a character

# name = 'Kostya'
# print(name.find("a"))

# .rfind() method (lastIndexOf()) finds the last occurrence of a character

# name = "Konstan"
# print(name.rfind("n"))

# .capitalize() capitalizes the first letter of a string

# name = 'ariana'
# print(name.capitalize())

# .lower() and .upper() make all characters in a string all lower or uppercase

# name = "Elena"
# print(name.upper())
# print(name.lower())

# .isdigit() checks if a string contains only digits
# and .isalpha() checks if a string contains only alphebetical
# characters - both return true or false

# digit = "1"
# no_digit = '1a'
# print(digit.isdigit()) 
# print(no_digit.isdigit())

# abc = 'abc'
# no_abc = 'ab1'
# print(abc.isalpha())
# print(no_abc.isalpha())

#.count() calculates how many times a character repeats in a string
# doc_num = "124/ARB/234-094-55"
# print(doc_num.count("/"))
# print(doc_num.count('-'))

# .replace() method allows you to replace one character with another
# phone = '234-555-444-66'
# print(phone.replace('-', '    '))

print(help(str))


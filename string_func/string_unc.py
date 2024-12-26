
first_name ="Mina Maher MOSadef"
second_name ="Astifanous Shenouda Elmaraghy"
digit_str = "1234566788"
empty_string =""
#string built-in functions.
#len lenght function 
print("lenght of first_name is",len(first_name))
print("lenght of empty string is" ,len(empty_string))

#check string 
if "Maher" in first_name :
    print(True)
#loop string 
for char in first_name :
    print(char)

#check is not string 
if "maher" not in first_name :
    print(True)

#  ************************ Modify Function of string *************************
#  upper function
print(first_name)
print("upper case of first name is",first_name.upper() )
print(first_name)

# Lower Case Function 
print(first_name)
print("lower case of first name is",first_name.lower() )

# ************************** nonplace function ******************
"""
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The strip() method removes any whitespace from the beginning or the end:
"""
white_string ="  mina maher  "

print(f"white_string after Remove Whitespace :{white_string.strip()}" )

"""
    Replace String
Example
The replace() method replaces a string with another string:
"" is act each character not space 
" " is space character 
"""
print(white_string)
print("white after replace "" with - is : " ,white_string.replace(" " ,"-"))

"""
    Split String
The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:
"""
list = first_name.split(" ")
print(first_name)
print("List of first name after split : ",list)

"""
    ************************ Python - Format - Strings ***************************
    String Format
    f formate 
    As we learned in the Python Variables chapter, we cannot combine strings and numbers
"""
age = 36
txt = "my name is {} my age is {}".format(first_name ,age)
print(txt)
print("by using f formate")
print(f"my name is {first_name} , age is {age}")

"""
    *************            ***  Escape Character ***************** ******
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash  followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example Get your own Python Server
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

      txt = We are the so-called Vikings from the north.

"""
txt = "We are the so-called \"Vikings\" from the north." 
print("double quotes inside double quotes " ,txt)

""" 
    ************************* String Methods *****************
    Python has a set of built-in methods that you can use on strings.

    Method	Description
capitalize()	Converts the first character to upper case (nonplace)
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginningMethod	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
full_name ="mINA Saher!"
print(full_name)
print(full_name.capitalize())
print(full_name)
print(full_name)
print(full_name.casefold())
print(full_name)
"""
ExampleGet your own Python Server
Replace any "S" characters with a "P" character:

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
"""
mydict = {83:  80}
print(full_name.translate(mydict))
print(full_name)

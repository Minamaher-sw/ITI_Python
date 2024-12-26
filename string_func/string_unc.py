
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

""""
    *************            ***  Escape Character ***************** ******
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example Get your own Python Server
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

      txt = "We are the so-called "Vikings" from the north."

      To fix this problem, use the escape character \":

    \'	    Single Quote	
    \\	    Backslash	
    \n	    New Line	
    \r	    Carriage Return	
    \t	    Tab	
    \b	    Backspace	
    \f	    Form Feed	
    \ooo	Octal value	
    \xhh	Hex value
"""
txt = "We are the so-called \"Vikings\" from the north." 
print("double quotes inside double quotes " ,txt)
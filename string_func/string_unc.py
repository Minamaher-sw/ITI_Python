
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


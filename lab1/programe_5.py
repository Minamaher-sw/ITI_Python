
"""
    function which has an input of a string from user then it will 
return the same string reversed
"""
input_string =input("Enter String")

def reverse_string(input_string):
    input_string = input_string[::-1]
    return input_string

reverse_string_ret =reverse_string(input_string)
print(f"Reverse of sting {input_string} is {reverse_string_ret}")
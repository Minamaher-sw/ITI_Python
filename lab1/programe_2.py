
"""
    function that accepts two arguments (length, start) to generate 
an array of a specific length filled with integer numbers increased by one 
from start.
"""
gen_array =[]
def generate_array (array_lenght,array_start):
    for index in range(array_lenght):
        gen_array.append(array_start)
        array_start +=1 
array_lenght= int(input("Enter lenght of array "))
array_start = int(input("Enter Start of array "))
generate_array(array_lenght ,array_start)
print("array is" , gen_array)
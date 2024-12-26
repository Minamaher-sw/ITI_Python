"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
"""
"""
    *******************  List Length **************
To determine how many items a list has, use the len() function:
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
    List Items - Data Types
List items can be of any data type:

Example
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""

"""
    type() function 
    From Python's perspective, lists are defined as objects with the data type 'list':
"""
print(type(thislist))

"""
    The list() Constructor
    It is also possible to use the list() constructor when creating a new list.     
"""
thislist = list(('apple' , 'orange' ,22))
print(thislist)

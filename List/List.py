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

"""
    Negative Indexing
    Negative indexing means start from the end

    -1 refers to the last item, -2 refers to the second last item etc.
"""
new_list =thislist[-1]
print(new_list)

"""
    Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.just copy
"""
new_list_2 =thislist[0:2]
print(new_list_2)
new_list_2 =thislist[:2]
print(new_list_2)
new_list_2 =thislist[0:]
print(new_list_2)
new_list_2 =thislist[:]
print(new_list_2)

"""
    Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:
"""
#reverse
new_list_2 =thislist[-1::-1]
print(new_list_2)

new_list_2 =thislist[-1:-4:-1]
print(new_list_2)
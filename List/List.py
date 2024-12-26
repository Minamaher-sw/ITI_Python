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

"""
    Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:
"""
if 'apple' in thislist :
    print("it is found ")
"""
    Change Item Value
To change the value of a specific item, refer to the index number:
"""
thislist[0]= "banana"
print(thislist)
"""
    Change a Range of Item Values
"""
thislist[0:2] =["mina " , "maher"]
print(thislist)
# note 
"""
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second value by replacing it with two new values:
"""
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

""" 
If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:
"""
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""
   ******************  Insert function 
   pararmeter 1 :index
   pararmeter 2 : value 
   To insert a new list item, without replacing any of the existing values, we can use the insert() method.
   The insert() method inserts an item at the specified index:

"""
thislist.insert(2,"mosadef")
print(thislist)
thislist.insert(2,"Astifanous")
print(thislist)

"""
    ***************** Python - Add List Items ***********
Append Items
"""
thislist.append("full name")
print(thislist)
"""
    Extend List
    To append elements from another list to the current list, use the extend() method.

    Add Any Iterable
    The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

    Example
    Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
print(thislist ,"\n" ,tropical)
thislist.extend(tropical)
print(f"thislist after extend ffunction is {thislist} " )
# with tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
print(thislist ,"\n" ,thistuple)
thislist.extend(thistuple)
print(f"thislist after extend ffunction tuple is {thislist} " )

"""
    ******************** Python - Remove List Items ******
"""
"""
    Remove Specified Item
The remove() method removes the specified item

If there are more than one item with the specified value, the remove() method removes the first occurrence:

Example
Remove the first occurrence of "banana":
"""
print(thislist)
thislist.remove("apple")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)

"""
Remove Specified Index
The pop() method removes the specified index.
parameter 1 is index 
"""
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index: 
"""
    del :
    del thislist[0]
    The del keyword can also delete the list completely.
    del thislist
"""
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
del thislist[0]
print(thislist)
print("**************************************")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
del thislist
# error : name 'thislist' is not defined
#print(thislist)

"""
    Clear the List
    The clear() method empties the list.
"""
print("**************************************")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.clear()
print(thislist)


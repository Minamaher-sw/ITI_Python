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

"""
   ****************  Python - Loop Lists  *************
"""
print("********** Python - Loop Lists ***************\n")
thislist = ["apple", "banana", "cherry"]
for item in thislist:
    print(item)

"""
    Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
"""
print("printing from index by for loop")
for index in range(len(thislist)):
    print(thislist[index])

#using while loop
print("printing from index by while loop")
index =0 
while True :
    print(thislist[index])
    index+=1
    if(index == len(thislist)):
        break 
"""
Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

Example
A short hand for loop that will print all items in a list:

List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

"""
print("printing list byUsing List Comprehension ")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
print("printing list after using List Comprehension ")
"""
    The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
"""
new_list = [x for x in fruits if "a" in x]
print(newlist)

new_list = [x for x in fruits if x !="apple"]
print(new_list)

new_list =[x for x in range(10)]
print(new_list)

new_list =[x.upper() for x in fruits if x !="mango"]
print(new_list)

new_list =["hello" for x in fruits if x !="mango"]
print(new_list)
new_list =[x if x !="banana" else "orange " for x in fruits ]
print(new_list)

"""
 **************** Python - Sort Lists *****************
"""
"""
    Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana","test2","test1"]
thislist.sort()
print(thislist)

thislist_1 =[15,23,4,1,2]
thislist_1.sort()
print(thislist_1)

"""
    Sort Descending
To sort descending, use the keyword argument reverse = True:
"""
thislist_1 =[15,23,4,1,2]
thislist_1.sort(reverse= True)
print(thislist_1)
"""
    Sort Ascending
To sort Ascending, use the keyword argument reverse = False:
"""
thislist_1 =[15,23,4,1,2]
thislist_1.sort(reverse= False)
print(thislist_1)
"""
    Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

Example
Case sensitive sorting can give an unexpected result:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
    Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Example
Perform a case-insensitive sort of the list:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
"""
    Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
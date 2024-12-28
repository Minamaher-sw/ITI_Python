"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Tuple Items - Data Types
Tuple items can be of any data type:

Example
String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
"""
mytuple = ("apple", "banana", "cherry")
print (mytuple)

"""
    Allow Duplicates
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:
"""
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#lenght function 
print(f"Lenght of tuple is {len(thistuple)}")

"""
important note 
    Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple
"""
mytuple_1 =('apple')
print("class type of ('apple')",type(mytuple_1))

mytuple_1 =('apple',)
print (f"class type of ('apple',){type(mytuple_1)}")

#tuple()method to create new tuple
my_tuple =( 1 ,2 , 4,5)
thistuple =tuple(my_tuple)
print(type(thistuple))


"""
    Access Tuple Items
    You can access tuple items by referring to the index number, inside square brackets
    positive index 
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
"""
    Negative Indexing
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[-1])
"""
    Range of index
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0:2])

my_tuple =thistuple[:]
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment
#thistuple[0] ='mina'

"""
    Range of negative index
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

"""
    Check if Item Exists
    To determine if a specified item is present in a tuple use the in keyword:
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if 'apple' in thistuple:
    print(True)
"""
    Unpacking a Tuple
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
    ExampleGet your own Python Server
    Packing a tuple:

    fruits = ("apple", "banana", "cherry")
"""
fruits = ("apple", "banana", "cherry")

"""
    Unpacking a Tuple
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

    ExampleGet your own Python Server
    Packing a tuple:

    fruits = ("apple", "banana", "cherry")
"""
#unpacing 
(item1 , item2 ,item3) =fruits
print(item1)
print(item2)
print(item3)
"""
    Note: The number of variables must match the number of values in the tuple,
      if not, you must use an asterisk to collect the remaining values as a list.
      Using Asterisk* (*args) list type
        If the number of variables is less than the number of values, you can add an *  
        to the variable name and the values will be assigned to the variable as a list:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(item1 ,item2 ,*args) =fruits
print("item1 :",item1)
print("item1 :",item2)
print("*agrs :",args)

(item1 ,*args ,item2) =fruits
print("item1 :",item1)
print("item1 :",item2)
print("*agrs :",args)
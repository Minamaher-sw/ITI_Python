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
    Python - Update Tuples
    Tuples are unchangeable, meaning that you cannot change, add,  
    or remove items once the tuple is created.
But there are some workarounds.
    Change Tuple Values
Once a tuple is created, you cannot change its values. T
tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple.
"""
x = ("apple", "banana", "cherry")
y =list(x)
y[0]="Kiwi"
x =tuple(y)
print("workaround :" ,x)

"""
    Add Items
Since tuples are immutable, they do not have a built-in append() method, 
but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, 
you can convert it into a list, add your item(s), and convert it back into a tuple.

Example
Convert the tuple into a list, add "orange", and convert it back into a tuple:
"""
x = ("apple", "banana", "cherry")
print("tuple : " ,x)
y =list(x)
y.append("orange")
x =tuple(y)
print("adding items by list woraround b using append " ,x)

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

#Example
#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

"""
    Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

Example
Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("after use removve :" ,thistuple)

# del function 
del(thistuple)
#print(thistuple)  error name 'thistuple' is not defined
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
"""
    Loop Through a Tuple
    You can loop through the tuple items by using a for loop.
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for item in fruits :
    print(item)
#loop on indexx
print("by using for and index")
for index in range(len(fruits)):
    print(fruits[index])
#by using while loop
print("by using while and index")
index = 0
while index <len(fruits):
    print(fruits[index])
    index +=1
"""
    Python - Join Tuples
    Join Two Tuples
    To join two or more tuples you can use the + operator:
"""
#ExampleGet your own Python Server
#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 =tuple1 + tuple2
print("join by using +  " ,tuple3)

"""
Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:
"""
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
"""
    Python - Tuple Methods
Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
fruits = ("apple", "banana", "cherry" ,"apple")
print(fruits)
print("fruits count(apple) :",fruits.count("apple"))
print("fruits index(apple)" ,fruits.index("apple"))
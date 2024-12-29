#short if else 
degree =80
if degree < 60 :
    grade ="fair"
else :
    grade ="good"
print (grade )

grade ='fair' if degree < 60 else 'good'
print(grade)

"""
    **************** swap way ***************
    swap two numbers 
"""
x =60
y=70
#way 1 
print("x y" ,x,y)

z= x 
x=y 
y=z
print("after swap x y" ,x,y)

#way 2 by use tuple
x =30
y=89

print("x y" ,x,y)
x,y =y,x
print("after  tuple way x y" ,x,y)

# end of print end ="\n" by default
print("hi mina" ,end=" .")
print("com")

"""
    diff bet   is vs ==

    is is address of memory  in same position
    == values
"""
print("string with == and is")
str_1 ="mina"
str_2 ="mina"
if(str_1 == str_2):
    print("ok")

if(str_1 is str_2):
    print("ok")
print("list with == and is")
lis_1 =[1,2,3]
lis_2 =[1,2,3]
if(lis_1 == lis_2):
    print("ok")

if(lis_1 is lis_2):
    print("ok")
else :
    print("not")
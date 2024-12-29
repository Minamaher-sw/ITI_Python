#short if else 
degree =int(input("enter degree : "))
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

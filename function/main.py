#from cal_fun import *
from  my_package import cal_fun as x 
import math 
# DRY DON'T Repeet yourself 
def my_calTax_1(salary):
    Tax = (20/100) *salary
    if Tax :
        return Tax/2
    return 10
print(my_calTax_1(3000))
print(my_calTax_1(0))

#another short wayy
def my_calTax_2 (salary):
    Tax = (20/100) *salary
    return Tax and Tax/2 or 10
print(my_calTax_2(3000))
print(my_calTax_2(0))

#default value in function last parameter
def my_CalProfits(salary , Bonus =100):
    profits = (20/100)*salary + Bonus
    return profits
print(my_CalProfits(2000))
print(my_CalProfits(2000 , 300))

"""
    *args with function 
    class -> tuple
    **kwargs 
    class -> dictionary
"""
def m_sum(z ,x ,*args):
    return sum(args)+z+x
# positional call order 
print(m_sum(1 ,2 ,3,4 ,5))

#name call 
def my_sum( *arg1 ,x, y,z ,):
    sum_1 = x+y+z +sum(arg1)
    return sum_1 
print(my_sum( 12 ,12 ,12 ,z=40 ,y=10 ,x=10))

#un limited argument with name use 
def my_sum_1( x, y,z ,**kwarg ):
    sum_1 = x+y+z +sum(kwarg.values())
    return sum_1 
print (my_sum_1( z=40 ,y=10 ,x=10 , p=13 ,q=122 ,n=10 ))

#note positional argument not follow keyword arguument
def my_sum_2( *args ,x, y,z  ,**kwarg ):
    sum_1 = x+y+z +sum(args)+sum(kwarg.values())
    return sum_1 
print (my_sum_2(12 , 13,14 , z=40 ,y=10 ,x=10 , p=13 ,q=122 ,n=10 ))

"""
                story of scope
                lexical scope  from inner to outer
                globale scope  
"""
print(" lexical scope")
name ="ali"
def my_func (my_name ):
    name =my_name
    print(name)

my_func("mina")
print(name)

name ="ali"
def my_func_1 (my_name ):
    print(name)

my_func_1("mina")
print(name)

print(" global key word")
name ="ali"
def my_func_2 (my_name ):
    global name
    name =my_name
    print(name)
my_func_2("mina")
print(name)

print (x.sum_1(12,13,14))
lis =[1,2,3,4,5]
print (math.pow(2,3))
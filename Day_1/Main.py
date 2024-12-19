# Tricks In Python
# Hello World Programe 
print("Hellow World ") 

#Line Indentations in python Level_1 level_2  
a = 4 ;
if a == 4 :
    print("Hello World")
else :
    print("Hello World ")

# Quotes Tricks 
# Mlti Line Comment 
""" 
Single Quote is same Double Quotes in use 
Double Quotes
Triple Quotes is more readale Double Quote \n in Multi line string 
"""
word = ' word' #Single Quote is same Double Quotes in use 
sentence = "This is a sentence."
#Triple Quotes is more readale 
paragraph_1 ="his is a paragraph \n It is made up of multiple lines and sentences \n"
paragraph_2 = """This is a paragraph.
 It is made up of multiple lines and sentences.""" 
print(word ,'\n',sentence,'\n',paragraph_1,paragraph_2)

#Name Convension in python 
"""
in this shape 
is_student
first_name 
"""

"""
Type  is function to get data type  of enter variable 
    Strings 
    Numbers 
    Boolean 
    Tuples 
    Lists 
    Dictionaries

   parameter : is Variable 
   return :Data Type of Variable 
"""
first_name='Mina'
last_name =["Maher"]
age = 25 
long =12.5
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(long))

# casting function 
"""
 Cating Function
 it's Formula   type(variale)
 """
value_1 = 15.5
value_2 = 15
value_3 = 'mina'
value_4 =float(value_2)
value_5 =int(value_1)
value_6 =str(value_1)
#note
"""
if variable contain string and this string is number only
  a ='11' or '1' or '11111..'
  we can make for it casting with int  and float 
  but 
  if string contain at least one character casting will give you error
"""
value_3_1 ='1'
value_8=int(value_3_1)
value_9 =float(value_3_1)
# error value_10 = int(value_3)

print(value_1)
print(value_2)
print(value_3)
print(value_4)
print(value_5)
print(value_6)
print(value_8)
print(value_9)
"""                  ***************************
                        Arithmetic operators 
                 *********************************
"""
"""
+   addition Op  
-   Subtraction Op 
*   Multiplication Op 
/   Division Op  
%   Modulus Op 
//  Division without Fractions 
**  Exponent Op

"""
Cal_operand_1 =12 
Cal_operand_2 =5
# 12+5 =17
add_op1_op2 =Cal_operand_1 + Cal_operand_2 
#12 -5 = 7
sub_op1_op2 =Cal_operand_1 - Cal_operand_2 
#12*5 = 60
mul_op1_op2 =Cal_operand_1 * Cal_operand_2 
#12 %5 = ( 12//5 =2 s0 12 %5 = 12 - (5*2)=2
mod_op1_op2 =Cal_operand_1 % Cal_operand_2 
# 12/5 = 2.4
Div_op1_op2 =Cal_operand_1 /Cal_operand_2 
# 12 // 5 = 2
Dwf_op1_op2 =Cal_operand_1 //Cal_operand_2 
# 12 ** 5 = 12^5 pow(12,5) = 
exp_op1_op2 =Cal_operand_1 **Cal_operand_2 
print("*************** Arithmetic operators ************* ")
print("two operand  is ",Cal_operand_1 ,Cal_operand_2)
print("addition of op1 and op2 = ",add_op1_op2)
print("substraction of op1 and op2 = ",sub_op1_op2)
print("Multiplication of op1 and op2 = ",mul_op1_op2)
print("Division of op1 and op2 = ",mod_op1_op2)
print("Modulus  of op1 and op2 = ",Div_op1_op2)
print("Division without Fractions of op1 and op2 = ",Dwf_op1_op2)
print("Exponent Op of op1 and op2 = ",exp_op1_op2)

"""                             ***************************
                        AAssignment  operators with Arithmetic operators 
                             *********************************
"""
"""
=    assign 
+=   add and assign  
-=   subtract and assign 
*=   multiply and assign 
/=   divide and assign  
%=   get modulus and assign 
//=  floor divide and assign 
**=  get exponent and assign

"""
#assign 
cal_oper_3 = 12 
cal_oper_4 = 5
result = cal_oper_3
print("******* Assignment  operators with Arithmetic operators section ** ")
result += cal_oper_4   #add and assign  
print(result)
result -= cal_oper_4   #subtract and assign 
print(result)
result *= cal_oper_4  #multiply and assign 
print(result)
result /= cal_oper_4  #divide and assign  
print(result)
result %= cal_oper_4 #get modulus and assign 
print(result)
result //= cal_oper_4  #floor divide and assign 
print(result)
result **= cal_oper_4 #  get exponent and assign
print(result)
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
print("******* Assignment  operators with Arithmetic operators section ** ")
result = cal_oper_3
result += cal_oper_4   #add and assign  
print(result)

result = cal_oper_3
result -= cal_oper_4   #subtract and assign 
print(result)

result = cal_oper_3
result *= cal_oper_4  #multiply and assign 
print(result)

result = cal_oper_3
result /= cal_oper_4  #divide and assign  
print(result)

result = cal_oper_3
result %= cal_oper_4 #get modulus and assign 
print(result)

result = cal_oper_3
result //= cal_oper_4  #floor divide and assign 
print(result)

result = cal_oper_3
result **= cal_oper_4 #  get exponent and assign
print(result)

"""
       *****************************************  *********************88
                              False Tricks
        if value o any varialble (x)is false if
        1-  = '' or "" or """ """ --> empty string 
        2-  =0
        3-  = None
        4-  = {} or [] or ()
        5-  = false 

            if x :    this condition is false 
        any value of x other these is true 
"""
my_list =[]  #empty string 
if my_list : # condition false
    print("list not empty")
else:
    print("list is empty")

my_list =[1]  #non empty string 
if my_list : # condition true
    print("list not empty")
else:
    print("list is empty")

var_1 =None 
if var_1 :
    print("not good ")
else :
    print("good")
var_2 ='' 
if var_2 :
    print("str not empty ")
else :
    print("str empty")

"""
            ***************************************  *****************  ********************************
                                               Strings and operation on it 
            ***************************************  *****************  ********************************                                    
"""
first_name ="Mina"
last_name  ="Maher"
#operation 
first_name=first_name.upper()
print(first_name)
first_name=first_name.lower()
print(first_name)
#solve error 
if first_name.isdigit():
    print(int(first_name))
else :
    print("not digit")

#  *******************************  How we get Full Name 6 ways ************************ #
# First way  poor use high mistakes 
full_name =first_name +" "+ last_name 
print("Full name is ",full_name  )

# Second way 
full_name = "Full name is %s %s"%(first_name , last_name)
print(full_name  )

# Third way
"""
 trick
 full_name = "Full name is {} {}".format(first_name , last_name ,... , ... ,...) is true becouse number of elements more than and equal number of bracs
 but 
 full_name = "Full name is {} {}".format(first_name ) is false 

"""
full_name = "Full name is {} {}".format(first_name , last_name)
print(full_name  )

# problem is dublicate for elements 
full_name = "Hello {} your Full name is {} {}".format(first_name ,first_name , last_name)
print(full_name  )

# way num 4  index way solve for dublicate at way 3 by index
full_name = "Hello {0} your Full name is {0} {1}".format(first_name , last_name)
print(full_name  )

#way nm 5 is more readable than way num 4
name_array = "Hello {first_name} your Full name is {first_name} {last_name}"
full_name = name_array.format(first_name = first_name, last_name= last_name)
print(full_name  )

# way num 6 is more readable than way 5 character  f and we delet formate fnction
full_name = f"Hello {first_name} your Full name is {first_name} {last_name}"
print(full_name  )


"""
                        mutable and immmutable 
                              strings
"""

name_str="menamaher"
#error 'str' object does not support item assignment
# name_str[1]='i'
#to change thi character two way
#way_1
name_str="minamaher"
print(name_str)
#way_2   we use replace function 
"""
            *********** Replace Function *************
            parameter_1 = char that want to change 
            parameter_2 = new char 

            return : new address of new string 
            change isn't inplcae 
"""
#no change  becouse change isn't inplcae 
name_str="menamaher"
name_str.replace('e','i')
print(name_str)

#solu
# replace each character (e) and set i instead of it 
name_str_2 = name_str.replace('e','i')
print(name_str)
print(name_str_2)

"""
        ******************** Slice of String *****************************
        we can take part from string 
"""
full_name ="Mina Maher Mosadef"
first_name =full_name[:5] #count from 0 to 4 M i n a ''
sec_name = full_name[5:11]
last_name = full_name[11:]

print("full_name  is " , full_name)
print("first_name is " ,first_name)
print("sec_name   is " ,  sec_name)
print("last_name  is " , last_name)

# Step 
any_char =full_name[::2] # mean from start to end with step 2 
print("any char is " ,any_char)

#to get last char fam way 
# nead to know lenthg not recommend 
last_char_of_fn =full_name[17:]
print("last char of full name" ,last_char_of_fn)
#second is reccomend 
last_char_of_fn =full_name[-1] # -1 is last char f and -2 is e -3 is d so
print("last char of full name" ,last_char_of_fn)

#   ****************  how we can revrse string  ************************** 
# way 1
Reverse_name_1 =full_name[-1 ::-1]# start is last char and end first char and step is back step -1
print("Reverse name way 1 is ",Reverse_name_1)

#way 2
Reverse_name_2 = full_name[::-1] # from last char to start char and step is back step -1
print("Reverse name way 2 is ",Reverse_name_2)

"""
     *************************  Length Function ********************* 
     fnction number of character or elemnts in string , ist 

     parameter : Variable 
     return : Lenght of variable 
"""
Lenght_Full_neme =len(full_name)
print(type(Lenght_Full_neme))
print(Lenght_Full_neme)


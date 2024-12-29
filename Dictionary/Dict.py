# ****************8 Lecture *******************8
# Hetrogenous data type 
t1 =(12 , "mina")
t2 =(13 ,"maher")
list_1 =[t1 ,t2]
print("t1" ,t1 ,"  ",'t2' ,t2)
print("list_1 =[t1 ,t2] is :",list_1)
print("to get first ellemnet in t1 is 12")
print("fisrt elemet it t1 list_1[0][0] is ",list_1[0][0])

"""
    ************ Dictionary
    keys : values
    keys is imutable so is string 
    nested dictionary is allowed 
"""
my_dict ={"name" :"ali" ,"age" :(13,15,16) ,"email" :["minamosadef@gmail.com"]
          ,"address":{"street" :10 , "block" :8 ,"city":"cairo"}
          }
# access dict 
print(my_dict)
print(my_dict["name"])
print(my_dict["age"][1])
print(my_dict["email"][0])
print(my_dict["address"]["street"])

#change value inside dict
my_dict["name"] ="mina"
print("after change name " ,my_dict)

#loop with dict  loop on key  iterate on keys
print("loop on key ")
for key in my_dict :
    print(my_dict[key])

#loop on values 
print("loop on value ")
for value in my_dict.values():
    print(value)

#loop on key and value 
print("loop on key and value ")
for key ,value in my_dict.items():
    print(key)
    print(value)

#search on dict 
#key 
if "name" in my_dict :
    print("ok")

if "mina" in my_dict.values():
    print("ok")

#how solve access un  known key  key error 
#way 1 by check way 

#way 2 
"""
    .get()
    parameter : key o dict 
    if key in dict return it's value
    if not found return none so nit give keyerror
    to return anything other None
    myy_dict.get(key , "Default Name") "Default Name" will return it if key not in dict 
"""
# at this case print mina 
if(my_dict.get("name")):
    print(my_dict["name"])
else:
    print (my_dict.get("name", "Hi"))
#at this case print HI
if(my_dict.get("nam")):
    print(my_dict["nam"])
else:
    print (my_dict.get("nam", "Hi"))

"""
    update function 
    parameter is : dictionary
    looklike extend with list
"""
print (my_dict)
my_dict.update({"Key1":13 ,"key2" :30})
print("after update function " ,my_dict)

#append in list 
my_dict['my_hoby']="tennsi"
print(my_dict)

#to remove key from dict 
del(my_dict["Key1"])
print(my_dict)

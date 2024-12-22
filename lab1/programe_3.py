my_array=[]

for index in range(0,5):
    my_array.append(int(input(f"enter value of index {index} ")))

def desending_array(my_array):
   for index in range(0,5) :
       min_val=my_array[index]
       for index_2 in range(index ,5):
           if(my_array[index_2] <= min_val):
               min_val =my_array[index_2]
               my_array[index_2] = my_array[index]
               my_array[index] = min_val

desending_array(my_array) 
print(my_array) 

my_array=[]
print("Enter arrray for asending way\n")
for index in range(0,5):
    my_array.append(int(input(f"enter value of index {index} ")))

def asending_array(my_array):
   for index in range(0,5) :
       max_val=my_array[index]
       for index_2 in range(index ,5):
           if(my_array[index_2] >= max_val):
               max_val =my_array[index_2]
               my_array[index_2] = my_array[index]
               my_array[index] = max_val

asending_array(my_array) 
print(my_array) 


               


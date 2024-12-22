input_string =input("Enter  string ")
vowels_char =['a', 'e', 'i', 'o', 'u']
count =0 
for char in input_string :
    if char in vowels_char :
        count +=1
    else:
        continue
print(f"number of vowels char is {count} ")
 

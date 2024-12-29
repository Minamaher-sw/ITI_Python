#short if else 
degree =int(input("enter degree : "))
if degree < 60 :
    grade ="fair"
else :
    grade ="good"
print (grade )

grade ='fair' if degree < 60 else 'good'
print(grade)

"""
 function that takes a number as an argument and if the number 
divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is 
divisible by both return "FizzBuzz"
"""
user_number =int(input("Enter Number : "))
def check_nmber (user_number) :
    while True :
        if(user_number % 3 == 0 and user_number %5 ==0):
            print("FizzBuzz")
            break 
        elif(user_number % 3 == 0) :
            print("Fizz")
            break
        elif(user_number % 5 == 0) :
            print("Buzz")
            break
        else :
           user_number =int(input("Enter Number : "))
check_nmber(user_number)
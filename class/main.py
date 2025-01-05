
"""
    static problem 
    we cannot update values of class becouse is static 
    so sol 
"""
class ComEmployee :
    #class variable  belong class
    active =True
    # --init-- magic function
    def __init__(self , name ,age ,salary ,title ,address ,department):
        #instance variable
        self.name=name
        self.age=age
        self.salary=salary
        self.title=title
        self.address=address
        self.department=department
    

emp1=ComEmployee(name="mina",age=14,salary=1230,title="Devops Engineer",address={"city":"sohag","street":"minst"},department="communication")
emp2=ComEmployee(name="Pepo",age=23,salary=2300,title="Devnet Engineer",address={"city":"sohag","street":"mohmen"},department="Computer science")

print(emp1.name)
print(emp2.name)
print(emp1.address)
#adding new item at emp1 not error but not reccomended
#instance variable belong object
emp1.gender="male"
#display for emp1  address of emp1 0x000001E40F4CCB90
print(emp2)

"""
    access of class variable
"""
print(ComEmployee.active ,emp1.active,emp2.active)
#instance variable
emp1.active=False
print(ComEmployee.active ,emp1.active,emp2.active)
#creet instance variable with same name class variable
emp2.active=False
print(ComEmployee.active ,emp1.active,emp2.active)
"""
    using of class variable
    is variable belong all object of this class 
"""
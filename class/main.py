class ComEmployee :
    # --init-- magic function
    def __init__(self , name ,age ,salary ,title ,address ,department):
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

"""
    static problem 
    we cannot update values of class becouse is static 
    so sol 
"""

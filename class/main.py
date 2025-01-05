
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
        """
            Methodes of class 
        """
    #instance method  99 %it use 
    def get_tax_dol(self):
         return self.salary * .20
    
    def get_tax_egp(self):
        taxs =self.salary * .20
        return self.getConv_dol_egp(taxs)
    #class Method share with all object creete object
    @classmethod
    def greatobject_from_string(cls ,string):
        data_split=string.split("_")
        return cls(data_split[0] ,int(data_split[1]),int(data_split[2]),data_split[3],{data_split[4]:data_split[5],data_split[6]:data_split[7]},data_split[8])
    #Static Method not use ot class 
    @staticmethod
    def getConv_dol_egp(value):
        return value * 55

    
txt="Krkr_14_1230_Devops Engineer_city_sohag_street_minst_communication"
emp1=ComEmployee(name="mina",age=14,salary=1230,title="Devops Engineer",address={"city":"sohag","street":"minst"},department="communication")
emp2=ComEmployee(name="Pepo",age=23,salary=2300,title="Devnet Engineer",address={"city":"sohag","street":"mohmen"},department="Computer science")
emp3=ComEmployee.greatobject_from_string(txt)
print(emp3.name)
#call instance method
emp1_tax=emp1.get_tax_dol()
print("Tax by Dollar" ,emp1_tax)
emp1_tax=emp1.get_tax_egp()
print("Tax in Egp" ,emp1_tax)


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

"""
    inheritance section 
    Employee can be 
    manger 
    sales 
    enginner 
"""
#defination of inheritance adding new atrribute only
class manger(ComEmployee):
    def __init__(self , name ,age ,salary ,title ,address ,department ,office_id):
        super().__init__( name ,age ,salary ,title ,address ,department )
        self.office_id =office_id
    @classmethod
    def manger_greatobject_from_string(cls,string):
        data_split=string.split("_")
        return cls(data_split[0] ,int(data_split[1]),int(data_split[2]),data_split[3],{data_split[4]:data_split[5],data_split[6]:data_split[7]},data_split[8],int(data_split[9]))
    
manger_hr=manger(name="hamada" ,age=44 ,salary=45000 ,title="Manger of Hr section" ,address={"city":"cairo","street":"mary gergres" },department="HR" ,office_id=123)
manger_hr_data="Krkr_14_1230_Devops Engineer_city_sohag_street_minst_communication_123"
manger_hr_2=manger.manger_greatobject_from_string(manger_hr_data)
print(manger_hr_2.office_id)

class any :
    def __init__(self,name ,slaray ):
        self.name=name
        self.slaray=slaray
        self.taxs=self.slaray *.20
emp1=any(name="mina", slaray=2200 )
# DRY DON'T Repeet yourself 
def my_calTax_1(salary):
    Tax = (20/100) *salary
    if Tax :
        return Tax/2
    return 10
print(my_calTax_1(3000))
print(my_calTax_1(0))

#another short wayy
def my_calTax_2 (salary):
    Tax = (20/100) *salary
    return Tax and Tax/2 or 10
print(my_calTax_2(3000))
print(my_calTax_2(0))
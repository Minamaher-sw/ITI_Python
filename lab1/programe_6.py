radiaS_circle = int(input("Enter radias of circle : "))
PI =3.14
#area
def aree_circle(radiaS_circle):
    area_of_circle = PI*(radiaS_circle**2)
    print(f"area of circle is : {area_of_circle}" )
aree_circle(radiaS_circle)

# circumference
def crf_circle(radiaS_circle):
    crf_of_circle = 2*PI*(radiaS_circle)
    print(f"Circumference of circle is : {crf_of_circle}" )
crf_circle(radiaS_circle)
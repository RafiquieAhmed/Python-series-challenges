#Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(radius):
    area= math.pi*radius**2
    circumferences=2*math.pi *radius
    return area,circumferences

a,c=circle(3)
a,c=round(a,2),round(c,3)
print("area : ",a,"circumferences : ",c)

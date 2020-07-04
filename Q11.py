# Write a python program to compute the area of geometrical objects and display the computed area.
import math
def compute():
    a="y"
    while a.lower()=="y":
        ob=input("Enter the name of geometrical object : ")
        if ob=="circle":
            r=float(input("Enter the radius : "))
            area=math.pi*r*r
        elif ob=="square":
            e=float(input("Enter the edge : "))
            area=e*e
        elif ob=="rectangle":
            l=float(input("Enter the length : "))
            b=float(input("Enter the breadth : "))
            area=l*b
        elif ob == "triangle":
            h=float(input("Enter the height : "))
            b=float(input("Enter the base : "))
            area=(1/2)*h*b
        else:
            pass

        print("Area of "+ob +" is : "+str(area))
        # print("%.2f"%area)
        print("Want to continue ? ")
        a=input("y/n : ")

compute()
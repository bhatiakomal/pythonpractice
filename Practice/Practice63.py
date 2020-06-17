x1=int(input("Enter length of reactangle:"))
y1=int(input("Enter width of reactangle:"))
areaOfReactangle1=x1*y1
print("Print area of reactangle:",areaOfReactangle1,"cm")
x2=int(input("Enter length of reactangle:"))
y2=int(input("Enter width of reactangle:"))
areaOfReactangle2=x2*y2
print("Print area of reactangle:",areaOfReactangle2,"cm")
if areaOfReactangle1>areaOfReactangle2:
    print("Area of reactangle1 is greater than area of reactangle2 ")
elif areaOfReactangle2>areaOfReactangle1:
    print("Area of reactangle2 is greater than area of reactangle1")
else:
    print("Both reactangles have same area")
def show(num1,num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
num1=(int(input("Enter first number:")))
num2=(int(input("Enter second number:")))
result=show(num1,num2)
print("print your result:",result)

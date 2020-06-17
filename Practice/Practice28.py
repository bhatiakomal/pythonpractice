def show(num1,num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
number1=(int(input("Enter first number:")))
number2=(int(input("Enter second number:")))
result=show(number1,number2)
print("print your result:",result)

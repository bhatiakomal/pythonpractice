#Nested function
'''def disp():
    def show():
        print("Show function")
    print("disp function")
    show()
disp()'''


def disp(k):
    def show():
        return "Show Function  "
    result=show() + k + " Disp Function "
    return result
a=disp("komal")
print(a)
#Function returning another Function
def disp():
    def show():
        return "show function"
    print("Disp function")
    return show()
print(disp())
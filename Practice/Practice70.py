def show():
    x=int(input("Enter number:"))
    if x<0 or x>36:
        print("Plz enter number between 0-36")
    else:
        if x==0:
            print("The pocket is green")
        elif x<11:
            if x%2!=0:
                print("The pocket is red")
            else:
                print("The pocket is black")
        elif x<19:
            if x%2!=0:
                print("The pocket is black")
            else:
                print("The pocket is red")
        elif x<29:
            if x%2!=0:
                print("The pocket is red")
            else:
                print("The pocket is black")
        elif x<37:
            if x%2!=0:
                print("The pocket is black")
            else:
                print("The pocket is red")
show()
show()
show()


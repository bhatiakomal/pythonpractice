def disp():
    x=int(input("Enter number of books purchased by customers:"))
    if x==0:
        print("He/she earns 0 points")
    elif x==2:
        print("He/she earns 5 points")
    elif x==4:
        print("He/she earns 15 points")
    elif x==6:
        print("He/she earns 30 points")
    elif x>=8:
        print("He/she earns 60 points")
disp()
disp()
disp()
disp()
def show():
    day=int(input("Enter Day:"))
    month=int(input("Enter month:"))
    year=int(input("Enter year:"))
    if day*month==year:
        print("The date"+str(month)+"/"+str(day)+"/"+str(year)+"is magic")
    else:
        print("The date" + str(month) + "/" + str(day) + "/" + str(year) + "is not magic")
show()
show()
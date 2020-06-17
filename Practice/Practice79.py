speed=int(input("Enter speed of vehicle:"))
time=int(input("Enter time taken vehicle:"))
print("Hours","\tDistance Travell")
for current_hours in range(1,time+1):
    distance = speed * current_hours
    print(current_hours,"\t",distance)

def disp():
    userFat=float(input("Enter fat in gramss:"))
    userCarbs=float(input("Enter carbs in grams:"))
    caloriesFormate=userFat*9
    caloriesFromCarbs=userCarbs*4
    print("calories from fat:",caloriesFormate,\
          "calories from carbs:",caloriesFromCarbs,sep=" ")
disp()
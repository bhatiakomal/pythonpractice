def disp():
    x=int(input("No.of males in the class:"))
    print("No. of males:",x)
    y=int(input("No.of females in the class:"))
    print("No. of males:",y)
    total_students=x+y
    percentage_males=(x/total_students)*100
    print("Percentage of males:",percentage_males,"%")
    percentage_females=(y/total_students)*100
    print("Percentage of females:",percentage_females,"%")

disp()
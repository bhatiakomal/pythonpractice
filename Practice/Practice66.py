x=int(input("Enter mass of object:"))
weight=x*9.8
print("Total weight is:",weight)
if weight>500:
    print("The object weght is:"+format(weight,".2f")+" Its too heavy")
elif weight<100:
    print("The object weght is:"+format(weight,".2f")+" Its too light")
else:
    print("The object weght is:"+format(weight,".2f")+" Its neither heavy nor light")
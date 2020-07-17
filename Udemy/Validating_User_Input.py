'''def user_choice():
    choice=input("Please enter number (0-10) :")
    return int(choice)
rslt=user_choice()
print(rslt)'''

'''def user_choice():
    choice=input("Please enter number (0-10) :")
    return int(choice)
some_value='100'
print(some_value.isdigit())
print(int(some_value))'''

'''def user_choice():
    choice='wrong'
    while choice.isdigit()==False:
        choice=input("Please enter number (0-10) :")
        if choice.isdigit()==False:
                print("That is not digit")komal
    return int(choice)
rslt=user_choice()
print(rslt)'''

'''rslt='wrong'
values=[1,2,3,4,5,6,7,8]
print(rslt not in  values)'''

def user_choice():
    choice = 'wrong'
    values_range = range(0,10)
    within_Range=False
    while choice.isdigit() == False or  within_Range==False:
        choice=input("Please enter number (0-10) :")
        #Digit Check
        if choice.isdigit()==False:
            print("Sorry this is not digit")
        #RAnge Check
        if choice.isdigit()==True:
            if int(choice) in values_range:
                within_Range=True
            else:
                within_Range=False
    return int(choice)
rslt=user_choice()
print(rslt)

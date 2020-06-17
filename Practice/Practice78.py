user_budget=int(input("Enter your monthly budget:"))
more_expensese="y"
user_total_expensese=0
while more_expensese=="y":
    user_expense=input("Enter expense:")
    user_total_expensese+=int(user_expense)
    more_expensese=input("Do you have more expenses?:Type:y for yes for no type N")
if user_total_expensese > user_budget:
    print("You were over your budegt",(user_budget),"by",user_total_expensese-user_budget)
elif user_budget>user_total_expensese:
    print("You were under your budegt",(user_budget),"by",user_budget-user_total_expensese)
else:
    print("You used exactly ur budget:",(user_budget))



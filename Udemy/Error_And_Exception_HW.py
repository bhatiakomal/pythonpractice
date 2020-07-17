'''try:
    for i in['a','b','c']:
        print(i**2)
except TypeError:
    print('Type error! Watch out!')'''

'''try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError:
    print("This is zero divison error:")
finally:
    print('All done')'''

def ask():
    while True:
        try:
            n=int(input("Enter a number:"))
        except:
            print("Plz try again! \n")
            continue
        else:
            break
    print('Your number square is:')
    print(n**2)
ask()



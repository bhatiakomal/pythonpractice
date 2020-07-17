'''def add(n1,n2):
    print(n1+n2)
try:
    add=10+10
except:
    print("Hey it looks u r not add corretly")
print(add)

try:
    f=open('testfile','r')
    f.write('Write a test line ')
except TypeError:
    print('There was a type error')
except OSError:
    print('hey u have an OS error')
finally:
    print('I always run')'''

'''def ask_for_int():
    try:
        result=int(input("Provide a number:"))
    except:
        print("whoops! That is not a number")
    finally:
        print("End od Try/Except/Fianlly")
ask_for_int()'''

def ask_for_int():
    while True:
        try:
            result=int(input("Provide a number:"))
        except:
            print("whoops! That is not a number")
            continue
        else:
            print('YEs thank you')
            break
        finally:
            print("End od Try/Except/Fianlly")
            print("I am always run at the end")
ask_for_int()

'''x=input("Enter word")
print(x)
print(x[0])
print(x[2])
print(x[4])
print(x[6])'''

def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = input("Enter String ")
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)
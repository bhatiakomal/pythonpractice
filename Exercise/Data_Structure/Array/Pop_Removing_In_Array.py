#Ininlizing Array
#Import Array From module
import array
arr=array.array('i',[1, 2, 3, 1, 5])
#Print original array
print("Original Array is:",end='')
for i in range(0,5):
    print(arr[i],end=' ')
print('\r')

#pop( ) method is used to remove element from specific position
#And it return popped item
print('Popped element is:',end=' ')
print(arr.pop(2))

#Array after poping
print('Array after poping:',end=' ')
for i in range(0,4):
    print(arr[i],end=' ')
print('\r')
# using remove() to remove 1st occurrence of 1
arr.remove(5)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
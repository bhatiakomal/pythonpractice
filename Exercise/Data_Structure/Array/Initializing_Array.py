#Ininlizing Array
#Import Array From module
import array
arr=array.array('i',[1,2,3])
#Print Original Array
print ("The new created array is : ",end=" ")
for i in range(0,3):
    print(arr[i],end=' ')
print('\r')

#Using append method append the data at the last
arr.append(4)
#Print after appneding data
print('After Append data:',end=' ')
for i in range(0,4):
    print(arr[i],end=' ')
print("\r")

#Using Insert( ) method insert data at the specific position
#here insert 10 at 3rd position
arr.insert(3,10)
print('Array after insertion:',end=' ')
for i in range(0,5):
    print(arr[i],end=' ')
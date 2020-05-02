from numpy import*
a=array([101,102,103,104,105])
b=array([[10,20,30,40],[50,60,70,80]])
print()
#ndim Attribute
print("1D array ndim:",a.ndim)
print("2D array ndim:",b.ndim)

#Shape Attribute
#for 1D  array shape elements in the row
# #for 2D  array shape specifies number of rows and column in each row
print("1D array shape:",a.shape)
print("2D array shape:",b.shape)
#Size attribute
print("1D array size:",a.size)
print("2D array size:",b.size)
#Itemsize
print("1D array itemsize:",a.itemsize)
print("2D array itemsize:",b.itemsize)
#dtpe
print("1D array dtye:",a.dtype)
print("2D array dtye:",b.dtype)
#nbytes
print("1D array nbytes:",a.nbytes)
print("2D array nbytes:",b.nbytes)

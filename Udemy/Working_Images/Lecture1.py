#Working with Images
'''from PIL  import Image
mac=Image.open('example.jpg')
print(mac)
print(type(mac))
#To see image call show()
mac.show()
#To know about size of image;
print(mac.size)'''

#Crop mathod
'''from PIL  import Image
mac=Image.open('example.jpg')
print(type(mac))
print(mac.size)
x=0
y=0
w=720/3
h=960/10
mac=mac.crop((x,y,w,h))
print(mac)
#mac.show()

img_in_img=mac.crop((x,y,w,h))
print(mac.paste(im=img_in_img,box=(0,0)))
img_in_img.show()'''





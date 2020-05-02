d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish"}
print(d1)#this can print whole dictionary

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish"}
print(d1["Harry"])#this only print harry vakue ie burger

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish", "Suraj":{"B":"Bread","L":"Rice","D":"roti"}}
print(d1["Suraj"])#by this we can add some dictionary and values

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish", "Suraj":{"B":"Bread","L":"Rice","D":"roti"}}
print(d1["Suraj"]["D"])#it determine particular value

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish"}
d2=d1.copy()#this is copy function
print(d2)

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish", "Suraj":{"B":"Bread","L":"Rice","D":"roti"}}
print(d1.get("Harry"))

d1={"Harry":"Burger","Ram":"Roti","Rohit":"Fish", "Suraj":{"B":"Bread","L":"Rice","D":"roti"}}
d1.update({"Rashika":"Maggie"})#update additional term
print(d1)
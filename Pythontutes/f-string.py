#Integer
'''a=10
b=20
m=f"{a}"
print(m)
print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")

#Float
print("***float***")
c=10.20
d=45.23
print(f"{c}")
print(f"{c} {d}")
print(f"{d} {c}")

#String
k1="komal"
k2="harry"
print(f"{k1}")
print(f"{k1} {k2}")
print(f"{k2} {k1}")

name="komal"
age="23"
print(f"{name}")
print(f"{name} {age}")

#[fill][align][sign][#][width][,][.precision]type
num=324
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:>5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")

#Float
num=32.24
print(f"{num:8f}")
print(f"{num:08f}")
print(f"{num:+8.3f}")
print(f"{num:<8.2f}")
print(f"{num:*<8f}")
print(f"{num:>8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print(f"{num:*^8.2f}")

num=32.24
print(f"{num:8f}")
print(f"{num:08f}")
print(f"{num:+8.3f}")
print(f"{num:<8.2f}")
print(f"{num:*<8f}")
print(f"{num:>8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print(f"{num:*^8.2f}")'''

name="Suraj"
print(f"{name:8s}")
print(f"{name:<8}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8s}")
print(f"{name:^8}")
print(f"{name:*^8s}")

name="Suraj"
print(f"{name:.3s}")
print(f"{name:<8.3}")
print(f"{name:*<8.3}")
print(f"{name:>8.3}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3}")
print(f"{name:*^8.3s}")

rate=123456789901
print(f"{rate:,}")
print(f"{rate:_}")

name="komal"
age="23"
print(f"{name}")
print(f"my name is {name} and my age is{age}")

a=50
b=2
print(f"{a/b:.2%}")

a=(10,89)
print(f"{a[0]} {a[1]}")

data={'rahul':20,'komal':80}
print(f"{data['rahul']:d} {data['komal']:d}")

name="komal"
print(f"{name.upper()}")

#Date and time
from  datetime import datetime
today=datetime(2019,10,8)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
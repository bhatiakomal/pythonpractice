class Mobile:
    fp="yes"                #class variable
    @classmethod            #Class Method
    def is_fp(cls):         #Class Method
       print(cls.fp)        #Accessing Class variable
realme=Mobile()
redmi=Mobile()
geeks=Mobile()
print('Class Fp',Mobile.fp)
print('RealMe ',realme.fp)
print('RedMi ',redmi.fp)

print()
Mobile.fp='No'
print('Class Fp',Mobile.fp)
print('RealMe ',realme.fp)
print('RedMi ',redmi.fp)

print()
realme.fp="Not working"
print('Class Fp',Mobile.fp)
print('RealMe ',realme.fp)
print('RedMi ',redmi.fp)

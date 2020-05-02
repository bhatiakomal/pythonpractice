# Format( )Method
print("{}".format(10))  #Do not writ space between {}
print("{} {}".format(10,20))
print("   {}    {}".format(10,20))
print("{0} {1}".format(10,20))
print("{1} {0}".format(10,20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10,num2=20))
print("{num2} {num1}".format(num1=10,num2=20))

#Float
print("{}".format(10.45))  #Do not writ space between {}
print("{} {}".format(10.45,20.65))
print("   {}    {}".format(10.45,20.65))
print("{0} {1}".format(10.45,20.65))
print("{1} {0}".format(10.45,20.65))
print("{num1}".format(num1=10.45))
print("{num1} {num2}".format(num1=10.45,num2=20.65))
print("{num2} {num1}".format(num1=10.45,num2=20.65))

#String
print("{}".format("hii"))  #Do not writ space between {}
print("{} {}".format("hii","komal"))
print("   {}    {}".format("hii","komal"))
print("{0} {1}".format("hii","komal"))
print("{1} {0}".format("hii","komal"))
print("{num1}".format(num1="hii"))
print("{num1} {num2}".format(num1="hiii",num2="komal"))
print("{num2} {num1}".format(num1="hii",num2="komal"))


print("hello my name is{}".format("komal"))
print("{} {}".format(10,"komal"))
print("   {}    {}".format("koma",20.65))
print("{0} {1}".format(10.45,"komal"))
print("{1} {0}".format(10,"komal"))
print("{num1}".format(num1=10.45))
print("{num1} {str1}".format(num1=10,str1="priya"))
print("{str1} {num1}".format(num1=10,str1="aarti"))

print("{:d}".format(10))
print("{0:d}".format(10))
print("{num:d}".format(num=10))

#:[fill][align][sign][#][width][,][.precision]type
print("{num:5d}".format(num=10))
print("{num:05d}".format(num=10))
print("{num:+5d}".format(num=10))
print("{num:<5d}".format(num=10))
print("{num:>5d}".format(num=10))
print("{num:*>5d}".format(num=10))
print("{num:*<5d}".format(num=10))
print("{num:^5d}".format(num=10))
print("{num:*^5d}".format(num=10))

print("{}".format(11.11))
print("{:f}".format(11.11))
print("{0:f}".format(11.11))
print("{num:f}".format(num=11.11))
print("{num:8f}".format(num=11.11))
print("{num:8.3f}".format(num=11.11))
print("{num:+8.3f}".format(num=11.11))
print("{num:<8.3f}".format(num=11.11))
print("{num:*<8.3f}".format(num=11.11))
print("{num:>8.3f}".format(num=11.11))
print("{num:*>8.3f}".format(num=11.11))
print("{num:^8.3f}".format(num=11.11))
print("{num:*^8.3f}".format(num=11.11))

print("{:.3s}".format("KomalBhatia"))
print("{:<8.3s}".format("KomalBhatia"))
print("{:*<8.3s}".format("KomalBhatia"))
print("{:>8.3s}".format("KomalBhatia"))
print("{:*>8.3s}".format("KomalBhatia"))
print("{:^8.3s}".format("KomalBhatia"))
print("{:*^8.3s}".format("KomalBhatia"))

print("{:,}".format(123456789))
print("{:_}".format(123456789))

data1={'rahul':20,'komal':80}
print("{0[rahul]:d} {0[komal]:d}".format(data1))
print("{rahul} {komal}".format(**data1))
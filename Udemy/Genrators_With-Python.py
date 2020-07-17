def creat_cubes(n):
    for i in range(n):
        yield i**3
for x in creat_cubes(10):
    print(x)
print(list(creat_cubes(20)))
def show(*name):
    print(name)
    print(name[1])
    print(name[3])
show('surya','komal','ankit','aarti')

def show(*name):
    return name
result=show('surya','komal','ankit','aarti')
print(result)




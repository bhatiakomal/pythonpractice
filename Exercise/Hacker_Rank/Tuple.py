'''t=(input().split())
p=tuple(t)
print(p)
print(type(p))'''

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))


from array import *
i = 5
while i >= 1:
    print('Kousik', i, end=' ')
    j = 1
    while j <= i:
        print('Manna', j, end=' ')
        j = j + 1
    i = i - 1
    print()
print('It,s cool!')
v = array('i', [4, 4, 5])
print(v.itemsize)
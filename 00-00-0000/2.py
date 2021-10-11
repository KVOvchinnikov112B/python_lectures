print('введите трёхзначное число')
a = input()
a = int(a)
ed = a // 100
a = a - ed*100
dec = a // 10
a = a - dec*10
sot = a // 1
a = a - sot*1
b = ed+dec+sot
print(b)
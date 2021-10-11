print('введите число')
a = int(input())
b = a - (a // 100)*100 - (a % 10) + a // 100 + (a % 10) * 100
print(b)
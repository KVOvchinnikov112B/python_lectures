print('Введите одно число')
a = int(input())
a = a - (a // 10 - (a // 100)*10)*10
print(a)
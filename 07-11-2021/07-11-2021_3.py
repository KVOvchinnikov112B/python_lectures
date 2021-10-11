print ('Введите номер года')
n = int(input())
if ((n%10 == 4) and (n%100 == 0)) or(n%1000 == 400):
                   print('YES')
else:
    print('NO')

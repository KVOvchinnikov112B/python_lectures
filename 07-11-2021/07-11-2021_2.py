print('Введите число минут')
n = int(input())
hours = n // 60
mins = n % 60
if hours >= 24:
    hours -=24
print ('Время на часах:',hours,'часов',mins,'минут',sep=' ')

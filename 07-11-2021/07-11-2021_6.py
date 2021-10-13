print ('Введите начальную клетку')
str1 = int(input())
stol1 = int(input())
print ('введите конечную клетку')
stol2 = int(input())
str2 = int(input())

if ((str1 == str2) and (stol1 != stol2)) or ((stol1 == stol2) and (str1 != str2)):
    print('YES')
else:
        print('NO')

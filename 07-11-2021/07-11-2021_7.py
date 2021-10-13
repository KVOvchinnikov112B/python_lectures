print ('Введите начальную клетку')
str1 = int(input())
stol1 = int(input())
print ('введите конечную клетку')
str2 = int(input())
stol2 = int(input())

if ( (str1-1 == str2) or (str1+1 == str2) ) and ( (stol1+2 == stol2) or (stol1-2 == stol2) ) or( (stol1-1 == stol2) or (stol1+1 == stol2) ) and ( (str1+2 == str2) or (str1-2 == str2) ) :
     print('YES')
else:
    print ('NO')

    
 

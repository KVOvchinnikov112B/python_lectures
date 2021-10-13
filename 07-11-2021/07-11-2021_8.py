print ('Введите длину бортиков')
N = int(input())
M = int(input())
print ('Введите расстояние до длинного бортика')
x = int(input())
print ('Введите расстояние до короткого бортика')
y = int(input())

if M>N:
    long = M
    short = N
else:
    long = N
    short = M

if x > long//2:
    x = long - x

if y > short//2:
    y = short - y

if x>y:
    print(y)
else:
    print(x)
    

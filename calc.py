print (" ")
print ("Напишите желаемую операцию в формате (число) (действие) (число), вводя по отдельности")
a = int(input())
oper = input()
b = int(input())
if oper == "+":
    print (a+b)
elif oper == "-":
    print (a-b)
elif oper == "*":
    print (a*b)
elif (oper == "/") and (b != 0):
    print (a/b)
elif (oper == "/") and (b == 0):
    print ("Сам дели на ноль")





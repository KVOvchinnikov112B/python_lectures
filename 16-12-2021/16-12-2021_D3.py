file1 = open('16-12-2021_D3.txt', 'r')
A = ['']
i = 0 
p = 0

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # записываем строку
    (A).append(line.strip())
    i += 1

#Убираем лишнее
for i in range(len(A)):
    A[i] = A[i].replace(',', ' ')
    A[i] = A[i].replace('!', ' ')
    A[i] = A[i].replace('–', ' ')
    A[i] = A[i].replace('.', ' ')
    A[i] = A[i].replace(':', ' ')
    A[i] = A[i].replace(';', ' ')
print(A)

B = ['']
k = 0

# разбивка на слова
for i in range(len(A)):
    p = 0
    for j in range(1,len(A[i])):
        if (A[i][j] == (' ')) :
            B.append(A[i][p:j])
            p = j
            k +=1
print(B)

#Подчистить пробелы
print('def')
for i in range(len(B)):
    B[i] = B[i].replace(' ', '')
print(B)

#Ловеркейснуть
#Всё ради того, чтобы компьютер смог это съесть
print('def')
for i in range(len(B)):
    B[i] = B[i].lower()
print(B)

#Убрать пустые подстроки
C = ['']
print('def')
i = 0
for i in range(len(B)):
    if B[i] != (''):
        C.append(B[i])
        i += 1
C.remove('')
print(C)
#Если на этом моменте у вас не заболела голова и не появились рвотные позывы,
#то вы - индус.

#займёмся подсчётами
D = {}
BigD = {}
for i in range(len(C)):
    s = C.count(C[i])
    D = {C[i]: s}
    BigD.update(D)

print(BigD)

print(max(BigD.values()))

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
#file1 = open('16-12-2021_D3.txt', 'r')
A = ['']
i = 0 
p = 0

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # записываем строку
    (A).append(line.strip())
    i += 1

#Убираем лишнее
for i in range(len(A)):
    A[i] = A[i].replace(',', ' ')
    A[i] = A[i].replace('!', ' ')
    A[i] = A[i].replace('–', ' ')
    A[i] = A[i].replace('.', ' ')
    A[i] = A[i].replace(':', ' ')
    A[i] = A[i].replace(';', ' ')
print(A)

B = ['']
k = 0

# разбивка на слова
for i in range(len(A)):
    p = 0
    for j in range(1,len(A[i])):
        if (A[i][j] == (' ')) :
            B.append(A[i][p:j])
            p = j
            k +=1
print(B)

#Подчистить пробелы
print('def')
for i in range(len(B)):
    B[i] = B[i].replace(' ', '')
print(B)

#Ловеркейснуть
#Всё ради того, чтобы компьютер смог это съесть
print('def')
for i in range(len(B)):
    B[i] = B[i].lower()
print(B)

#Убрать пустые подстроки
C = ['']
print('def')
i = 0
for i in range(len(B)):
    if B[i] != (''):
        C.append(B[i])
        i += 1
C.remove('')
print(C)
#Если на этом моменте у вас не заболела голова и не появились рвотные позывы,
#то вы - индус.

#займёмся подсчётами
D = {}
BigD = {}
for i in range(len(C)):
    s = C.count(C[i])
    D = {C[i]: s}
    BigD.update(D)

print(BigD)

print(max(BigD.values()))

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
#функцию взял с рустаковерфлоу 
        
print('Искомое значение:',get_key(BigD,(max(BigD.values()))))
#Завершено.
#Мой духовный учитель: https://yanderedev.wordpress.com




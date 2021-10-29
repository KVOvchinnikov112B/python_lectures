print ('Введите значения списка, закончив их нулём')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
A.remove(1)
A.pop(len(A)-1)

def srar(A):
    S = 0
    for i in range(len(A)):
        S += A[i]
    return S/len(A)

print(A)
print(srar(A))

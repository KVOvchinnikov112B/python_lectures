class Student:
    def __init__(self, name, age, surname, sex, stud):
        self.name = name
        self.age = age
        self.surname = surname
        self.sex = sex
        self.stud = stud
        
    def naidi_raboty(self):
        print(self.name,',',self.age,',',self.surname,',',self.sex,',',self.stud)

s1 = Student("Валера",17,"Жмышенко","М",346468) #буква пола по-русски
s2 = Student("Имя", 18,"Фамилия","М",124362)
s3 = Student("Виталий",31,"Цаль","М",134794)
s4 = Student("Рофлан",16,"Лицо","Ж",157241)
s5 = Student("Тестовоеимя",18,"Пожадуйстаигнорируйте","Ж",177013)

s0 = Student("Тараскин",0,"Павел","М",000000)

students = [s1, s2, s3, s4, s5]
students1 = [s1, s2, s3, s4, s5]

for i in range(0,len(students)):
    print(students[i].naidi_raboty())

#2 ВОПРОС
print('ВТОРОЙ ВОПРОС')
def students_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j].age > A[j + 1].age:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A
        
d = students_sort(students)

for i in range(len(d)):
    for j in range (len(students)):
        if (d[i].age == students[j].age):
            if d[i].age != 0 :
                print(students[j].naidi_raboty())
                d[i] = s0

#3 ВОПРОС
print('ТРЕТИЙ ВОПРОС')
def bin_search(target, nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        guess = nums[m].age
        if guess == target:
            return students1[m].naidi_raboty()
        if target < guess:
            r = m - 1
        else:
            l = m + 1
    return ('no')
        
sigma = students_sort(students1)
target = 31
ind = bin_search(target, sigma)
print(ind)
if ind == 'no':
    print("Число %d не было найдено!" % target)

for j in range (len(students)):
    if (target == students[j].age):
        print(students[j].naidi_raboty())
        break

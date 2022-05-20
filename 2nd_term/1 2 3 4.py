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



students = [s1, s2, s3, s4, s5]

for i in range(0,len(students)):
    print(students[i].naidi_raboty())

#2 ВОПРОС

students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]

def bubble_sort(c):
    a = c[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

d = bubble_sort(students_age)

for i in range(len(d)):
    for j in range (len(students)):
        if (d[i] == students_age[j]):
            print(students[j].naidi_raboty())
            students_age[j] = ''


#3 ВОПРОС
print('ТРЕТИЙ ВОПРОС')
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
def bin_search(target, nums):
    # Определяем границы поиска (начальные)
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        guess = nums[m]
        if guess == target:
            return m
        if target < guess:
            r = m - 1
        else:
            l = m + 1
    return ('no')
    

students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
sigma = bubble_sort(students_age)
target = 31

ind = bin_search(target, sigma)

if ind == 'no':
    print("Число %d не было найдено!" % target)

for j in range (len(students)):
    if (target == students_age[j]):
        print(students[j].naidi_raboty())
        break

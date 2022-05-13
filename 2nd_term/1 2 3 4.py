# Создание класса, описывающего студента
# Класс - это описание (шаблон) объекта (студента)
class Student:
    # Функция-конструктор - для создания объекта
    def __init__(self, name, age, surname, sex, stud):
        # Заполняем поля (внутренние переменные) объекта
        self.name = name
        self.age = age
        self.surname = surname
        self.sex = sex #NOW
        self.stud = stud
        
    def naidi_raboty(self):
        print(self.name,',',self.age,',',self.surname,',',self.sex,',',self.stud)

# Создаем объекты по шаблону (классу)
s1 = Student("Валера",17,"Жмышенко","М",346468) #буква пола по-русски
s2 = Student("Маша", 18,"Пожилая","М",124362)
# print(s2.name, s2.group, s2.email)
s3 = Student("Виталий",31,"Цаль","М",134794)
s4 = Student("Рофлан",16,"Лицо","Ж",157241)
s5 = Student("Анастасия",18,"Окёнинсберг","Ж",177013)
# Создаем список из студентов
students = [s1, s2, s3, s4, s5]

for i in range(0,len(students)):
    print(students[i].naidi_raboty_eblan())

#2 ВОПРОС

students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]

def bubble_sort(c):
    # создаем копию исходного массива
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
            print(students[j].naidi_raboty_eblan())
            students_age[j] = ''


#3 ВОПРОС
print('ТРЕТИЙ ВОПРОС')
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
def bin_search(target, nums):
    # Определяем границы поиска (начальные)
    l = 0
    r = len(nums) - 1
    while l <= r:
        # Вычисляем индекс числа посередине
        m = (l + r) // 2
        # Берем это число
        guess = nums[m]
        # Сравниваем число с искомым
        if guess == target:
            return m
        # Если проверяемое число не совпадает с искомым,
        # то определяем половину, в которой находится искомое число
        if target < guess:
            # Нужно рассмотреть левую половину, поэтому сдвигаем правый указатель за середину
            r = m - 1
        else:
            # Нужно рассмотреть правую половину, поэтому сдвигаем левый указатель за середину
            l = m + 1
    # Возвращаем -1 если в цикле ни один элемент не прошел условие
    return ('no')
    


# У нас есть упорядоченный массив из чисел
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
sigma = bubble_sort(students_age)
target = 31

# Используем функцию для поиска индекса числа в массиве
# ind = linar_search(target, nums)
ind = bin_search(target, sigma)

# Выводим число и его индекс
if ind == 'no':
    print("Число %d не было найдено!" % target)

for j in range (len(students)):
    if (target == students_age[j]):
        print(students[j].naidi_raboty())
        break

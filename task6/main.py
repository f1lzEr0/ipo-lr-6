#Kisel Artyom
import random
#генерируем список со списками
some_list = [[random.randint(-10,10) for i in range(4)] for i in range(20)]
unique = []
#перебераем значения из some_list и записываем уникальные значения в unique в виде кортежей
for nums in some_list :
    if tuple(sorted(nums)) not in unique:
        unique.append(tuple(sorted(nums)))
#выводим список с кортежами
print("Список с кортежами: ",unique)
sum_in = int(input("Введите число для сравнения: "))
#перебираем кортежи и находим их сумму, после сравниваем её с введённым числом
for nums in unique:
    sum_nums = 0
    for num in nums:
        sum_nums +=num
    if sum_in > sum_nums:
        print(F"сумма пары {nums} меньше {sum_in}")
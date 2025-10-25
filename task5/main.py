#Kisel Artyom
import random
#Счётчики положительных, отрицательных и нулевых чисел
count_plus = 0
count_minus = 0
count_zero = 0
#генерируем список
nums = [random.randint(-50,50) for i in range(25)]
#создаём три списка с положительными, отрицательными и нулевыми числами
plus = []
minus = []
zero = []
#выводим список всех чисел
print("Наш список: ",nums)
#перебираем список и записываем переменные в три списка в зависимости от значения элемента
for num in nums:
    if num > 0:
        count_plus += 1
        plus.append(num)
    elif num < 0:
        count_minus += 1
        minus.append(num)
    elif num == 0:
        count_zero += 1
        zero.append(num)
#высчитываем процент чисел каждого списка относительно списка всех чисел
plus_percent = ((count_plus/len(nums))*100)
minus_percent = ((count_minus/len(nums))*100)
zero_percent = ((count_zero/len(nums))*100)

#выводим все данные, указанные в задании
print("Положительные числа: ", end = "")
for plus_nums in plus:
        print(plus_nums, end = " ")
print("\nКоличество положительных чисел: ", count_plus)
print(f"Процент положительных чисел в списке: {round(plus_percent, 2)}%")

print("Отрицательные числа: ", end = "")
for minus_nums in minus:
        print(minus_nums, end = " ")
print("\nКоличество отрицательных чисел: ", count_minus)
print(f"Процент отрицательных чисел в списке: {round(minus_percent, 2)}%")

print("числа, равные нулю: ", end = "")
for zero_nums in zero:
        print(zero_nums, end = " ")
print("\nКоличество чисел, равных нулю: ", count_zero)
print(f"Процент чисел, равных нулю в списке: {round(zero_percent, 2)}%")

print("Минимальное значение списка: ", min(nums))
print("Максимальное значение списка: ",max(nums))
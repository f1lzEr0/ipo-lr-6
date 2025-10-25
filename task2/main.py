#Kisel Artyom вариант3
import random
summ = 0
matrix = []
nums = [-3,-5,-2,-12,0,15,4,7,2]
#задаются рандомные значения столбцов и строк
column = random.randint(4,8)
rows = random.randint(4,8)
#цикл с заданием значений матрицы
for j in range(column):
#создаётся строка
    line = []
#в строку записываются рандомные значения из nums
    for i in range(rows):
        line.append(random.choice(nums))
#если мы заполнили строку, то записываем её в матрицу и переходим на следующюю строку
        if i == rows-1:
            matrix.append(line)
for i in matrix:
    for j in i:
        if j%3==0:
            summ +=j
        print(f"{j:3}", end =' ')
    print()
print(f"Сумма всех элементов кратных 3: {summ}")


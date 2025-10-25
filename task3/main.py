#Kisel Artyom
count_w = 0
list_with_strings = []
#задается количество строк, которое нужно ввести
count = int(input("Сколько строк вы хотитет ввести?: "))
#ввод заданного кол-ва строк
for i in range(count):
    string = input(f"{i+1} строка: ")
    list_with_strings.append(string)
#разбор списка со строками на строки
for string_in_list in list_with_strings:
#разбор строки на слова
    words = string_in_list.split()
    for word in words:
        count_w += 1
print("Количество слов: ", count_w)
#Kisel Artyom
strings_for_sort = []
#ввод искомого слова
find_str = input("Что вам нужно найти?: ")
#открытие файла
file1 = open("file.txt","r",encoding = "utf-8")
#перебор строк с проверкой на искомую строку и дальнейший вывод нужных строк
for string_of_file in file1:
    string = file1.readline()
    if find_str in string:
        strings_for_sort.append(string)
sorted_string = sorted(strings_for_sort)
for string in sorted_string:
    print(string)
#закрытие файла
file1.close()

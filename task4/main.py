#Kisel Artyom
#ввод искомого слова
find_str = input("Что вам нужно найти?: ")
#открытие файл
file1 = open("file.txt","r",encoding = "utf-8")
#перебор строк с проверкой на искомую строку и дальнейший вывод нужных строк
for string_of_file in file1:
    string = file1.readline()
    if find_str in string:
        print(string)
#закрытие файла
file1.close()

#2.Ввести произовльную строку в консоль.
#Циклом пройтись по всем символам этой строки
#Пропустить 3ий символ.
#Если есть символ "c" вывести сообщение об этом.
#Загуглить функцию вывода длины строки.
#Не выводить последний символ в строке.

name = input("введите слово: ")
last_name = name[:-1]
start = -1
str_name = " "
for x in range(0, len(last_name)):
    if x != 2:
        str_name = str_name + last_name[x]
print(str_name)
if name.find("с") >= 0:
    print("есть с")

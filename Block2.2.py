#Вводим 3 произвольных слова. Пусть будет название овощей.
#Выводим все 3 слова с нижнем регистре, в верхнем регистре, потом только первый сивол в верхний(есть отдельная функция для этого)
#Далее вводим кол-во каждого овоща.
#После чего с помощью метода format выводим все данные в читаемом виде.

vegetable1 = input("1 овощ: ")
vegetable2 = input("2 овощ: ")
vegetable3 = input("3 овощ: ")
vegl1 = vegetable1.lower()
vegl2 = vegetable2.lower()
vegl3 = vegetable3.lower()
vegu1 = vegetable1.upper()
vegu2 = vegetable2.upper()
vegu3 = vegetable3.upper()
vegt1 = vegetable1.title()
vegt2 = vegetable2.title()
vegt3 = vegetable3.title()
vegetables1 = int(input("сколько " + vegetable1 + ": "))
vegetables2 = int(input("сколько " + vegetable2 + ": "))
vegetables3 = int(input("сколько " + vegetable3 + ": "))
print("{} {} ({}, {})".format(vegetables1, vegl1, vegu1, vegt1))
print("{} {} ({}, {})".format(vegetables2, vegl2, vegu2, vegt2))
print("{} {} ({}, {})".format(vegetables3, vegl3, vegu3, vegt3))
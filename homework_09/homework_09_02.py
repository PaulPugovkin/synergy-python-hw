# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый.
# Все числа каждого списка находятся на отдельной строке.
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

list1 = set(input("Введите числа первого списка через пробел: ").split())
list2 = set(input("Введите числа второго списка через пробел: ").split())

commonNumbers = list1.intersection(list2)  # Находим пересечение множеств

count = len(commonNumbers)  # Получаем количество общих чисел

print("Количество чисел, содержащихся одновременно в обоих списках: ", count)

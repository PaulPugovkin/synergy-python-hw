# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.
#
# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
# В итоге, на вход программа получает например число 3,
# возвращает число 6 (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в убывающем порядке.
# Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1
#
# То есть, результирующий список будет выглядеть в нашем примере так:
#
# [720, 120, 24, 6, 2, 1]

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def factorialList(num):
    result = []
    while num >= 1:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        result.append(fact)
        num -= 1
    return result


# Пример использования функции factorial_list
num = int(input("Введите натуральное число: "))
result = factorialList(factorial(num))
print("Факториал числа {}: {}".format(num, factorial(num)))
print("Список факториалов: ", result)

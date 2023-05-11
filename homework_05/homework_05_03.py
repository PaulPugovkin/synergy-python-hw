# Два инвестора - Майкл и Иван хотят вложиться в стартап.
# Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно.
# У Майкла A долларов, у Ивана B долларов.
# Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan,
# если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

minInvestSum = int(input("Минимальная сумма инвестиций: "))
mikeSum = int(input("Сумма у Майкла: "))
ivanSum = int(input("Сумма у Ивана: "))

if (mikeSum >= minInvestSum) and (ivanSum >= minInvestSum):
    print(2)
elif (mikeSum >= minInvestSum):
    print("Mike")
elif (ivanSum >= minInvestSum):
    print("Ivan")
elif (mikeSum+ivanSum >= minInvestSum):
    print(1)
else:
    print(0)
# Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
# Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, его возраст и кличку,
# а потом выведет все эти данные в одно предложение. Например:

# Это желторотый питон по кличке "Каа". Возраст: 34 года.

print("Введите данные питомца:")
animal = input("Животное: ")
name = input("Кличка: ")
age = input("Возраст: ")
print(f'Это {animal} по кличке {name}. Возраст: {age}')
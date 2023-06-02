# Ранее вы выполняли задание связанное с ветеринарной клиникой.
# той задаче вам предстояло вывести информацию о питомце на экран.
# Сейчас вам необходимо создать словарь pets = {}
#
# Примерный вид будет следующим:
#
# pets = {
#   "Имя питомца": {
#     'Вид питомца': # придумайте каким образом сюда внести информацию,
#     'Возраст питомца': # придумайте каким образом сюда внести информацию,
#     'Имя владельца': # придумайте каким образом сюда внести информацию
#   }
# }
#
# У вас должен получиться словарь, с ещё одним словарём внутри.
# То есть, есть словарь pets. Он в себе хранит ещё один словарь, который обозначается именем питомца.
# Имя питомца также нужно каким-то образом вносить туда.
#
# Задача не будет считаться выполненной, если вы заходите сразу внести информацию, не прибегая в функции input()
#
# Например:
#
# pets = {
#
#   "Мухтар": {
#
#     "Вид питомца": "Собака",
#
#     "Возраст питомца": 9,
#
#     "Имя владельца": "Павел"
#
#   }
#
# }
#
# Так должен будет выглядеть результируюший словарь, но первоначальный его вид - пустой.
# Его необходимо заполнить пользовательским вводом через консоль с помощью функции input(),
# а не вписать значения уже в самом коде.
#
# Возраст питомца должен быть типа int Всё остальное - строки
#
# Так как возраст питомца указывается типом int.
# Необходимо, в соответствии с указанным возрастом выводит год, года или лет. Например:
#
# Его возраст: 24 года
#
# Его возраст: 21 год
#
# Его возраст: 19 лет
#
# И теперь осталось только получить всю информацию о питомце в виде строки, как из задания по Урок №3.
# Ввод-вывод и базовые переменные. Задание №1, но с небольшими изменениями.
# Для получения информации необходимо воспользоваться методами словаря keys() и values():
#
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша

def checkAge(age):
    if (age > 4) and (age < 21):
        return f'{age} лет'
    else:
        i = age % 10
        if i==1:
            return f'{age} год'
        elif i < 5:
            return f'{age} года'
        else:
            return f'{age} лет'

pet = {}

petName = input("Введите кличку питомца: ")
typeOfPet = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
ownerName = input("Введите имя владельца: ")

if (petName and typeOfPet and age and ownerName):
    pet[petName] = {
        "Вид питомца": typeOfPet,
        "Возраст питомца": checkAge(age),
        "Владелец питомца": ownerName
    }
    print(pet)
else:
    print("Incorrect input values, try again")

# В Урок №10. Задание №1 вы создавали словарь с информацией о питомце.
# Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
#
# Подробный требуемый функционал будет ниже. Пока что справка:
#
# Создайте функцию create
# Создайте функцию read
# Создайте функцию update
# Создайте функцию delete
# Используйте словарь pets, который будет предоставлен ниже, либо создайте свой аналогичный
# Функция create:
#
# Данная функция будет создавать новую запись с информацией о питомце и добавлять эту информацию в наш словарь pets
#
# Функция read
#
# Данная функция будет отображать информацию о запрашиваемом питомце в виде:
#
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
#
# Функция update
#
# Данная функция будет обновлять информацию об указанном питомце
#
# Функция delete
#
# Данная функция будет удалять запись о существующем питомце
#
# Структруа результирующего словаря pets будет как и в Урок №10. Задание №1, но с небольшим видоизменением:
#
# Словарь pets
#
# pets = {
#     1:
#         {
#             "Мухтар": {
#                 "Вид питомца": "Собака",
#                 "Возраст питомца": 9,
#                 "Имя владельца": "Павел"
#             },
#         },
#     2:
#         {
#             "Каа": {
#                 "Вид питомца": "желторотый питон",
#                 "Возраст питомца": 19,
#                 "Имя владельца": "Саша"
#             },
#         },
#
# и так далее
#
# }

# Здесь, 1 и 2 - это идентификаторы наших питомцев.
# Это уникальные ключи, по которым мы сможем обращаться к нашим записям в "базе данных"
#
# Суть будущей программы будет заключаться в следующем:
#
# Программа будет работать с помощью цикла while с условием command != 'stop',
# то есть до тех пор, пока на предложение ввести команду, пользователь не введёт слово stop
# Перед взаимодействием с "базой данных" запрашивается одна из команд в качестве пользовательского ввода.
# Пусть это будет переменная command
# Функция create должна добавлять новую информацию таким образом, чтобы идентификатор увеличивался на единицу.
# Чтобы у вас была возможность получать последний ключ в словаре воспользуйтесь импортом модуля collections.
# В начале вашей программы пропишите строчку: import collection, а в функции create в первых строках пропишите следующий код:

# def create():
# last = collections.deque(pets, maxlen=1)[0]
#
# last в данном случае и будет число последнего ключа (или в нашей логике - идентификатора записи).
# Именно его и необходимо будет увеличивать на единицу при добавлении следующей записи.
# Как вам уже известно - суть функций заключается в том, чтобы использовать один и тот же код в нескольких местах.
# В данной задаче вам предстоит получать информацию о питомце несколько раз.
# Чтобы не повторяться в коде, вам нужно создать такие функции
#
# get_pet(ID):
#
# def get_pet(ID):

# функция, с помощью которой вы получите информацию о питомце в виде словаря

# сделайте проверку, если питомца с таким ID нету в нашей "базе данных"

# верните в этом случае False

# а если питомец всё же есть в "базе данных" - верните информацию о нём

# выглядеть это может примерно так:
#
# return pets[ID] if ID in pets.keys() else False
#
# get_suffix(age):
#
# def get_suffix(age):

# функция, с помощью которой можно получить суффикс

# 'год', 'года', 'лет'

# реализацию этой функции вам предстоит придумать самостоятельно

# функция будет возвращать соответствующую строку

# return

# pets_list():

# def pets_list():

# Эта функция будет создана для удобства отображения всего списка питомцев

# Информацию по каждому питомцу можно вывести с помощью цикла for

# Обратите внимание, если ID не существует в словаре с питомцами - будет возникать ошибка.
# Вам можно от неё избавиться, если правильно составить проверочное условие.
# Здесь не потребуется использовать такие конструкции, как try, except, чтобы обработать возникшую ошибку

import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}


def checkAge(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age // 10) % 10 != 1:
        return "года"
    else:
        return "лет"

def create():
    last = collections.deque(pets, maxlen=1)[0]
    newId = last + 1

    petName = input("Введите имя питомца: ")
    petType = input("Введите вид питомца: ")
    petAge = int(input("Введите возраст питомца: "))
    ownerName = input("Введите имя владельца: ")

    pets[newId] = {
        petName: {
            "Вид питомца": petType,
            "Возраст питомца": petAge,
            "Имя владельца": ownerName
        }
    }
    print('Pet successfully added to dict')

def getPet(petId):
    return pets.get(petId, False)

def read(petId):
    pet_info = getPet(petId)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        pet_type = pet_info[pet_name]["Вид питомца"]
        pet_age = pet_info[pet_name]["Возраст питомца"]
        owner_name = pet_info[pet_name]["Имя владельца"]
        suffix = checkAge(pet_age)

        print("Это {} по кличке \"{}\". Возраст питомца: {} {}. Имя владельца: {}".format(
            pet_type, pet_name, pet_age, suffix, owner_name))
    else:
        print("Питомец с ID {} не найден.".format(petId))


def update(petId):
    petInfo = getPet(petId)
    if petInfo:
        petName = list(petInfo.keys())[0]
        petType = petInfo[petName]["Вид питомца"]
        petAge = petInfo[petName]["Возраст питомца"]
        ownerName = petInfo[petName]["Имя владельца"]
        suffix = checkAge(petAge)

        print("Информация о питомце:")
        print("ID: {}".format(petId))
        print("Имя питомца: {}".format(petName))
        print("Вид питомца: {}".format(petType))
        print("Возраст питомца: {} {}".format(petAge, suffix))
        print("Имя владельца: {}".format(ownerName))

        newPetName = input("Введите новое имя питомца (оставьте пустым для сохранения текущего имени): ")
        newPetType = input("Введите новый вид питомца (оставьте пустым для сохранения текущего вида): ")
        newPetAge = input("Введите новый возраст питомца (оставьте пустым для сохранения текущего возраста): ")
        newOwnerName = input("Введите новое имя владельца (оставьте пустым для сохранения текущего имени): ")

        if newPetName:
            petInfo[newPetName] = petInfo.pop(petName)

        if newPetType:
            petInfo[petName]["Вид питомца"] = newPetType

        if newPetAge:
            petInfo[petName]["Возраст питомца"] = int(newPetAge)

        if newOwnerName:
            petInfo[petName]["Имя владельца"] = newOwnerName

        print("Информация о питомце после обновления:")
        print("ID: {}".format(petId))
        print("Имя питомца: {}".format(petName))
        print("Вид питомца: {}".format(petInfo[petName]["Вид питомца"]))
        print("Возраст питомца: {} {}".format(petInfo[petName]["Возраст питомца"], suffix))
        print("Имя владельца: {}".format(petInfo[petName]["Имя владельца"]))
    else:
        print("Питомец с ID {} не найден.".format(petId))


def delete(petId):
    petInfo = getPet(petId)
    if petInfo:
        petName = list(petInfo.keys())[0]
        del pets[petId]
        print("Запись о питомце с ID {} и именем \"{}\" удалена.".format(petId, petName))
    else:
        print("Питомец с ID {} не найден.".format(petId))


def petList():
    for ID, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        pet_type = pet_info[pet_name]["Вид питомца"]
        pet_age = pet_info[pet_name]["Возраст питомца"]
        owner_name = pet_info[pet_name]["Имя владельца"]
        suffix = checkAge(pet_age)

        print("ID: {}".format(ID))
        print("Имя питомца: {}".format(pet_name))
        print("Вид питомца: {}".format(pet_type))
        print("Возраст питомца: {} {}".format(pet_age, suffix))
        print("Имя владельца: {}".format(owner_name))
        print()


command = ""

while command != 'stop':
    command = input("Enter command (stop, create, read, update, delete, list): ")
    if (command == 'create'):
        create()
    elif (command == 'read'):
        petId = int(input('Enter pet id: '))
        read(petId)
    elif (command == 'update'):
        update()
    elif (command == 'delete'):
        petIdToDelete = int(input("Id to delete: "))
        delete(petIdToDelete)
    elif (command == 'list'):
        petList()
    elif (command == ''):
        command = input("Enter command: ")
    elif (command == 'stop'):
        print("Goodbye, see you later!")
    else:
        print("Incorrect command. Available commands: stop, create, read, update, delete, list")

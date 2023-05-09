# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить, что тоже очень важно для программиста.)
# и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому.
# В следующих уроках мы дополним эту форму до полноценного теста, который будет проверять правильность ответов, а пока - начнем с малого.
# Напоминаем, что разделить эти данные тебе поможет команда sep внутри команды print, например, чтобы разделить переменные знаком + нужно ввести:
#
# print(a1, a2, a3, sep='+')
#
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

evolutionList = "Dryopithecus=>Ramapithecus=>Australopithecus=>Homo Erectus=>Homo Sapiens Neanderthalensis=>" \
                "Homo Sapiens Sapiens"

firstStep = input("Enter first step of evolution: ")
secondStep = input("Enter second step of evolution: ")
thirdStep = input("Enter third step of evolution: ")
fourthStep = input("Enter fourth step of evolution: ")
fifthStep = input("Enter fifth step of evolution: ")
sixthStep = input("Enter sixth step of evolution: ")

print(firstStep, secondStep, thirdStep, fourthStep, fifthStep, sixthStep, sep=" => ")
print("Correct answer: ", evolutionList)

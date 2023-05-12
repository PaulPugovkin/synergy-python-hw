# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
# Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков
# В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка.
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
# В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
# Программа должна вывести одно число - минимальное количество лодок,
# необходимое для переправки всех рыбаков на противоположный берег.

fishermanCount = int(input("Количество рыбаков: "))
fishermanWeight = []
maxBoatCapability = int(input("Максимальная нагрузка в лодке: "))
boatCount = 0
fishermanWhoCant = 0

if (fishermanCount > 0):
    for i in range(fishermanCount):
        fishermanWeight.append(int(input(f"Введите вес {i + 1} рыбака: ")))
    for i in range(fishermanCount - 1):
        if (fishermanWeight[i] + fishermanWeight[i + 1] <= maxBoatCapability):
            boatCount += 1
            i += 1
        elif (fishermanWeight[i] <= maxBoatCapability):
            boatCount += 1
        else:
            fishermanWhoCant += 1

print(f"Необходимо {boatCount} лодки, чтобы переправить {fishermanCount - fishermanWhoCant} путешественников")
if (fishermanWhoCant > 0):
    print(f"Количество путешественников, которые не могут переправится: {fishermanWhoCant} (лодка не вмещает такой вес)")


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

    fishermanWeight.sort()

    left = 0
    right = fishermanCount - 1

    while left <= right:
        if (fishermanWeight[left] + fishermanWeight[right] <= maxBoatCapability):
            left += 1
            right -= 1
        else:
            right -= 1
        boatCount += 1

print(f"Необходимо {boatCount} лодки, чтобы переправить {fishermanCount} путешественников")

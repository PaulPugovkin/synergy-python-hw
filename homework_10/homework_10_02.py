# С помощью цикла создайте словарь, в котором ключи будут, например от числа 10, до -5 (включительно).
# А значениями этих ключей будут сами эти числа возведённые в степени равных этим числам
#
# Например:
#
# my_dict = {
#   10: 10000000000,
#   9: 387420489,
#   # и так далее ...
#   -5: -0.00032
# }

numDict = {}
for num in range(10, -6, -1):
    numDict[num] = num ** num
print(numDict)
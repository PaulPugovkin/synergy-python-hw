# Во входную строку водится последовательность чисел через пробел.
# Для каждого числа выведите слово ”YES” (в отдельной строке),
# если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

numbers = input("Введите последовательность чисел через пробел: ").split()
seenNumbers = set()

for number in numbers:
    if number in seenNumbers:
        print("YES")
    else:
        print("NO")
        seenNumbers.add(number)

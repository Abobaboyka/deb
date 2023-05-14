python
import random

# Создание списка случайных чисел
numbers = []
for _ in range(100):
    numbers.append(random.randint(1, 100))

# Вывод суммы всех чисел в списке
sum = 0
for num in numbers:
    sum += num
print("Сумма чисел:", sum)

# Вывод отдельно четных и нечетных чисел
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)

# Поиск наибольшего и наименьшего чисел
max_number = max(numbers)
min_number = min(numbers)
print("Наибольшее число:", max_number)
print("Наименьшее число:", min_number)

# Сортировка чисел по возрастанию
sorted_numbers = sorted(numbers)
print("Отсортированные числа:", sorted_numbers)

# Поиск числа, ближайшего к среднему значению
average = sum / len(numbers)
closest_number = min(numbers, key=lambda x: abs(x - average))
print("Число, ближайшее к среднему:", closest_number)

# Генерация случайной строки
def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for _ in range(length):
        result += random.choice(letters)
    return result

random_string = generate_random_string(10)
print("Случайная строка:", random_string)

# Подсчет количества гласных и согласных букв в строке
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
string = "hello world"
vowel_count = 0
consonant_count = 0
for char in string:
    if char.lower() in vowels:
        vowel_count += 1
    elif char.lower() in consonants:
        consonant_count += 1
print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

# Генерация случайного списка букв
letters = "abcdefghijklmnopqrstuvwxyz"
random_letters = random.choices(letters, k=10)
print("Случайный список букв:", random_letters)

# Пример функции с рекурсией
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Факториал числа 5:", result)

# Завершение программы
print("Программа завершена.")

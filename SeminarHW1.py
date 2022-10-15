# 1

# day = int(input('Enter day number: '))
# if day > 7 or day < 1:
#     print('Please, repeat the input')
# elif day == 6 or day == 7:
#     print("Yes, it's weekend!")
# else:
#     print("No, it's not weekend!")

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))
#
# a = x * y * z
# b = x + y + z
#
# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 1
# elif b < 1:
#     b = 1
#
# if a == b:
#     print('Утверждение истинно')
# elif a != b:
#     print('Утверждение ложно')
#
# leftSide = not (x or y or z)
# rightSide = not x and not y and not z
# result = leftSide == rightSide
#
# if result == True:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите число x≠0:'))
# y = int(input('Введите число y≠0:'))
#
#
# if x == 0 and y == 0:
#     print('Вы не услышали условия поэтому Вы находитесь в начале начал ;)')
# elif x > 0 and y > 0:
#     print(
#         f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
# elif x < 0 and y > 0:
#     print(
#         f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
# elif x < 0 and y < 0:
#     print(
#         f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
# elif x > 0 and y < 0:
#     print(
#         f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')

# 4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('input quarter number: '))
# if n < 1 or n > 4:
#     print('Please, repeat the input')
# elif n == 1:
#     print('x > 0 and y > 0')
# elif n == 2:
#     print('x < 0 and y > 0')
# elif n == 3:
#     print('x < 0 and y < 0')
# elif n == 4:
#     print('x > 0 and y < 0')

# 5 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# def input_numbers(x):
#     xy = ["X", "Y"]
#     a = []
#     for i in range(x):
#         reality = False
#         while not reality:
#             try:
#                 number = int(input(f"Введите координату {xy[i]}: "))
#                 a.append(number)
#                 reality = True
#             except ValueError:
#                 print("Не тот цифра, что после запятой идет. Цифра тот, что без запятых")
#     return a
#
#
# def Length(a, b):
#     lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return lengthSegment
#
#
# print("Введите координаты точки А")
# pointA = input_numbers(2)
# print("Введите координаты точки В")
# pointB = input_numbers(2)
#
# print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")
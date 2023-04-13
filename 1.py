# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения.
# Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов
# в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

# * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.

first_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
second_list = [1, 21, 3, 4, 5, 6, 7, 8, 9, 2]

def difference(list_1, list_2):
    try:
        difference_list = list(map(lambda a, b: a - b, list_1, list_2))
        print("Разности элементов двух входящих массивов:")
        print(difference_list)
    except TypeError:
        print("В массиве есть нечисловые элементы")
    finally:
        if len(list_1) == len(list_2):
            print('Длинна массивов равна')
        else:
            print(f"Длинна массивов НЕ равна, Первый = {len(list_1)},"
                  f" Второй = {len(list_2)}")


def division(list_1, list_2):
    try:
        division_list = list(map(lambda a, b: a // b, list_1, list_2))
        print("Частное элементов двух входящих массивов")
        print(division_list)
    except TypeError:
        print("В массиве есть нечисловые элементы")
    finally:
        if len(list_1) == len(list_2):
            print('Длинна массивов равна')
        else: print(f"Длинна массивов НЕ равна, Первый = {len(list_1)},"
                    f" Второй = {len(list_2)}")


difference(first_list, second_list)
print()
division(first_list, second_list)



# SyntaxError
# dec func_1():
#     pass

# NameError
# print(x)

# TypeError
# new_list = [1,2,3]
# [print(new_list + 1)]

# IndexError
# new_list = [1,2,3]
# print(new_list[3])

#ValueError
# print(int("one"))

# KeyError
# new_dict = {1 : 'orange', 2: 'banana'}
# print(new_dict[3])

# AttributeError
# "string".append()
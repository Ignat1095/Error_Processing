# 1. Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение.
# Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.
#
# 2. Если необходимо, исправьте данный код (задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)
#   2.1 Дан следующий код, исправьте его там, где требуется (задание 3 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)
#   2.2 Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. Пользователю должно показаться сообщение, что пустые строки вводить нельзя.


        # Задание 1
def float():
    try:
        print(int(input("input number: ")))
    except ValueError:
        print("Надо вводить число!")
    finally:
        print()
        float()


        # Задание 2.1
def tusk_2_1(divider):
    my_list = [i for i in range(0, 20, 3)]
    try:
        d = divider
        print(f"Делитель = {d}")
        print(f"my_list = {my_list}")
        catched_result = [i/d for i in my_list]
        print(catched_result)

    except ZeroDivisionError:
        print("На ноль делить нельзя! ")

    except ArithmeticError:
        print("Неверный делитель")
    except TypeError:
        print("Делитель должен быть числом")
    finally:
        print("\n"*1)


        # Задание 2.2
def tusk_2_2():
    try:
        a = 90
        b = 3
        print(a / b)

        print_sum(23, 123.1)

        abc = [1, 2]
        abc[3] = 9
        print(abc)
    except ZeroDivisionError:
        print(f"{a}/{b} На ноль делить нельзя")

    except IndexError:
        print("(abc) Массив выходит за пределы своего размера!")

def print_sum(a, b):
    try:
        print(f"print_sum = {a + b}")
    except TypeError:
        print("В функции (print_sum) должны быть указаны только числа")







# float()

# tusk_2_1(1/2)
# tusk_2_1(0)
# tusk_2_1("null")

# tusk_2_2()

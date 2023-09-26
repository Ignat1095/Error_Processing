from typing import Dict, Any, List


def information() -> dict[Any, list[list[str] | Any]]:
    data = input("Введите свои данные через пробел как в примере:\n"
                 "Иванов Иван Иванович дату рождения(01.01.2001) тел(89211234567) пол(f/m)\n:").split(' ')
    result = {}
    if len(data) != 6:
        print(f"Вы забыли что-то указать\n:{data}\n")
        information()
    f_name = data[0]

    fio = list(map(str, data[:3]))
    if len(fio) != 3:
        print("Надо написать фамилию имя отчество!")
        return information()

    b_day = data[3]

    number = data[4]
    if len(number) != 11:
        print(f"В номере 11 цифр, вы ввели: {data[4]}")
        return information()

    if data[5] not in ['f', 'm']:
        print('Надо указать "f" или "m"!')
        return information()
    else:
        sex = data[5]

    result[f_name] = [fio, b_day, number, sex]
    return result


data_dict = {}
while True:

    for key, value in information().items():

        data_dict[key] = value
        if key in data_dict.keys():
# todo
            print(data_dict)
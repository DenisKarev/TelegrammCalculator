import logger as log


def menu_check(val: str) -> str:
    if val.isdigit():
        if len(val) > 1:
            return ' '
        return val
    return ' '


def digit_check(a):  # проверяет является ли введенные данные числом и если нет просит ввести еще раз пока не получит число
    while not float_check(a):
        print("упс, это не число")
        log.write_log(f" !!error typ!!")
        a = input(f"Введите число: ")
        log.write_log(f", input: {a}")
    return float(a)


def float_check(s):  # обрботка ошибок если не число возвращает лож
    try:
        float(s)
        return True
    except ValueError:
        return False

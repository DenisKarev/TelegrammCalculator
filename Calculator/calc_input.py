from cheks import menu_check, digit_check
import logger as log


def menu_inp(val: str) -> int:
    # ars#  что принимает эта функция, стороку ? что должно прийти?
    # den# да она принимает строку, права в контроллре не совсем правильные цифры
    # в интерфейсе можнов коментах посмотреть правильные
    """ Меню верхнего уровня """
    res = ' '
    while res not in val:                           # Сравниваем со строкой которая пришла в вызове
        # Причем тут проверка (menu_check) уже вроде как уже не нужна
        res = menu_check(input('Введите выбор: '))
    else:
        return int(res)


def real_inp():
    a = input(f"Введите рациональное число: ")  # запрос числа
    log.write_log(f", input: {a}")  # отправка в логер что введи
    # проаерка является ли введенное числом, если нет спрашивает  повтороно пока не дождется числа
    a = digit_check(a)
    if a % 1 == 0:# проверка если введенное число не дробное присваивается инт
        a = int(a)
    return a


def complex_inp() -> complex:
    print()
    temp1_comp = input(
        f"Введите действительную часть комплексного числа: ")  # запрос числа
    log.write_log(f", input: {temp1_comp}")  # отправка в логер что введи
    # проаерка является ли введенное числом, если нет спрашивает  повтороно пока не дождется числа
    temp1_comp = digit_check(temp1_comp)
    temp2_comp = input(f"Введите действительную часть комплексного числа: ")
    log.write_log(f", input: {temp2_comp}")
    temp2_comp = digit_check(temp2_comp)

    return complex(temp1_comp, temp2_comp)

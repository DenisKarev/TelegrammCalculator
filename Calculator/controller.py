from user_interface import *
from calc_input import menu_inp, real_inp, complex_inp
import model_sum as sum
import model_sub as sub
import model_mult as mult
import model_div as div
import model_pow as pow
import model_mod as rem
import model_div_ as div_
import model_sqrt as sqrt
import logger as log


def user_num(start: int):               # ars# для понимания
    if start == 1:                      # что запрашиваем используем переменную
        return real_inp()               # цифра берется из выбора первого меню
    elif start == 2:
        return complex_inp()            # если 1 то рациональные если 2 то комплексные
    elif start == 0:
        exit()


def run():
    while True:
        draw_menu_start()
        in_run = menu_inp('012')                # первое меню
        if in_run == 1:
            log.write_log("\noperation steps: 1")
            draw_menu_real()                    # меню реальных чисел # возможный выбор 012345678
            in_start = menu_inp('012345678')
            operation(in_run, in_start)
        elif in_run == 2:
            log.write_log("\noperation steps: 2")
            draw_menu_complex()                 # меню комплексных чисел # возможный выбор 0123456
            in_start = menu_inp('0123456')
            operation(in_run, in_start)
        else:
            log.write_log("\n!exit!")
            exit()


def operation_2num(tip_num: int, oper, znak):
    num1 = user_num(tip_num)  # запрашиваем 1е число
    num2 = user_num(tip_num)  # запрашиваем 2е число
    result = oper.init(num1, num2)  # фиксируем результат
    log.logger(num1, znak, result, num2)  # отправляем в логер
    return result


def operation_1num(tip_num: int, oper, znak):
    num1 = user_num(tip_num)  # запрашиваем 1е число
    log.write_log(f"input: {num1}, ")
    result = oper.init(num1)  # фиксируем результат
    log.logger(num1, znak, result)  # отправляем в логер
    return result


def operation(tip_num: int, tip_oper: int):
    if tip_oper == 1:  # Отрисовывается результать сложения первого и второго числа для обоих случиев
        log.write_log(f", 1")
        draw_result(operation_2num(tip_num, sum, "+"))  # выводим результат
    elif tip_oper == 2:  # Отрисовывается результать вычитания второго из первого числа для обоих случиев
        log.write_log(f", 2")
        draw_result(operation_2num(tip_num, sub, "-"))
    elif tip_oper == 3:  # Отрисовывается результать перемножения первого и второго числа для обоих случиев
        log.write_log(f", 3")
        draw_result(operation_2num(tip_num, mult, "*"))
    elif tip_oper == 4:  # Отрисовывается результать деления
        log.write_log(f", 4")
        draw_result(operation_2num(tip_num, div, "/"))  # модуль деления
    elif tip_oper == 5:
        if tip_num == 1:
            # модуль целочисленного деления #
            log.write_log(f", 5")
            draw_result(operation_2num(tip_num, div_, "//"))
        else:
            # модуль возведения в степень #
            log.write_log(f", 5")
            draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 6:
        if tip_num == 1:
            # модуль остатка от деления #
            log.write_log(f", 6")
            draw_result(operation_2num(tip_num, rem, "%"))
        else:
            # модуль квадратного корня #
            log.write_log(f", 6")
            draw_result(operation_1num(tip_num, sqrt, "sqrt"))
    elif tip_oper == 7:
        # модуль возведения в сепень #
        log.write_log(f", 7")
        draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 8:
        # модуль квадратного корня #
        log.write_log(f", 8")
        draw_result(operation_1num(tip_num, sqrt, "sqrt"))
    elif tip_oper == 0:         # переход в предыдущие меню
        log.write_log(f", 0")
        run()

# Calculator status WiP
| person              | to do               |   status |   done   |  есть изменения для внесения     |
|---|---|---|---|---|
| Анна Толстова       | complex.py          |   | X |   |
| Арсений Беляев aza  | conroller.py        |   | v |   |
| Ирина Боярчукова    |                     |   |   |   |
| Анна Орлова         |                     |   |   |   |
| Вадим Борзиков      |                     |   |   |   |
| Денис aka Goofy     | user_interface.py   |   | X |   |
## main.py
    calls controller (.py)
нашел пустую строчку чтобы залетело без проблем
# нужны добровольци на разработку модулей математических оперкаций, звучит страшно но не очень) надо создать фаил и описать в нем метод который принимает 1 или 2 числа и производит математическую операцию с ним и возвращает результат. все готово)))
## controller.
    num1: float
    num2: float

    com1: Complex(n1, n2)
    com2: Complex(n3, n4)
    1. call user_interface

## user_interface.py    view —> тупо отрисовка менюх?
    draw_start_menu()
    draw_real_menu()
    draw_complex_menu()

### except.py —> Обработка исключений
#    отсутствует как класс?

## calc_input.py
    1. input_complex
    2. input_real

## model_ * модули для каждой орерации

```
+        sum
-       minus
*       mult
/       div
//      div_
%       mod
**      pow
sqrt    sqrt

## complex.py —> Работа с Комплексными числами
вызов возможных из модулей работы с рациональными?
    1. sum
    2. minus
    3. multiply
    4. division
    5. power
    6. sqrt

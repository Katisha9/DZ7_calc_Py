import view                                                 # импорт основных модулей
import model
import parser

def input_first():                                          # Получаем и задаем первое число/выражение
    number = view.input_number()
    if number.isdigit():
        number = int(number)
        model.set_first(number)
    else:
        model.set_expression(number)
        parser.parser(number)

def input_second():                                         # Получаем и задаем второе число
    while True:
        number = int(view.input_number())
        if model.get_operation() == '/' and number == 0:    # Проверка деления на ноль
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break


def input_operation():                                      # Получение и присвоение операции
    oper = view.input_operation()
    model.set_operation(oper)


def solution():                                             # Прозводим вычисления
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)                   # Вывод на печать
    model.set_first(model.get_result())                    # Результат стал первым числом для следующих вычислений
    return False


def start():                                               # Калькулятор (старт с обработчиком "=")
    input_first()
    if not model.get_exression():
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
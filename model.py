first_number = 0                # первое число/выражение
second_number = 0               # второе число
operation = ''                  # строковая переменная для математических оперций
result = 0
expression = ''                 # строковая переменная для выражения

def get_first():                        # задаем геттеры  для чисел, операций и результата
    global first_number
    return first_number


def get_second():
    global second_number
    return second_number


def get_operation():
    global operation
    return operation


def get_result():
    global result
    return result

def get_exression():
    global expression
    return expression

def set_first(value):                   # задаем cеттеры для чисел, выражения и операций
    global first_number
    first_number = value

def set_expression(exp):
    global expression
    expression = exp

def set_second(value):
    global second_number
    second_number = value


def set_operation(oper):
    global operation
    operation = oper


def addition():                         # создаем методы для выполения операций +, -, *, /
    global first_number
    global second_number
    global result
    result = first_number + second_number


def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number


def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number


def division():
    global first_number
    global second_number
    global result
    result = first_number / second_number
    if result == int(result):
        result = int(result)
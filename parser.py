def parser(string):                                     # функция для парсера и вычисления
    expression_list = string.split()
    for i in range(len(expression_list)):
        if expression_list[i].isdigit():
            expression_list[i] = int(expression_list[i])
    result = 0
    while len(expression_list) != 1:
        i = 0
        while ('*' in expression_list or '/' in expression_list) and i < len(expression_list):
            if expression_list[i] == '*':
                result = expression_list[i - 1] * expression_list[i + 1]
                expression_list.pop(i)
                expression_list.pop(i)
                expression_list[i - 1] = result
            elif expression_list[i] == '/':
                result = expression_list[i - 1] / expression_list[i + 1]
                expression_list.pop(i)
                expression_list.pop(i)
                expression_list[i - 1] = result
            else:
                i += 1

        while ('+' in expression_list or '-' in expression_list) and i < len(expression_list):
            if expression_list[i] == '+':
                result = expression_list[i - 1] + expression_list[i + 1]
                expression_list.pop(i)
                expression_list.pop(i)
                expression_list[i - 1] = result
                i -= 1
            elif expression_list[i] == '-':
                result = expression_list[i - 1] - expression_list[i + 1]
                expression_list.pop(i)
                expression_list.pop(i)
                expression_list[i - 1] = result
                i -= 1
            else:
                i += 1
    print(f'Ответ: {result}')
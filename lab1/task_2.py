from validation import validateInput


def returnMaxOrZero(a, b):
    if a == b:
        return 0
    return max(a, b)


def task2():

    a = validateInput(int, 'Ведіть ціле значення числа a: ',
                      'Неправильлий формат числа a')
    b = validateInput(int, 'Введіть ціле значення числа b: ',
                      'Неправильлий формат числа b')

    print(f'Введені значення: a = {a}, b = {b}')

    c = returnMaxOrZero(a, b)
    a = c
    b = c
    print(f'Отримані значення: a = {a}, b = {b}')

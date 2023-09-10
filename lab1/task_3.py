from validation import validateInput


def task3():

    x = validateInput(float, "Введіть значення x: ", "Дані не підходять")
    if x <= 7:
        number = 3*x-9
    else:
        number = f'{(1/((x^2)-4)):.4}'
    print('Результат обчислення функції: ', number)

from validation import validateInput


def task2():
    N = validateInput(int, "Введіть значення числа N: ", "Дані не підходять!")
    i = 1
    result = ""

    while i * i <= N:
        result += f"{i * i} "
        i += 1
    if result == "":
        print("Число не натуральне.")
    else:
        print("Всі квадрати натуральних чисел, які не перевищують числа N: ")
        print(result)

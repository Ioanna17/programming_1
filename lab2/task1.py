from validation import validateInput


def task1():
    print("Умова: sum (x-i)/i^2, i=1 to n ")
    n = validateInput(int, "Введіть значення n: ", "Дані не підходять!")
    x = validateInput(float, "Введіть значення x: ", "Дані не підходять!")
    result = 0

    for i in range(1, n+1):
        result += (x - i) / (i ** 2)

    print(f'Відповідь: {result:.3f}')

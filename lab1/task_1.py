from validation import validateInput


def task1():
    temperature = validateInput(
        int, "Введіть температуру в градусах Цельсія: ", "Дані не підходять")
    print(f'Температура в градусах Фаренгейта: {(temperature*1.8+32):.3f}')

from task1 import task1
from task2 import task2
print("Лабораторна робота №2, Варіант 6\nСтудентки Васильчук Іванни, КМ-33\nТема: Програмування циклічних алгоритмів.")
while True:
    choice = input("Введіть номер завдання(1-2): ")
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    else:
        break

from task_1 import task1
from task_2 import task2
from task_3 import task3
while True:
    choice = input("Введіть номер завдання(1-3): ")
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    else:
        break

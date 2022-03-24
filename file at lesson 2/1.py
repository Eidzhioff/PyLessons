a = input("Введите первое число: ")
b = input("Введите второе число: ")
com=input("Введите действие: ")
try:
    a = int(a)
    b = int(b)
    if com == "+":
        print(a+b)
    elif com == "-":
        print(a-b)
    elif com == "/":
        if b == 0:
            print("Ошибка деления на ноль")
        else:
            print(a % b)
except ValueError:
    print("Ошибка преобразования типов")

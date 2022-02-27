import random
n = random.randint(1,10)
while True:
    chislo=input("Введите число: ")
    if int(chislo) == n:
        print("Верно")
        break
    elif int(chislo) > n:
        print("Вы загодали число больше нужного")
    else:
        print("Вы загодали число меньше нужного")

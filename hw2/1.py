print("Идет ли у вас дождь?")
x = input().lower()
if x == "yes":
    print("Ветрино ли на улице?")
    y = input().lower()
    if y == "yes":
        print("Слишком ветрено для зонтика")
    else:
        print("Возьми зонтик")
elif x == "no":
    print("Хорошего вам дня")

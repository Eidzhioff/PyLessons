print("Введите ваше имя")
s = input()
if len(s)<5:
    print("Теперь введите вашу фамилию")
    s1 = input()
    s2 = s + ' ' + s1
    print(s2.upper())
else:
    print(s.lower())

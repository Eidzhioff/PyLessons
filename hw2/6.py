import math
print("Введите фигуру площадь которой хотите вычелить")
ktp = input().lower()
if ktp == "круг":
    print("Введите радиус")
    radius = float(input())
    sk = 3.14 * (radius ** 2)
    print("Площадь круга:", sk)
elif ktp == "треугольник":
    print("Введите длины его сторон")
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    y = p*(p-a)*(p-b)*(p-c)
    st = math.sqrt(y)
    print("Площадь треугольника:", st)
else:
    print("Введите две стороны")
    a1 = float(input())
    b1 = float(input())
    sp = a1 * b1
    print("Площадь прямоуголька:",sp)

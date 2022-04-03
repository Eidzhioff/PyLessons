import re
txt = open("students.txt", "r", encoding="utf8")
lst = txt.read().split("\n")
sort=lst.sort()

def showlst():
    print(lst)

def addstud():
    student = input("Введите имя студента: ")
    if student in lst:
        print(student, "уже есть в списке")
    else:
        lst.append(student)
        lst.sort()
        print(student, "был добавлен(а)")


def showstud():
    surname=input("Введите фамилию: ")
    name=input("Введите имя или нет:")
    stud=surname+ " " + name
    if name == "нет":
        for i in lst:
            if surname in i:
                sur=re.findall(r'\w+', i)[0]
                if surname == sur:
                    print("Ученик с данной фамилией: ", i)
                else:
                    print( "Такого нет" )               
    else:
        if stud in lst:
            print("Студент находится в группе")
        else:
            print("Студент не находится в группе")

def editstud():
    surname=input("Введите фамилию: ")
    name=input("Введите имя:")
    stud=surname+ " " + name
    if stud in lst:
        for i in lst:
            if stud == i:
                print("Что вы хотите поменять?")
                print("Если хотите поменять имя напишите: имя")
                print("Если хотите поменять фамилию напишите: фамилия")
                print("Если хотите поменять все напишите: все")
                answer=input()
                if answer == "имя":
                    new_name=input("Введите новое имя:")
                    lst.remove(stud)
                    app=surname + " " + new_name
                    lst.append(app)
                    lst.sort()
                    print(lst)
                elif answer == "фамилия":
                    new_surname=input("Введите новую фамилию:")
                    lst.remove(stud)
                    app=new_surname + " " + name
                    lst.append(app)
                    lst.sort()
                    print(lst)
                elif answer == "все":
                    new_name=input("Введите новое имя:")
                    new_surname=input("Введите новую фамилию:")
                    lst.remove(stud)
                    app=new_surname + " " + new_name
                    lst.append(app)
                    lst.sort()
                    print(lst)
    else:
        print("Студент не в списке")


def removestud():
    surname=input("Введите фамилию: ")
    name=input("Введите имя или нет:")
    stud=surname+ " " + name
    if name == "нет":
        for i in lst:
            if surname in i:
                print("Ученик с данной вамилией: ", i)
                utoch=input("Введите имя: ")
                student = surname + " " + utoch
                if student in lst:
                    lst.remove(student)
                    lst.sort()
                    print(lst)
    else:
        if stud in lst:
            for i in lst:
                if stud == i:           
                    lst.remove(stud)
                    lst.sort()
                    print(lst)
        else:
            print("Такого ученика нету в списке")
        


while (True):
    com=input("Введите команду: ")
    if com == "show":
        showlst()
    if com == "add":
        addstud()
    if com == "shows":
        showstud()
    if com == "edit":
        editstud()
    if com == "remove":
        removestud()
    if com == "end":
        break

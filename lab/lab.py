documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
def p():
    ndoc=input("Введите номер: ")
    for i in documents:
        if i['number'] == ndoc:
            print (f"Владелец документа: {i['name']}")
            break
    else:
        print ("Документ не найден в базе")
        
def s():
    ndoc=input("Введите номер: ")
    for i in directories:
        for doc in directories[i]:
            if doc == ndoc:
                while True:
                    print(f"Документ хранится на полке: {i}")
                    break
                else:
                    print("Документ не найден в базе")

def fullinf():
    for i in documents:
        for j in directories:
            for x in directories[j]:
                if x == i['number']:
                    print (f"№:{i['number']}, тип: {i['type']}, владелец: {i['name']}, полка хранения: {j}")

def ads():
    polka1=[]
    polka2=[]
    for x in directories:
        polka1.append(x)
    polka2=" ".join(polka1)
    nshelf=input("Введите номер полки: ")
    test=False
    for i in directories:
        if nshelf == i:
            test=True
    if test == False:
        directories[nshelf]=[]
        print ("Полка добавлена. Текущий перечень полок:", polka2, nshelf) 
    else:
        print ("Такая полка уже существует. Текущий перечень полок:", polka2)

def ds():
    polka1=[]
    polka2=[]
    for x in directories:
        polka1.append(x)
    polka2=" ".join(polka1)
    nshelf=input("Введите номер полки: ")
    if nshelf in directories:
        if directories[nshelf]==[]:
            directories.pop(nshelf)
            print("Полка удалена. Текущий перечень полок: ", polka2)
        else:
            print("На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: ", polka2)
    else:
        print ("Такой полки не существует. Текущий перечень полок:", polka2) 

def ad():
    doc={}
    doc['type']=input("Введите тип документа: ")
    doc['number']=input("Введите номер документа: ")
    doc['name']=input("Введите владельца документа: ")
    polka1=input("Введите полку для хранения: ")
    if polka1 in directories:
        documents.append(doc)
        directories[polka1].append(doc['number'])
        print("Документ добавлен. Текущий список документов: ", "\n")
        fullinf()
    else:
        print("Такой полки не существует. Добавьте полку командой as")
        print("Текущий список документов: ")
        fullinf()

def d():
    ndoc=input("Введите номер докумета: ")
    for i in documents:
        test=False
        if i['number'] == ndoc:
            test=True
            documents.remove(i)
            for j in directories:
                for x in directories[j]:
                    if x == ndoc:
                        directories[j].remove(x)
                        break
                if x!=ndoc:
                    break
            break
    if test ==  True:
        print("Документ удален.")
        print("Текущий список документов: ")
        fullinf()
    else:
        print("Документ не найден в базе.")
        print("Текущий список документов: ")
        fullinf()

def m():
    ndoc=input("Введите номер докумета: ")
    polka1=input("Введите полку для хранения: ")
    test=False
    if polka1 in directories:
        for i in documents:
            if i['number'] == ndoc:
                test=True
                break
        if test == True:
            for j in directories:
                for x in directories[j]:
                    if x == ndoc:
                        directories[j].remove(ndoc)
                        directories[polka1].append(ndoc)
                        break
            print("Документ перемещен.")
            print("Текущий список документов:")
            fullinf()
        else:
            print("Документ не найден в базе.")
            print("Текущий список документов:")
            fullinf()
    else:
        print("Такой полки не существует.")
        print("Текущий перечень полок: ")
        for pol in directories:
            print(f"{pol}")
 
7
    
while (True):
     call = input("Введите команду: ")
     if call == "p":
         p()
     if call == "s":
         s()
     if call == "/":
         fullinf()
     if call == "ads":
         ads()
     if call == "ds":
         ds()
     if call == "ad":
         ad()
     if call == "d":
         d()
     if call == "m":
         m()
     if call == "q":
         break

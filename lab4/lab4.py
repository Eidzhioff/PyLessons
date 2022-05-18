class Hotel:
    self_prices = {"SGL": 1000, "DBL": 2000, "Junior Suite": 3000, "Suite": 4000}
    self_roomTypes = list(self_prices.keys())
    self_rooms = dict()
    
    def __init__(self, num_room):
        for num in range(len(num_room)):
            self.self_rooms[self.self_roomTypes[num]]=[1]*num_room[num]

    #Свободен номер или нет
    def __str__(self):
        roomsInfo = ""
        for typ in self.self_roomTypes:
            typeInfo = f"Тип {typ}: \n"
            for num in range(len(self.self_rooms[typ])):
                if self.self_rooms[typ][num] == 1:
                    typeInfo += f"{num + 1} номер свободен \n"
                else:
                    typeInfo += f"{num + 1} номер занят \n"
            roomsInfo += typeInfo
        return roomsInfo

    #Бронь номера
    def occupy (self, typeOfRoom, NumRoom):
        if (self.self_rooms[typeOfRoom][NumRoom-1]==1):
            self.self_rooms[typeOfRoom][NumRoom-1] = 0
            print (f"Номер {NumRoom} забронирован в {typeOfRoom} \n")
        else:
            raise RuntimeError("Номер занят")

    #Занимает все свободные номера в отеле
    def all_occypy(self):
        for typ in self.self_roomTypes:
            for num in range(len(self.self_rooms[typ])):
                self.self_rooms[typ][num]=0

    #Доля занятых номеров
    def occupy_rate(self):
        occupyInfo="Процент занятых номеров: \n"
        for typ in self.self_roomTypes:
            occupyInfo += f"Тип {typ}: {round(self.self_rooms[typ].count(0)/len(self.self_rooms[typ])*100, 2)}% \n"
        return occupyInfo

    #Освобождает все занятые номера
    def all_free(self):
        for typ in self.self_roomTypes:
            for num in range(len(self.self_rooms[typ])):
                self.self_rooms[typ][num]=1

    #Выручка
    def income(self):
        income=0
        for typ in self.self_roomTypes:
            income += (self.self_rooms[typ].count(0)) * self.self_prices[typ]
        return f"Выручка {income} \n"


hotel = Hotel((1,2,3,4))
hotel.occupy("SGL", 1) 
hotel.occupy("DBL", 1)
hotel.occupy("DBL", 2)
hotel.occupy("Suite", 2)
hotel.all_occypy()
print (hotel.occupy_rate())
hotel.all_free()
print (hotel.income())

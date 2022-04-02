import requests
import random
res = requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt')
otv=res.text
def ran():
    print(random.choice(otv.split('\n')))
    
print("Чтобы выйти из прогруммы введите - / ")
while (True):
    ques=input("Введите ваш вопрос: ")
    if ques != "/":
        ran()
    if ques == "/":
        break


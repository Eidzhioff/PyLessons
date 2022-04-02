import requests
import string
res = requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt')
text=res.text
pas = string.ascii_letters.upper()
a=text.split()
count = 0
for i in a:
    for j in i:
        if j in pas:
            count +=1
print(count)

digits=string.digits
count_d = 0
for i in a:
    for j in i:
        if j in pas:
            count_d +=1
print(count_d)

print(text.count(" "))

import requests
import numpy as np
import matplotlib.pyplot as plt
res = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
a=res.text
inttemp=[float(x) for x in a.split()]
print("Максимально значение: ",max(inttemp))
print("Минимальное значение: ",min(inttemp))
print(f"Среднее значение: {sum(inttemp)/len(inttemp)}")
print("Колличество уникальныйх значений: ",len(np.unique(inttemp)))
y = inttemp
plt.plot(y)
plt.show()

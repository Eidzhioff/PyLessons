import requests
import re
import string
words = {}
res = requests.get('http://dfedorov.spb.ru/python3/src/romeo.txt')
text=res.text.lower()
ww = re.findall(r'\b[a-z]{1,15}\b', text)
 
for w in ww:
    count = words.get(w,0)
    words[w] = count + 1
     
word = words.keys()
 
for w_w in word:
    print(w_w, words[w_w])

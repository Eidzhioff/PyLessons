from random import choice, randint 
words=['дота', 'репер', 'хахахаха'] 
word=choice(words)
n = randint(0, len(word)-1)
for x in range(len(word)):
    if x==n:
        print('?',end='')
        continue
    print(word[x],end='')
print(' ')
while True:
    desired=input('Введите букву: ')
    if desired==word[n]:
        print('победа')
        break
    else:
        print('Увы! Попробуйте в еще раз')

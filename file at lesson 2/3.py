import string
text = open("moby.txt","r")
txt=text.read()
print(txt.translate(str.maketrans('', '', string.punctuation)))
         


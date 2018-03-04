#Tom Geraghty 03/03/2018
#Explanation of lists looping in Python

words = ["Jack", "Amy", "Lisa", "Conor", "Mum"]

i = 0
while i < len(words):
    print(i, words[i])
    i = i+1

#https://docs.python.org/3/tutorial/controlflow.html#for-statements
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(len(words)):
    print(i, words[i], len(words[i]))
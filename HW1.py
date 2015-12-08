import os

f = open('gralph.csv', 'r', encoding='utf-8')

d = {}

for line in f:
    line = line.replace('\ufeff', '')
    l = line.split('\t')
    d[l[0]]=l[2]



f.close()

f2 = open('granthem.txt', 'r', encoding='utf-8')
f3 = open('f4.txt', 'w', encoding='utf-8')

for line in f2:
    for word in line:
        for k in d:
            if word == k:
                word = word.replace(word, d[k])
                f3.write(word)
                
f2.close()    

f3.close()

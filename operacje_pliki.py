#! /usr/bin/python
#zapis do pliku
file=open('test.txt','w')
file.write('hello world!')
file.close()
#odczyt pliku
file=open('test.txt','r')
print(file.read())
file.close()
#bezpieczna praca z plikami
with open('test.txt', 'r') as f:
    print(f.read())

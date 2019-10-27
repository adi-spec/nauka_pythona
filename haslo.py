#! /usr/bin/python

#haslo='woj'
haslo=input()
pwd=len(haslo)

#gwiazdki=
#secret=''
if pwd<3:
    print("haslo za krotkie")

else:
    for i in range(1, pwd -1):
        print(haslo[0] + (pwd-2)*'*' + haslo[-1])
    #    break



#haslo = 'wojtek'

#gwiazdki = (len(haslo) - 2) * "*"
#secret = haslo[0] + gwiazdki + haslo[-1]
#print(secret)

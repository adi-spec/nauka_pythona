#! /usr/bin/python

samochody=['syrena','polonez','maluch']
print(samochody[1])
print(samochody[0])

for s in samochody:
    print(s)

for idx in range(len(samochody)):
    print('idx: ' +str(idx)+ ':' +samochody[idx])

print('---------------------------------------')
samoloty=['f-14', 'f-16', 'MIG-29', 'Su-27']
print(samoloty[1])
print(samoloty[0])

for s in samoloty:
    print(s)

for idx in range(len(samoloty)):
    print('idx: ' +str(idx)+ ':' +samoloty[idx])

from kolejka import *
from probowka import *
from plansza import *
from copy import deepcopy

poziom = Plansza([

Probowka( ['bez', 'nieb', 'bez']),
Probowka( []),
Probowka( ['ziel', 'ziel', 'ziel', 'ziel']),
Probowka( []),
Probowka( ['braz','zlot','zlot']),
Probowka( []),
])
print(poziom)
print(poziom.vials[0].top())
print(poziom.vials[2].top())
print(poziom.vials[4].top())

moves = [(2,3),(0,1),(4,5)]
for i in moves:
    przelej(poziom.vials[i[0]],poziom.vials[i[1]])
# print(poziom)

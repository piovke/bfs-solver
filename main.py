from solver import *

poziom = Plansza([
    Probowka(['zolty','bezowy','niebieski','czerwony']),
    Probowka(['bezowy','zolty','niebieski']),
    Probowka(['czerwony','pomaranczowy','rozowy','pomaranczowy']),
    Probowka(['bezowy','czerwony','pomaranczowy','niebieski']),
    Probowka(['czerwony','zielony','zielony','rozowy']),
    Probowka(['zielony','zolty','pomaranczowy','niebieski']),
    Probowka(['zolty','rozowy','zielony','bezowy']),
    Probowka(['rozowy']),
    Probowka([]),
])


print('rozwiązywanie...\n')
rozwiazanie = solve(poziom)
visualise(poziom,rozwiazanie)
print(rozwiazanie)

from solver import *

poziom = Plansza([
    Probowka(['cziel','bez','malin','ziel']),
    Probowka(['pom','gran','zol','fiol']),
    Probowka(['fiol','pizdz','gran','braz']),
    Probowka(['pizdz','malin','malin','roz']),
    Probowka(['roz','bez','gran','pom']),
    Probowka(['bez','nieb','pizdz','zol']),
    Probowka(['cziel','zol','braz','pizdz']),
    Probowka(['pom','cziel','fiol','ziel']),
    Probowka(['nieb','braz','pom','nieb']),
    Probowka(['braz','roz','malin','nieb']),
    Probowka(['bez','zol','gran','roz']),
    Probowka(['ziel','cziel','ziel','fiol']),
    Probowka([]),
    Probowka([]),
])

print('rozwiązywanie...\n')
rozwiazanie = solve(poziom)
visualise(poziom,rozwiazanie)
print(rozwiazanie)
from kolejka import *
from probowka import *
from plansza import *
from copy import deepcopy

def solve(plansza_poczatkowa:Plansza):
    odwiedzone = set()
    odwiedzone.add(plansza_poczatkowa.state())
    q = Kolejka()
    # W kolejce  są dane:  ruch DO WYKONANIA⬇️
    #                     (plansza, (giver, receiver), [historia_ruchow])

    #do kolejki dodaje: (kopie aktualnej planszy); (jeden z możliwych ruchów); (lista na historie ruchów)
    #i tak dodaje wszystkie valid ruchy z początkowej planszy
    for move in plansza_poczatkowa.possible_moves():
        q.add((deepcopy(plansza_poczatkowa), move, []))

    #wykonuje ruchy z kolejki, póki istnieją valid ruchy albo aż wygra
    while not q.empty():
        #pobiera dane z kolejki
        dane = q.take()
        plansza = dane[0]
        ruch = dane[1]
        historia = dane[2]
        giver = plansza.vials[ruch[0]]
        receiver = plansza.vials[ruch[1]]

        #Wykonuje ruch. jeśli prowadzi do stanu widzianego wcześniej przechodzi do następnego elementu kolejki
        przelej(giver,receiver)
        if plansza.state() in odwiedzone:
            continue
        odwiedzone.add(plansza.state())

        #check czy wygral
        if plansza.won():
            historia.append(ruch)
            # print(historia)
            return historia

        # do kolejki dodaje: (kopie aktualnej planszy); (jeden z możliwych ruchów); (historie ruchów)
        for move in plansza.possible_moves():
            nowa_historia = deepcopy(historia)
            nowa_historia.append(ruch)
            q.add((deepcopy(plansza), move, nowa_historia))

    return None

def visualise(plansza:Plansza, moves):
    print(plansza)
    for i in moves:
        przelej(plansza.vials[i[0]],plansza.vials[i[1]])
        ruch = f"po ruchu:  {str(i)}"
        print(f"{ruch:^20}")
        print(plansza)
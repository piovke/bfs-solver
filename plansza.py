from probowka import *
from copy import deepcopy

class Plansza:
    def __init__(self, vials):
        self.vials = vials

    def __str__(self):
        text = ""
        for i,vial in enumerate(self.vials):
            text+=f"{i}: {str(vial.content):<40} {"✅" if vial.winning_state() else "":>2}\n"
        return text

    def __deepcopy__(self, memo):
        return Plansza(deepcopy(self.vials))


    def possible_moves(self) -> list[tuple[int, int]]:
        moves = []
        for i, giver in enumerate(self.vials):
            for j, receiver in enumerate(self.vials):
                if i == j:
                    continue
                if moznaprzelac(giver,receiver):
                    moves.append((i,j))
        return moves

    def won(self):
        for vial in self.vials:
            if not vial.winning_state():
                return False
        return True

    def state(self):
        #zwraca stan planszy w taki sposob ze zmiana kolejnosci probowek nie ma znaczenia
        probowki = []
        for vial in self.vials:
            probowki.append(deepcopy(vial).state())
        return tuple(sorted(probowki))
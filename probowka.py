from copy import deepcopy
class Probowka:
    def __init__(self, content, height=4):
        self.height = height
        self.content = content

    def __str__(self):
        text = ""
        for i in range(0, self.height - len(self.content)):
            text += f'|{"xxxxxxx":^15}|\n'
        for i in range(-1, len(self.content) * -1 - 1, -1):
            text += f'|{self.content[i]:^15}|\n'
        return text


    def __deepcopy__(self, memo):
        new_copy = Probowka([], self.height)
        new_copy.content = deepcopy(self.content)
        return new_copy


    def top(self):
        if len(self.content) == 0:
            return []
        color = self.content[-1]
        top = [color]
        for i in range(-2, -len(self.content)-1, -1):
            if self.content[i] == color:
                top.append(color)
            else:
                break
        return top

    def take(self):
        onTop = self.top()
        taken = len(onTop)
        for i in range(taken):
            self.content.pop()
        return onTop

    def put(self, adding):
        self.content += adding

    def winning_state(self) -> bool:
        if len(self.top()) == self.height or len(self.top()) == 0:
            return True
        return False

    def state(self):   #wypełnia puste miejsca '', do przechowywania odwiedzonych plansz
        uzupelniona = list(self.content)
        while len(uzupelniona) < self.height:
            uzupelniona.append('')
        return tuple(uzupelniona)



def moznaprzelac(giver:Probowka, receiver:Probowka) -> bool:
    liquid = giver.top()
    if len(liquid) == 0:            #nie ma czego przelewac (pusta probowka)
        return False
    space = receiver.height - len(receiver.content)
    if space < len(liquid):         #nie ma miejsca w dostającej
        return False
    if len(receiver.content) == 0:     #dostająca jest pusta OK
        return True
    if liquid[0] == receiver.content[-1]:  #kolory się zgadzają OK
        return True
    return False                        #kolory się nie zgadzaja

def przelej(giver:Probowka, receiver:Probowka):
    receiver.put(giver.take())

def sprobojprzelac(giver:Probowka, receiver:Probowka) -> bool:
    #potrzebna tylko jakbym robil wersje dla ludzi
    if moznaprzelac(giver,receiver):
        przelej(giver,receiver)
        return True
    else: return False
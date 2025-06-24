class Wezel:
    def __init__(self, dane):
        self.dane = dane
        self.nast = None


class Kolejka:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        text="Q: <"
        temp=self.front
        while temp is not None:
            text+= f"P{temp.dane[1]} {temp.dane[2]} "
            temp = temp.nast
        text+=">"
        return text

    def empty(self):
        if self.front is None:
            return True
        return False

    def add(self, element):
        new_node = Wezel(element)
        if not self.front:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.nast = new_node
        self.rear = new_node

    def take(self):
        element = self.front
        if element is None:
            return None
        self.front = self.front.nast
        if self.front is None:
            self.rear = None
        return element.dane
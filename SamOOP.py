class Alien():
    def __init__(self, name:str, volume:int, filled:int):
        self.name = name
        self.volume = volume
        self.filled = filled

    def __iadd__(self, other):
        value = self.volume + other.volume
        return Alien(self.name, value, self.filled)

    def __str__(self):
        return f"Wheel Alien {self.name} with {self.volume} valume and filled up {self.filled}."

    def __isub__(self, other):
        value = self.volume - other.volume
        return Alien(self.name, value, self.filled)

    def __eq__(self, other):
        value = self.volume * self.filled == other.volume * other.filled
        return value

    def fill_up(self, x:int):
        if x >= 0:
            return Alien(self.name, self.volume, self.filled+x)
        else:
            return Alien(self.name, self.volume, self.filled - x)

    def __mul__(self, x:int):
        for i in range(x):
            print(Alien(self.name + "-" + str(i + 1), self.volume, self.filled))

    def __add__(self, other):
        return Alien(self.name + "-" + other.name, (self.volume + other.volume) // 2, min(self.filled, other.filled))

    def __ne__(self, other):
        value = self.volume * self.filled != other.volume * other.filled
        return value

    def __lt__(self, other):
        value = self.volume * self.filled < other.volume * other.filled
        return value

    def __gt__(self, other):
        value = self.volume * self.filled > other.volume * other.filled
        return value

    def __le__(self, other):
        value = self.volume * self.filled <= other.volume * other.filled
        return value

    def __ge__(self, other):
        value = self.volume * self.filled >= other.volume * other.filled
        return value


al = Alien("Man", 458, 181)
al1 = Alien("Spider", 780, 209)
print(al <= al1, al != al1, al > al1)
print(al, al1, sep="\n")
print()
al.fill_up(20)
res = al1 * 3
print(al, al1, res, sep="\n")
print(al.fill_up(20))
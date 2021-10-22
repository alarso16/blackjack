

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def is_ace(self) -> bool:
        if self.rank == 'Ace':
            return True
        return False

    def value(self) -> int:
        value = 0
        try:
            value = int(self.rank)
        except:
            if self.rank == "Ace":
                value = 11
            else:
                value = 10
        return value

    def __str__(self) -> str:
        disp = f"{self.rank} of {self.suit}"
        return disp

    def __add__(self, right) -> int:
        return self.value() + right.value()

    def __eq__(self, right) -> bool:
        return self.rank == right.rank

if __name__ == "__main__":
    print(Card('3', 'Spades'))
from card import Card

class Hand():
    def __init__(self, bet=0):
        self.card_list = []
        self.bet = bet

    def add(self, cards):
        for card in cards:
            self.card_list.append(card)

    def sum(self):
        sum = 0
        for card in self.card_list:
            sum += card.value
        return sum

    def get_top(self):
        if (len(self.card_list) == 0):
            return None
        return self.card_list[0]

    def discard(self, deck):
        deck.discard(self.card_list.copy())
        self.card_list.clear()
    
    def __str__(self) -> str:
        string = ""
        if self.bet > 0:
            string += f"${self.bet}- "
        for card in self.card_list:
            string += str(card) + ", "
        string = string[:-2]
        return string


if __name__ == "__main__":
    hand = Hand()
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    print(hand)
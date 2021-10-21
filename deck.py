from card import Card
import random

class Deck:
    def __init__(self, num_decks=1, shoe_depth=1):
        self.deck = []
        self.min_length = num_decks * shoe_depth * 52

        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8','9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for i in range(num_decks):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(rank, suit))

        random.shuffle(self.deck)

    def deal(self, num=1):
        if len(self.deck) < self.min_length:
            self.shuffle()

        return [self.deck.pop() for i in range(num)]

    def discard(self, card_list):
        for card in card_list:
            self.deck.append(card)

    def shuffle(self, discard):
        self.deck[len(self.deck):] = [card for card in discard.deck]
        discard.deck.clear()

        random.shuffle(self.deck)

    def isempty(self) -> bool:
        return not self.deck

    def __len__(self):
        return len(self.deck)

if __name__ == "__main__":
    deck = Deck()
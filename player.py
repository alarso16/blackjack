from card import Card
from hand import Hand

class Player():
    def __init__(self, name, dealer=False, buy_in=100):
        self.name = name
        self.hand = None
        self.split_hand = None
        self.dealer = dealer
        self.cash = buy_in
        self.has_blackjack = False

    def add_hand(self, hand):
        self.hand = hand

    def take_turn(self, deck):
        pass

    def payout(self, dealer):
        if self.has_blackjack: # already paid out
            return
        
        if self.hand.sum() < 21:
            if self.hand.sum() >= dealer.hand.sum():
                self.cash += self.hand.bet # make back money in tie
            if self.hand.sum() > dealer.hand.sum():
                self.cash += self.hand.bet # make money on win

    def cleanup(self, discard):
        self.hand.discard(discard)
        if self.split_hand != None:
            self.split_hand.discard(discard)
        self.split_hand = None
        self.has_blackjack = False

    def __str__(self) -> str:
        string = self.name + ": $" + str(self.cash) + "\n"
        string += "\t" + str(self.hand)
        if self.split_hand != None:
            string += "\n\t" + str(self.hand)
        return string

if __name__ == "__main__":
    player = Player('austin')
    hand = Hand(bet=5)
    hand.add(Card('3', 'Spades'))
    hand.add(Card('Ace', 'Diamonds'))
    player.add_hand(hand)
    print(player)
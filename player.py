from card import Card
from hand import Hand

class Player():
    def __init__(self, name, dealer=False, buy_in=100):
        self.name = name
        self.hand = Hand()
        self.split_hand = Hand()
        self.dealer = dealer
        self.cash = buy_in
        self.has_blackjack = False

    def add_hand(self, hand):
        self.hand = hand

    def take_turn(self, deck):
        if self.dealer:
            while self.hand.sum() <= 17:
                self.hand.add(deck.deal())
            if self.hand.sum() > 21:
                print('Bust!')

        else:
            return self._take_player_turn(deck)

        return 0


    def _take_player_turn(self,deck):
        action = 'h'
        main_done = False

        # Obviously wont hit on a blackjack
        if self.has_blackjack:
            return
        
        print(self)

        # offer split
        if (self.split_hand == None) and self.hand.can_split():
            action = input('Would you like to split your hand? (y/n): ').lower()
            if (action != 'y') and (action != 'n'):
                print("You're obviously too stupid to split your hand if you can't enter the right character.")
                print("Maybe you'll get it right next time...")
                print()
            elif action == 'y':
                self.split_hand = self.hand.split()
                self.cash -= self.split_hand.bet
                self.cash -= self.split_hand.play_hand(deck)

        self.cash -= self.hand.play_hand(deck)


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
            string += "\n\t" + str(self.split_hand)
        return string

if __name__ == "__main__":
    player = Player('austin')
    hand = Hand(bet=5)
    hand.add(Card('3', 'Spades'))
    hand.add(Card('Ace', 'Diamonds'))
    player.add_hand(hand)
    print(player)
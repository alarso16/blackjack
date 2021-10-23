from deck import Deck
from player import Player
from hand import Hand
from card import Card

class Game:
    def __init__(self, num_players, num_decks=1, shoe_perc=0, min_bet=5):
        self.deck = Deck(num_decks=num_decks, shoe_depth=shoe_perc)
        self.discard = Deck(num_decks=0)
        self.players = [Player(input(f'Player {i+1} please enter your name: ')) for i in range(num_players)]
        self.dealer = Player(name='Dealer', dealer=True)
        self.min_bet = min_bet
        self.insurance_bets = [0 for i in range(num_players)]
        self.done = False

    def play_game(self):
        # Make bets and deal cards

        while not self.done:
            self.deal_cards() # gets bets and deals initially

            print(self)
            print()
            
            # Check to see if insurance bets should be made
            if self.dealer.hand.get_top().is_ace():
                print('getting insurance bets')
                self.get_insurance()

            # Check for instant payouts
            self.check_blackjacks()

            # Check insurance bets and payout
            if self.dealer.has_blackjack and (sum(self.insurance_bets) != 0):
                self.payout_insurance()
            else:
                # Let each player take their turn
                for i in range(len(self.players)):
                    print(f"Dealer: {self.dealer.hand.get_top()}")
                    self.players[i].take_turn(self.deck)

                # Let dealer take turn
                self.dealer.take_turn(self.deck)

                # Compare sums and payout
                self.payout()

            # Clean up cards and prepare for next round
            self.cleanup()

            #Offer opportunity to remove a player
            self.confirm_players()

        print("Thanks for playing!")

        return

    def deal_cards(self):
        for i in range(len(self.players)):
            bet = 0
            while bet == 0:
                try:
                    bet = int(input(f"{self.players[i].name}: Please enter a bet. $"))
                    if bet < self.min_bet:
                        raise Exception()
                    if bet > self.players[i].cash:
                        raise Exception()
                except:
                    print("Please try entering above the minimum, but don't go into debt.")
            temp_hand = Hand(bet=bet)
            temp_hand.add(self.deck.deal(2))
            self.players[i].cash -= temp_hand.bet
            self.players[i].add_hand(temp_hand)
        temp_hand = Hand()
        temp_hand.add(self.deck.deal(2))
        self.dealer.add_hand(temp_hand)

    
    def get_insurance(self):
        print('Please enter your insurance bets.')
        print('Reminder: it can only be up to half of your bet.')
        for i in range(len(self.players)):
            try:
                self.insurance_bets[i] = int(input(f'{self.players[i].name}: $'))
                if self.insurance_bets[i] > (0.5 * self.players[i].hand.bet):
                    print('You put too much money in. You will just bet half.')
                    self.insurance_bets[i] = 0.5 * self.players[i].hand.bet
                if self.insurance_bets[i] > self.players[i].cash:
                    print("Actually, you don't have enough money to make that bet.")
                    self.insurance_bets[i] = 0
                self.players[i].cash -= self.insurance_bets[i]
            except:
                print('Enter a number next time and maybe you will be allowed to bet.')

    def payout_insurance(self):
        for i in range(len(self.players)):
            self.players[i].cash += 2 * self.insurance_bets[i]
            self.insurance_bets[i] = 0

    def check_blackjacks(self):
        for i in range(len(self.players)):
            if self.players[i].hand.sum() == 21:
                print(f'{self.players[i].name} has a blackjack!')
                self.players[i].has_blackjack = True

        if self.dealer.hand.sum() == 21:
            print("Dealer has a blackjack!")
            self.dealer.has_blackjack = True

        for i in range(len(self.players)):
            if self.players[i].has_blackjack:
                if self.dealer.has_blackjack:
                    self.players[i].cash += self.players[i].hand.bet
                else:
                    self.players[i].cash += 2.5 * self.players[i].hand.bet

    def payout(self):
        if self.dealer.hand.sum() > 21:
            print(f"Dealer: {self.dealer.hand.sum()} - Bust!")
        else:
            print(f"Dealer: {self.dealer.hand.sum()}")
        
        for i in range(len(self.players)):
            self.players[i].payout(self.dealer)

    def cleanup(self):
        for i in range(len(self.players)):
            self.players[i].cleanup(self.discard)
        self.dealer.cleanup(self.discard)

    def confirm_players(self):
        i = 0
        while i < len(self.players):
            if self.players[i].cash < self.min_bet:
                print(f"{self.players[i].name} does not have enough money to continue.")
                self.players.pop(i)
            else:
                answer = input(f"{self.players[i].name}: Enter 'q' if you wish to quit.\n").lower()
                if answer == 'q':
                    self.players.pop(i)
                else:
                    i += 1
        
        if len(self.players) == 0:
            self.done = True
            

    def __str__(self) -> str:
        string = f"Dealer: {self.dealer.hand.get_top()}\n"
        for player in self.players:
            string += str(player) + "\n"
        string += f"{len(self.deck)} cards remaining in deck."
        return string
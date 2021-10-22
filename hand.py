from card import Card

class Hand():
    def __init__(self, bet=0):
        self.card_list = []
        self.bet = bet

    def play_hand(self, deck):
        value = 0 #extra bet
        action = 'a'

        print(self)
        action = input("Would you like to double down? (y/n): ").lower()
        if action == 'y':
            value += self.bet
            self.bet *= 2
            print(self)
        elif action != 'n':
            print("You're too stupid. Guess you can't double down.")

        while (action != 's') and (self.sum() <=21):
            if action != 'y': # doubled down
                print('h: Hit')
                print('s: Stand')
                action = input().lower()
            
            if (action == 'h') or (action == 'y'):
                self.add(deck.deal())
                print(self)
            elif action !='s':
                print('Come on, enter one of the options next time.')

            if action == 'y':
                break

        if self.sum() > 21:
            print('Bust!')

        return value


    def add(self, cards):
        for card in cards:
            self.card_list.append(card)

    def sum(self):
        hand_sum = 0
        for card in self.card_list:
            hand_sum += card.value()
        if hand_sum > 21:
            for card in self.card_list:
                if card.is_ace():
                    hand_sum -= 10
                if hand_sum <= 21:
                    break
        return hand_sum

    def get_top(self):
        if (len(self.card_list) == 0):
            return None
        return self.card_list[0]

    def discard(self, deck):
        deck.discard(self.card_list.copy())
        self.card_list.clear()

    def can_split(self):
        if len(self) != 2:
            return False
        return self.card_list[0] == self.card_list[1]

    def split(self):
        split_hand = Hand(bet=self.bet)
        split_hand.add(self.card_list.pop())
        return split_hand
    
    def __str__(self) -> str:
        string = ""
        if self.bet > 0:
            string += f"${self.bet}- "
        for card in self.card_list:
            string += str(card) + ", "
        string = string[:-2]
        return string

    def __len__(self) -> int:
        return len(self.card_list)


if __name__ == "__main__":
    hand = Hand()
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    hand.add(Card('3', 'Spades'))
    print(hand)
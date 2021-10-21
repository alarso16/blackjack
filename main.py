from game import Game

def main():
    print("Welcome to Blackjack!")
    print()
    print("Each player will start with $100, with a minimum $5 bet.")
    print("You can split and double down, even on Aces.")
    print("Insurance/even money will be offered.")
    print("Dealer will stand at 17.")
    print()

    invalid = True
    
    while invalid:
        try:
            num_players = int(input("Please enter the number of players: "))
            if num_players < 1 or num_players > 6:
                raise Exception()
            num_decks = int(input("Please enter a number of decks: "))
            if num_decks < 1 or num_decks > 8:
                raise Exception()
            shoe_perc = float(input("Please enter a percent left in shoe before reshuffle: "))
            if shoe_perc > 0.8 or shoe_perc < 0:
                raise Exception()
            invalid = False
            
        except Exception as e:
            print("Enter a realistic number this time dumbass.\n")

    game = Game(num_players, num_decks, shoe_perc)
    game.play_game()

    return

if __name__ == "__main__":
    main()
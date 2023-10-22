import random

class Blackjack:
    def __init__(self): #Intializes the start of the game, aka deck, player, and dealer
        self.deck = self.initialize_deck()
        self.player_hand = [] 
        self.dealer_hand = []

    def initialize_deck(self): #Creates the deck and sorts it by its suit and number
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        total_value = 0
        num_aces = 0

        for suit, rank in hand:
            if rank == 'Ace':
                total_value += 11
                num_aces += 1
            elif rank in ('Jack', 'Queen', 'King'):
                total_value += 10
            else:
                total_value += int(rank)

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value

    def deal_initial_hands(self):
        for _ in range(2):
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())

    def display_hands(self, reveal_dealer=False):
        print(f"Player's hand: {self.player_hand} (Value: {self.calculate_hand_value(self.player_hand)})")
        print("Dealer's hand:", end=" ")

        if reveal_dealer:
            for suit, rank in self.dealer_hand:
                print(f"[{suit}, {rank}]", end=" ")
        else:
            suit, rank = self.dealer_hand[0]
            print(f"[{suit}, {rank}]", end=" [?]")

        print()

    def player_cards(self):
        while True:
            self.display_hands()

            if self.calculate_hand_value(self.player_hand) == 21:
                print("Blackjack! You Win!")
                self.dealer_play()
                break

            cards = input("Hit or Stand: ").lower()

            if cards == 'hit':
                self.player_hand.append(self.deck.pop())
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("Bust! Your hand value is over 21. You lose.")
                    self.dealer_play()
                    break
            elif cards == 'stand':
                self.dealer_play()
                break

    def dealer_play(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        self.display_hands(reveal_dealer=True)
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if dealer_value > 21:
            print("Dealer busts! You Win!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("It's a tie!")

    def play_game(self):
        print("Welcome to Blackjack!")
        self.deal_initial_hands()
        self.player_cards()


blackjack_game = Blackjack()

blackjack_game.play_game()

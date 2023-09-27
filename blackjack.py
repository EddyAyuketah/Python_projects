# Eddy Ayuketah 
# CIT 263
import random
from session import Session
import sys

session = Session()

class Card:
    def __init__(self, suit, rank):
        """Create a new card object suit and rank"""
        self.suit = suit
        self.rank = rank
        # NOTE: __init__() methods NEVER have a return statement.

    def value(self):
        if self.rank in ['jack', 'queen', 'king']:
            return 10
        elif self.rank == 'ace':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self, num_decks=1):
        self.deck = []
        self.current = 0
        for i in range(num_decks):
            for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
                for rank in range(1, 14):
                    card = Card(suit, rank)
                    self.deck.append(card)
        random.shuffle(self.deck)
        # NOTE: __init__() methods NEVER have a return statement.

    def shuffle(self):
        """The shuffle cards in deck."""
        random.shuffle(self.deck)
        self.current = 0

    def deal(self):
        """gets next card in deck."""
        card = self.deck[self.current]
        self.current +=1
 
        if self.current == len(self.deck):
            self.current = 0
            self.shuffle()
        card = self.deck[self.current]
        self.current += 1
        return card
        
class Hand:
    def __init__(self):
        """Create a new card object suit and rank"""
        self.cards = []
        # NOTE: __init__() methods NEVER have a return statement.

    def addCard(self, card):
        self.cards.append(card)

    def value(self):
        """Calculate the total value of the cards in the hand."""
        total = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ["J", "Q", "K"]:
                total += 10
            elif card.rank == "A":
                num_aces += 1
                total += 11
            else:
                total += int(card.rank)

        # Adjust the value for aces if the total exceeds 21
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1

        return total

    def has_blackjack(self):
        """Return True if the hand has blackjack, False otherwise"""
        return len(self.cards) == 2 and self.hand_value() == 21

    def isSoft17(self):
        if len(self.cards) ==  2 and "Ace" in [card.value for card in self.cards] and self.get_value() == 17:
            return True
        else:
            return False
        

    def hand_value(self):
        return min([value for value in self.values if value <= 21])
    
    def __str__ (self):
        hand = ""
        for c in range(len(self.cards)):
            hand = hand + str(self.cards[c].rank) + " of " + self.cards[c].suit

            if c < len(self.cards) - 1:
                hand = hand + ", "
        return hand
class BlackJack:
    def __init__(self, deck_count=1):
        self.deck = Deck(deck_count)
        self.player = Hand()
        self.dealer = Hand()
        self.session = Session()
        # initialize the deck, player and dealer hands, and session object
        pass
    
    def play_round(self):
        # ask the user for their bet amount
        while True:
            try:
                bet = float(input(f"\nYou have ${self.session.bankroll:.2f}. How much would you like to bet? "))
                if bet <= 0:
                    print("Invalid bet amount. Please enter a positive value.")
                elif bet > self.session.bankroll:
                    print("You don't have enough money to bet that amount.")
                    print(Session)
                else:
                    self.session.bet = bet
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        #self.session.bet = bet (i think this line is redundant)
        
        # deal the cards and play the game
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.deal_cards()
        self.show_table()
        self.player_turn()
        if not self.player_busted:
            self.dealer_turn()
        self.determine_winner()



# Update session object's hands_won, hands_lost, or hands_tied attribute
        if self.player.has_blackjack() and not self.dealer.has_blackjack():
            print("Blackjack! You win.")
            self.session.hands_won += 1
            self.session.winnings += self.session.bet * 1.5
            self.session.bankroll += self.session.bet * 2.5
        elif not self.player.has_blackjack() and self.dealer.has_blackjack():
            print("Dealer has blackjack. You lose.")
            self.session.hands_lost += 1
            self.session.losses += self.session.bet
            self.session.bankroll -= self.session.bet
        elif self.player.hand_value() > 21:
            print("Bust. You lose.")
            self.session.hands_lost += 1
            self.session.losses += self.session.bet
            self.session.bankroll -= self.session.bet
        elif self.dealer.hand_value() > 21:
            print("Dealer busts. You win!")
            self.session.hands_won += 1
            self.session.winnings += self.session.bet
            self.session.bankroll += self.session.bet * 2
        elif self.player.hand_value() > self.dealer.hand_value():
            print("You win!")
            self.session.hands_won += 1
            self.session.winnings += self.session.bet
            self.session.bankroll += self.session.bet * 2
        elif self.dealer.hand_value() > self.player.hand_value():
            print("You lose.")
            self.session.hands_lost += 1
            self.session.losses += self.session.bet
            self.session.bankroll -= self.session.bet
        else:
            print("It's a tie.")
            self.session.hands_tied += 1



        
        # update the session object's attributes based on the outcome
        if self.player_wins:
            self.session.bankroll += self.session.bet
            self.session.winnings += self.session.bet
            self.session.hands_won += 1
            print(f"\nYou won ${self.session.bet:.2f}.")
        elif self.dealer_wins:
            self.session.bankroll -= self.session.bet
            self.session.losses += self.session.bet
            self.session.hands_lost += 1
            print(f"\nYou lost ${self.session.bet:.2f}.")
        else:
            self.session.hands_tied += 1
            print("\nIt's a tie.")
        
        # check if the game is over (i.e., the player runs out of money)
        if self.session.bankroll <= 0:
            print("\nYou're out of money. Game over!")
            print(f"\nFinal bankroll: ${self.session.bankroll:.2f}")
            print(f"Average winnings per hand: ${self.session.winnings/self.session.hands_won:.2f}")
            print(f"Average losses per hand: ${self.session.losses/self.session.hands_lost:.2f}")
            sys.exit()
    

deal = "D"
while deal.upper() == "D":
    dealer = Hand()
    player = Hand()     
    deck = Deck(num_decks=6)
    deck.shuffle()
    #deal cards to dealer and player
    for d in range(2):
        player.addCard(deck.deal())
        dealer.addCard(deck.deal())
        
    #show dealer top card

    print("Dealer shows: " + str(dealer.cards[1].rank) + " of " + dealer.cards[1].suit)

    #show player hand and value
    print("Player holds: " + str(player))
    print("Player value: " + str(player.value()))

    #show dealer hand and value
    print("Dealer holds: " + str(dealer))
    print("Dealer value: " + str(dealer.value()))

    #player turn
    stand = False
    while player.value() < 22 and stand == False:
        choice = input("Enter H to hit or S to stand ")
        if choice.upper() == "S":
            stand = True
        elif choice.upper() == "H":
            print("Player taking card")
            player.addCard(deck.deal())
            print("Player holds: " + str(player))
            print("Player value: " + str(player.value()))
        else:
            print("You must enter an S or H")
            
    #if player bust, hand over
    if player.value() > 21:
        print("Player busts, dealer wins")
    else:
        #dealer turn
        print("Dealer holds: " + str(dealer))
        print("Dealer value: " + str(dealer.value()))
        stand = False
        while dealer.value() < 17:
            print("Dealer taking card")
            dealer.addCard(deck.deal())
            print("Dealer holds: " + str(dealer))
            print("Dealer value: " + str(dealer.value()))

        if dealer.value() > 21:
            print("Dealer busts, player wins")
        elif player.value() == dealer.value():
            print("It's a push")
        elif player.value() > dealer.value():
            print("Player wins")
        else:
            print("Dealer wins")
            deal = ""
            
        while deal.upper() != "D" and deal.upper() != "Q":
            deal = input("Enter D to deal or Q to quit ")
            # When the player decides to quit the game or runs out of money, print out the session object.
            if choice.upper() == "Q":
                print(Session())
            
print("You've come to the end of the game")

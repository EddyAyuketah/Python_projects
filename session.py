import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in
                      ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.value]
        if card.value == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Session:
    def __init__(self):
        self.bankroll = 200.00
        self.bet = 0
        self.winnings = 0
        self.losses = 0
        self.hands_won = 0
        self.hands_lost = 0
        self.hands_tied = 0

    def __str__(self):
        average_winnings = self.winnings / (self.hands_won + self.hands_lost + self.hands_tied)
        average_losses = self.losses / (self.hands_won + self.hands_lost + self.hands_tied)
        return f"Bankroll: ${self.bankroll:.2f}\nAverage Winnings: ${average_winnings:.2f}\nAverage Losses: ${average_losses:.2f}"

deck = Deck()
deck.shuffle()

values = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10,
          "King": 10}

session = Session()

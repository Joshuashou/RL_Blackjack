import random
import numpy as np

class Hand(): #Defines a Hand in Blackjack
    def __init__(self, player='P'):
        self.deck = Deck()

        self.use_ace = 0 #Starts out with no ace. 

        if player == 'P':
            self.hand = [self.deck.draw_card(), self.deck.draw_card()]  # Initial two cards
        else:  #player = Dealer
            self.hand = [self.deck.draw_card()]

        if ('1' in self.hand):
            self.use_ace = 1

        self.value = self.calculate_hand_value()

    def calculate_hand_value(self):
        value = sum(int(card) for card in self.hand)
        # Adjust for Ace value
        if '1' in self.hand and value + 10 <= 21:
            value += 10
        return value
    
    def hit(self):
        new_Card = self.deck.draw_card()
        self.hand.append(new_Card)

        old_value = self.value
        self.value = self.calculate_hand_value()

        if new_Card == '1' and (self.value - old_value == 11):
            self.use_ace = 1

    
        
class Deck():
    def __init__(self):
        self.cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10'] * 4

    def draw_card(self):
        return random.choice(self.cards)
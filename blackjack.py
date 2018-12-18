import random

#GLOBAL VARIABLES
SUITS = ("Hearts", "Spades", "Clubs", "Diamonds")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
VALUES = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

#Create a Card class
class Card():
    #Define the two attributes of a card: suit and rank
    def __init__(self, suit, rank):
        #Initialize suit and rank variables as part of the Card class, with the suit and rank attributes passed to the class
        self.suit = suit
        self.rank = rank   
    
    #Create the string definition of the object as: "Rank of Suit"
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Create a Deck class
class Deck():
    #Initialize the Deck object by creating the 52 card deck out of Card objects
    def __init__(self):   
        #Initialize the deck variable as part of the Deck class, which will be loaded with the 52 cards of type Card
        self.deck = []

        #For each suit in the GLOBAL VARIABLE suits
        for suit in SUITS:
            #For each suit in the GLOBAL VARIABLE suits
            for rank in RANKS:
                #Add a Card object of suit and rank to the self.deck variable
                self.deck.append(Card(suit, rank))
    
    #Create a string representation of self.deck to report back when the deck is called as a string
    def __str__(self):
        #Create an empty string for the deck contents
        deck_contents = ""

        #For each card in self.deck.  The card variable is just the variable used for iteration of all self.deck Card objects in this case.
        for card in self.deck:
            #Add the string definition of each Card object to the deck contents string.  The string definition is: f"{Card.rank} of {Card.suit}"
            deck_contents += card.__str__() + "\n"
        #Return the deck_contents string
        return deck_contents
    
    #Create a length representation of self.deck to report back when the length of the deck is requested
    def __len__(self):
        return len(self.deck)
    
    #Use the random.shuffle() method to shuffle the list of cards in place
    def shuffle_cards(self):
        random.shuffle(self.deck)

    #Use the pop() built in method for lists to remove the 
    def draw_card(self):
        #Remove the card from the end of the list, which would be the "top" card.  This isn't really necessary since the order is randomized, but it's fun.
        return self.deck.pop(-1)

#Create a Hand class
class Hand():
    #Initialize the Hand object by creating an empty hand with no value
    def __init__(self):
        #Initialize the hand variable to hold a list of cards as part of the Hand class
        self.hand = []
        self.hand_value = 0
        self.aces = 0
    
    def draw_hand(self, number_to_draw, deck: Deck):
        self.number_to_draw = number_to_draw
        for _ in range(number_to_draw):
            card = deck.draw_card()
            self.hand.append(card)
            self.hand_value += VALUES[card.rank]
            if card.rank == "Ace":
                self.aces += 1
    
    def add_card(self, card: Card):
        self.hand.append(card)
        self.hand_value += VALUES[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def check_aces(self):
        while (self.hand_value > 21) and (self.aces > 0):
            self.hand_value -= 10
            self.aces -= 1
    
    def __str__(self):
        hand_contents = ""

        for card in self.hand:
            hand_contents += card.__str__() + "\n"
        return hand_contents

class Chips():
    def __init__(self):
        self.total_bank = int(input("Enter starting pot value: "))
        self.bet = 0

    def win_bet(self):
        self.total_bank += self.bet
    
    def lose_bet(self):
        self.total_bank -= self.bet



##### TEST #####
myDeck = Deck()
myDeck.shuffle_cards()
#print(myDeck)

myHand = Hand()
myHand.draw_hand(2, myDeck)
#myHand.add_card(myDeck.draw_card())
#testAce = Card("Hearts", "Ace")
#myHand.add_card(testAce)
#myHand.add_card(myDeck.draw_card())
myHand.check_aces()

print(myHand)
print(f"Value: {myHand.hand_value}")
print(f"Cards left in deck: {len(myDeck)}")



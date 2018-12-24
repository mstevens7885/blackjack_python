import random

#GLOBAL VARIABLES
SUITS = ("Hearts", "Spades", "Clubs", "Diamonds")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
VALUES = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

#Create a Card class
class Card():
    '''
    DESCRIPTION: Card object used to represent a playing card
    INPUTS: the card's suit and the card's rank
    ATTRIBUTES: suit, rank
    METHODS: None
    SPECIAL FUNCTIONS: __str__()
    '''
    #Define the two attributes of a card: suit and rank
    def __init__(self, suit: str, rank: str):
        #Initialize suit and rank variables as part of the Card class, with the suit and rank attributes passed to the class
        self.suit = suit
        self.rank = rank   
    
    #Create the string definition of the object as: "Rank of Suit"
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Create a Deck class
class Deck():
    '''
    DESCRIPTION: Deck object used to represent a deck of cards, populated by card objects that are created from the global variables
    INPUTS: None
    ATTRIBUTES: cards
    METHODS: shuffle_cards(), draw_card() 
    SPECIAL FUNCTIONS: __str__(), __len__()
    '''
    #Initialize the Deck object by creating the 52 card deck out of Card objects
    def __init__(self):   
        #Initializes the cards variable, which is a list that will contain Card objects
        self.cards = []

        #For each suit in the GLOBAL VARIABLE suits
        for suit in SUITS:
            #For each suit in the GLOBAL VARIABLE suits
            for rank in RANKS:
                #Add a Card object of suit and rank to the self.deck variable
                self.cards.append(Card(suit, rank))
    
    #Create a string representation of self.cards to report back when the deck is called as a string
    def __str__(self):
        #Create an empty string for the deck contents
        deck_contents = ""

        #For each Card object in self.deck.  The card variable is just the variable used for iteration of all self.deck Card objects in this case.
        for card in self.cards:
            #Add the string definition of each Card object to the deck contents string.  The string definition is: f"{Card.rank} of {Card.suit}"
            deck_contents += card.__str__() + "\n"
        #Return the deck_contents string
        return deck_contents
    
    #Create a length representation of self.cards to report back when the length of the deck is requested
    def __len__(self):
        return len(self.cards)
    
    #Use the random.shuffle() method to shuffle the deck object, which is a list of card objects, in place
    def shuffle_cards(self):
        '''
        DESCRIPTION: Shuffle the self.cards object list in place
        INPUT: None
        OUTPUT: None
        '''
        random.shuffle(self.cards)

    #Use the pop() built in method for lists to remove a card object from the deck list and return the card object
    def draw_card(self):
        '''
        DESCRIPTION: Remove a card object from the self.cards list and return the object
        INPUT: None
        OUTPUT: Returns the card object at the end of the self.cards list
        '''
        try:
            #Remove the card from the end of the list, which would be the "top" card.  This isn't really necessary since the order is randomized, but it's fun.
            return self.cards.pop(-1)
        except IndexError:
            print("There are no cards to draw")

#Create a Hand class
class Hand():
    '''
    DESCRIPTION: Hand object used to represent a player's hand of cards
    INPUTS: None
    ATTRIBUTES: hand, hand_value, aces
    METHODS: None
    SPECIAL FUNCTIONS: __str__()
    '''
    #Initialize the Hand object by creating an empty hand with no value
    def __init__(self):
        #Initialize the hand variable to hold a list of cards as part of the Hand class
        self.hand = []
        #Initialize the hand_value variable to track the value of the hand
        self.hand_value = 0
        #Initialize the aces variable to track the number of aces
        self.aces = 0

    def __str__(self):
        hand_contents = ""

        for card in self.hand:
            hand_contents += card.__str__() + "\n"
        return hand_contents

    #Create a length representation of self.hand to report back when the length of the hand is requested
    def __len__(self):
        return len(self.hand)
    
    def draw_hand(self, number_to_draw, deck: Deck):
        '''
        DESCRIPTION: Removes a specified number of card objects from the deck object, and adds them to the hand object
        INPUT: the number of cards to draw, the deck object to draw the card objects from
        OUTPUT: None
        '''
        #Loop through the specified number_to_draw range
        #############################################################LEFT OFF HERE
        for _ in range(number_to_draw):
            try:
                #Set the card variable equal to the returned value of the draw_card() method from the Deck class, which is a Card object
                card = deck.draw_card()
                #Add the card object to the hand object
                self.hand.append(card)
                #Add the card's value to the hand's value, which is determined from the global VALUES dictionary that contains each rank's value
                self.hand_value += VALUES[card.rank]
                #If the card's rank is "Ace", add to the self.aces counter
                if card.rank == "Ace":
                    self.aces += 1
            except:
                print("The deck has no more cards!")
                break
            
    def add_card(self, card: Card):
        self.hand.append(card)
        self.hand_value += VALUES[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def check_aces(self):
        while (self.hand_value > 21) and (self.aces > 0):
            self.hand_value -= 10
            self.aces -= 1


class Chips():
    def __init__(self):
        self.total_bank = int(input("Enter starting bet value: "))
        self.bet = 0

    def win_bet(self):
        self.total_bank += self.bet
    
    def lose_bet(self):
        self.total_bank -= self.bet
    
    def __str__(self):
        return f"Value of the pot is: {self.total_bank}"

def make_bet(Chips):
    while True:
        try:
            Chips.bet = int(input("Enter your bet: "))
        except:
            print("Please enter a positive integer value.")
        
    return Chips.bet





##### TEST DECK #####
myDeck = Deck()
myDeck.shuffle_cards()
print(f"Your Deck: \n{myDeck}")


myHand = Hand()
myHand.draw_hand(54, myDeck)
#myHand.add_card(myDeck.draw_card())
#testAce = Card("Hearts", "Ace")
#myHand.add_card(testAce)
#myHand.add_card(myDeck.draw_card())
myHand.check_aces()

#myChips = Chips()
#myChips.bet = 100
#myChips.win_bet()
#print(myChips)

print(myHand)
print(f"Value: {myHand.hand_value}")
print(f"Cards left in deck: {len(myDeck)}")



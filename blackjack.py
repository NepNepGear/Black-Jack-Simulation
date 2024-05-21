import random

# Define a deck of cards. In blackjack, Jacks, Queens, and Kings are all worth 10.
# Aces can be worth 11 or 1, depending on the hand. This list represents a standard deck of 52 cards.
DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# This would be the storage of both your hand and the dealer's hand
your_Hand = []
the_Dealer = []

# Function to draw a card from the deck
def draw_card(deck, infinite=True):
    # If infinite is True, draw a card without removing it from the deck
    # This simulates an infinite deck scenario, where the probability of drawing any card is always the same
    if infinite:
        return random.choice(DECK)
    else:
        # If infinite is False, draw a card and remove it from the deck
        # This simulates a realistic scenario where the deck gets smaller as cards are drawn
        card = random.choice(deck)
        deck.remove(card)
        return card


# Function to calculate the value of a hand in blackjack
def hand_value(hand):
    # Sum the values of all cards in the hand
    value = sum(hand)
    # Count the number of aces in the hand
    aces = hand.count(11)

    # While the total value exceeds 21 and there are aces in the hand
    # Convert some aces from 11 to 1 (by subtracting 10 from total value)
    # This is done to prevent busting (going over 21)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def blackjack_game(infinite):
    # whos_Turn = true is the player's turn
    # whos_Turn = false is the dealer's turn
    
    whos_Turn = bool(True)
    
    # Your First card is drawn automatically
    your_Hand.append(draw_card(DECK,infinite))
    
    print('You Start with: ' + str(hand_value(your_Hand)))
    
    print("The Player's Turn:")
    
    #This is the player's turn
    while whos_Turn == True and hand_value(your_Hand) <= 21 :
        
        # Give the player their hand value and the prompt to say if they want to hit or not
        user_input = input("Do you Hit? True or False: ")
        if user_input == "True":
            your_Hand.append(draw_card(DECK,infinite))
            print(hand_value(your_Hand))
        else:
            whos_Turn = bool(False)
        
        # if the player goes over 21 then the player loses
        if hand_value(your_Hand) > 21:
            return False
    
    #This is the Dealer's turn
    print("The Dealer's Turn:")
    
    while whos_Turn == False and hand_value(the_Dealer) <= 21 :
        
        # If the dealer has not gone 21 and the dealer's hand is smaller than your hand
        if hand_value(the_Dealer) <= 21 and hand_value(the_Dealer) <= hand_value(your_Hand):
            # Give the dealer a card and print that number so the player can see
            the_Dealer.append(draw_card(DECK,infinite))
            print(hand_value(the_Dealer))
        else:
            # then end the dealer's turn
            whos_Turn = bool(True)
        
        # If the dealer goes over 21 then the player wins      
        if hand_value(the_Dealer) > 21:
            return True


# Tempory Main system of the game.
# player = True would be infinite system 
# player = False would be 52 cards system 

player = bool(False)

# The actual Game
gameresult = blackjack_game(player)

# Displays who wins
if gameresult == True:
    print("The Player Wins")
else:
    print("The House Always Wins. You lose")

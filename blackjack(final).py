import random

# Define a deck of cards. In blackjack, Jacks, Queens, and Kings are all worth 10.
# Aces can be worth 11 or 1, depending on the hand. This list represents a standard deck of 52 cards.
DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Backup deck just in case we are using the non infinity deck
COPYDECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

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

def isHard(hand):
    aces = hand.count(11)
    if aces > 0:
        return False
    else:
        return True

def blackjack_game(infinite,policy):
    # whos_Turn = true is the player's turn
    # whos_Turn = false is the dealer's turn

    whos_Turn = bool(True)
    
    # Your and dealer First two cards are drawn automatically


    your_Hand.append(draw_card(DECK, infinite))
    your_Hand.append(draw_card(DECK, infinite))
    the_Dealer.append(draw_card(DECK, infinite))
    the_Dealer.append(draw_card(DECK, infinite))


    #print('Your starting hand: ' + str(your_Hand) + ' with value: ' + str(hand_value(your_Hand)))
    #print("Dealer's visible card: " + str(the_Dealer[0]))

    while hand_value(your_Hand) <= 21:
        # Policy 1: If the hand value is 17 or higher, do not draw any more cards ("stick").
        if policy == 1:
            if hand_value(your_Hand) >= 17:
                whos_Turn = False
                break
            #Else pick up more cards
            else:
                your_Hand.append(draw_card(DECK, infinite))
        # Policy 2: Conditions for a more nuanced approach
        elif policy == 2:
            # If the hand is "hard" (no Ace counted as 11) and the value is 17 or more, stick. OR stick if the hand value exactly equals 21. 
            if hand_value(your_Hand) >= 17 and isHard(your_Hand):
                whos_Turn = False
                break
            elif hand_value(your_Hand) == 21:
                whos_Turn = False
                break
            else:
                 your_Hand.append(draw_card(DECK, infinite))
        # Policy 3: Always stick regardless of the hand value
        elif policy == 3:
            whos_Turn = False    
            break
        # If none of the above conditions are met, draw another card
        else:
            your_Hand.append(draw_card(DECK, infinite))
            #print('Your hand: ' + str(your_Hand) + ' with value: ' + str(hand_value(your_Hand)))
            if hand_value(your_Hand) > 21:
                #print("Busted! Your hand value is over 21.")
                return False


    #print('Your hand: ' + str(your_Hand) + ' with value: ' + str(hand_value(your_Hand)))
    
    # This is the Dealer's turn
    #print("The Dealer's Turn:")

    while whos_Turn == False and hand_value(the_Dealer) <= hand_value(your_Hand) and hand_value(the_Dealer) <= 21:

        the_Dealer.append(draw_card(DECK, infinite))
        #print("Dealer's hand: " + str(the_Dealer) + ' with value: ' + str(hand_value(the_Dealer)))
        if hand_value(the_Dealer) > 21:
            #print("Dealer busted! You win.")
            return True
    


print("Select deck type:")
print("1. Infinite deck (cards are replaced after draw)")
print("2. Single deck (cards are not replaced, deck is finite)")
deck_choice = int(input("Choose deck type (1 or 2): "))


print("Select a policy for playing:")
print("1. Stick if hand ≥ 17, else hit.")
print("2. Stick if hand ≥ 17 and is hard, else hit unless hand = 21.")
print("3. Always stick.")
selected_policy = int(input("Choose policy (1, 2, or 3): "))

print("Select deck type:")
print("1. 100,000 Games")
print("2. 1,000,000 Games")
simulategames = int(input("Choose how many simulations (1 or 2): "))

# Tempory Main system of the game.
# player = True would be infinite system
# player = False would be 52 cards system

i = 0;
wins = 0;
lose = 0;
amount_Of_Games = 0

if simulategames == 1:
    amount_Of_Games = 100000
elif simulategames == 2:
    amount_Of_Games = 1000000

infinite = True if deck_choice == 1 else False

while i < amount_Of_Games:
    # The actual Game
    gameresult = blackjack_game(infinite,selected_policy)

    # Displays who wins
    if gameresult == True:
        #print("The Player Wins")
        wins = wins + 1
    else:
        #print("The House Always Wins. You lose")
        lose = lose + 1
    
    i = i + 1
    
    #clear all arrays so it can be reused for the next game
    your_Hand.clear()
    the_Dealer.clear()
    DECK.clear()
    DECK = COPYDECK.copy()

print("The win rate out of " + str(amount_Of_Games) + " is: " + str(wins/amount_Of_Games))
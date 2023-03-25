############### Blackjack Project #####################
import random
import os
from tabnanny import check
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### functions #####################
def pick(name):
    for i in range (2):
        name.append (random.choice(cards))
    return name

def  check_ace (hand_list):
    s= sum(hand_list)
    if 11 in hand_list and s> 21:
        # s -= 10
        hand_list[hand_list.index(11)]=1
    return hand_list


def want_new_card ():
    ans = input ("do you want another card? 'y'or 'n' :").lower()
    while not (ans == 'y' or ans == "n"):
        ans = input ("do you want another card? 'y'or 'n' :").lower()
    if ans == "y":
        return True
    else:
        return False


##################### main #####################
wanna_play = True

while wanna_play:
    if input("Do you want to play BlackJack?'y' or 'n'?")=="y":
        wanna_play = True
        os.system("cls")
    else:
        wanna_play = False
    print (logo)
    
    #pick cards for player
    player_cards=[]
    dealer_cards=[]

    pick(player_cards)
    player_score= sum(player_cards)
    print(f"Your cars: {player_cards} , and your  score: {player_score}.")
    
    #pick card for dealer
    pick(dealer_cards)
    dealer_score = sum(dealer_cards)
    print(f"Fisrst card of  dealer is {dealer_cards[0]}.")


    while want_new_card () and player_score<21:
        player_cards.append(random.choice(cards))
        player_cards = check_ace(player_cards)
        player_score = sum(player_cards)
        print(f"Your cars: {player_cards} , and your  score: {player_score}.")
    
    if player_score > 21:
        print ("you lose")
    else:
        while dealer_score <17:
            dealer_cards.append(random.choice(cards))
            dealer_cards = check_ace(dealer_cards)
            dealer_score = sum(dealer_cards)
        print (f"compuer score is:{dealer_score}, and hand {dealer_cards}")
        if dealer_score > 21:
            print("Computer lose!")
        elif (player_score - dealer_score > 0):
            print("Player Won!")
        elif (player_score - dealer_score == 0):
            print("Player Won!")
        else:
            print("Computer Won!")
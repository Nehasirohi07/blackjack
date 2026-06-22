
import random

Rank = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
suits = ["Heart","Diamond","Clubs","Spades"] 


def create_deck(): 
    deck = []

    for i in suits:
        for j in Rank:
            deck.append(f"{j}{i[0]}")

    random.shuffle(deck)
    return deck 



def calculate(hands):
    total = 0
    aces = 0
    for card in hands:
        rank = card[:-1]

        if rank in ["J","K","Q"]:
            total += 10
    
        elif rank == "A":
            total += 11
            aces += 1
    
        else:
            total += int(rank)
        
    while total > 21 and  aces > 0:
            total -= 10
            aces -= 1
    


    return total


def player_turn(player_hand,deck):
     
    while True:
        print("\nPlayer Hand:", player_hand)
        print("Player Score:", calculate(player_hand))

        choice = input("Hit or Stand? ").lower()

        if choice == "hit":
            player_hand.append(deck.pop())

        if calculate(player_hand) > 21:
            print("\nPlayer Hand:", player_hand)
            print("Player Score:", calculate(player_hand))
            print("Bust! Dealer wins.")
            return False

        elif choice == "stand":
            return True

        else:
            print("Enter hit or stand.")

def dealer_turn(dealer_hand,deck):

    while calculate(dealer_hand)< 17:
         dealer_hand.append(deck.pop())


def determine_winner(player_hand,dealer_hand):

    player_score = calculate(player_hand)
    dealer_score = calculate(dealer_hand)

    print("\nFinal Hands")
    print("palyer:",player_hand)
    print("player score:",player_score)

    print("dealer:",dealer_hand)
    print("dealer score:",dealer_score) 

    if player_score > 21:
        print("player busts! dealer wins.")

    elif dealer_score > 21:
        print("dealer busts! player wins.")

    elif player_score > dealer_score:
        print("player wins.")

    elif dealer_score > player_score:
        print("dealer wins.")

    else:
        print("push(tie)")

def main():
    deck = create_deck()

    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print("player:",player_hand)
    print("dealer:",dealer_hand)

    player_alive = player_turn(player_hand,deck)

    if player_alive:
        dealer_turn(dealer_hand,deck)
        determine_winner(player_hand,dealer_hand)

main()


# main()
# Testing For Multi Commit
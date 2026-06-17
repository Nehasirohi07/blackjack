def calculate(hand):
    total=0
    aces=0
    
    for card in hand:
        if card in ['K','J','Q']:
            total = total + 10
        elif card =='A':
            aces += 1
            total +=11

        else:
            total = total + card
    while total > 21 and aces > 0:
        total-=10
        aces-=1
    return total
def blackjack(hand_1,hand_2):
    total_1 = calculate(hand_1)
    total_2 = calculate(hand_2)
    if total_1> 21:
        print("hand_2 wins")
    elif total_2> 21:
        print("hand_1 wins")
    elif total_1>total_2:
        print("hand_1 wins")
    elif total_2>total_1:
        print("hand_2 wins")
    else:
        print("tie")
blackjack([1,'K',2],['J','Q','K'])



import random as r
import time as tell

card_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["♠","♣","♥","♦"]
cards = []
unshuffled_cards = []
hands = []
visible_hands = []
middle_card = "<error>"
player_ended = False

for possible in range(len(card_values)):
    for suits_available in range(len(suits)):
        card = card_values(possible),suits[suits_available]
        cards.insert(0, card)

def modify_hand(hand_number, hands_list, pos_in_hand, new_value):
    """
        Returns hand list with the correct hand modified in the way specified. All parameters must be filled in for correct result.
    """
    modified_hand = hands_list[hand_number-1]
    modified_hand[pos_in_hand-1] =  new_value
    hand_list_mod = hands_list
    hand_list_mod[pos_in_hand-1] = modified_hand
    return hand_list_mod

def isInt(value):
    """
        Return True only if the value is an integer, and between 1-9.
    """
    try:
        test = int(value)
        if test < 9 and test > 1:
            return True
        else:
            return False
    except ValueError:
        return False

def get_non_duplicate():
    """
        Returns card that has not yet been dealt, or shuffles and then deals one of the cards which have been shuffled.
    """
    global unshuffled_cards
    global cards
    if len(unshuffled_cards) == len(cards):
        unshuffled_cards = []
        for i in range(len(hands)):
            current_hand = hands[i]
            for x in range(len(current_hand)):
                unshuffled_cards.insert(len(unshuffled_cards), current_hand[x]) #Add all of the cards currently in player hands into the unshuffled cards list, to prevent duplicate cards from being dealt.
    card_choice = cards[r.randint(len(cards))]
    while card_choice in unshuffled_cards:
        card_choice = cards[r.randint(len(cards))]
    return card_choice
    
def deal():
    """
        Returns hand with no possible duplicates resulting in other hands. This creates result of max players being <= 4.
    """
    global unshuffled_cards
    global cards
    hand = []
    for x in range(9):
        card = get_non_duplicate()
        unshuffled_cards.insert(len(unshuffled_cards), card)
        hand.insert(len(hand), card)
    return hand

def flip_card():
    global visible_hands
    print("1-9 starting in top left, ending bottom right")
    flip_cardA = input("Which card would you like to flip? : ")
    while isInt(flip_cardA) == False:
        flip_cardA = input("Which card would you like to flip? : ")
    if visible_hands[x][flip_cardA-1] != hands[x][flip_cardA-1]:
        v_hand = visible_hands[x]
        v_hand[flip_cardA-1] = hands[x][flip_cardA-1]
        visible_hands[x] = v_hand
    else:
        print("INVALID FLIP: [Reason: Card already flipped]")
        print("TRY AGAIN!")
        flip_card()

def takeTurn(hand_number):
    global hands
    global unshuffled_cards
    global middle_card
    global player_ended
    print("Middle card:", middle_card, sep=" ", end=".\n")
    print("\"Draw\" or \"Take\" (take = take middle card)")
    choice = input(" -> ")
    while choice.lower() != "draw" and choice.lower() != "take":
        print("\"Draw\" or \"Take\" (take = take middle card)")
        choice = input(" -> ")
    if choice.lower() == "draw":
        drawn_card = get_non_duplicate()
        unshuffled_cards.insert(len(unshuffled_cards), drawn_card)
        print("You drew:", drawn_card, sep=" ", end=".\n")
        t.sleep(1)
        print("Will you \"Replace\" or \"Flip\"?")
        choice = input(" -> ")
        while choice.lower() != "replace" and choice.lower() != "flip":
            print("Will you \"Replace\" or \"Flip\"?")
            choice = input(" -> ")
        if choice.lower() == "replace":
            print("Which card will you replace?")
            choice = input(" -> ")
            while isInt(choice) == False:
                print("Which card will you replace?")
                choice = input(" -> ")
            choice = int(choice)
            middle_card = hands[hand_number][choice]
            hands = modify_hand(hand_number, hands, choice, drawn_card)
            visible_hands[hand_number][choice] = modify_hand(hand_number, visible_hands, choice, drawn_card)
            print("Your new hand:\n" + visible_hands[hand_number])
        elif choice.lower() == "flip":
            flip_card()
    elif choice.lower() == "take":
        print("Which card will you replace?")
        choice = input(" -> ")
        while isInt(choice) == False:
            print("Which card will you replace?")
            choice = input(" -> ")
        choice = int(choice)
        middle_card = hands[hand_number][choice]
        hands = modify_hand(hand_number, hands, choice, drawn_card)
        visible_hands[hand_number][choice] = modify_hand(hand_number, visible_hands, choice, drawn_card)
        print("Your new hand:\n" + visible_hands[hand_number])
    if not "-" in visible_hands[hand_number]:
        player_ended = hand_number

def main(num_of_players):
    """
        Runs the game.
    """
    global unshuffled_cards
    global cards
    global hands
    global visible_hands
    global middle_card
    for x in range(num_of_players):
        hand = [x, deal()] #hand 0 (1)
        hands.insert(len(hands),hand)
        visible_hands.insert(x, "---\n---\n---")
        flip_card()
        flip_card()
    middle_card = get_non_duplicate()
    unshuffled_cards.insert(len(unshuffled_cards), middle_card)
    x = 0
    while True:
        if len(hands) < x:
            x = 0
        current = hands[x]
        if player_ended == x:
            break
        takeTurn(x)
    for x in range(num_of_players):
        print(x + "\'s hand:\n" + hands[x])
    print("Now you can determine who wins!") #Automatic system coming after this is confirmed working without it.
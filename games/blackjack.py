import random
from games.helper import get_stake

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def create_deck():
    """Hiermee wordt het spel kaarten gemaakt"""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{suit}{rank}")
    return deck

def draw_card(deck,hand):
    """Met deze functie wordt een nieuwe kaart getrokken"""
    card = deck.pop()
    hand.append(card)
    return card

def show_hand(label, hand, hide_card=False):
    """Deze functie laat een hand zien en door hide_card True mee te geven wordt 1 van de 2 kaarten verborgen"""
    if hide_card:
        visible_cards = hand[:1] + ["??"]
    else:
        visible_cards = hand
    print(f"{label}: {' | '.join(visible_cards)}")

def calculate_card_value(card):
    """Hiermee wordt de waarde van een kaart berekend"""
    rank = card[1]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    """Hiermee wordt de waarde van een hand berekend"""
    total = 0
    number_of_aces = 0
    for card in hand:
        if card[1] == "A":
            number_of_aces += 1

    for card in hand:
        total += calculate_card_value(card)

    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1

    return total

def play_blackjack(balance):
    """Standaard functie om Blackjack mee te spelen"""
    deck = create_deck()
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []

    stake = get_stake(balance)
    if stake == 0:
        return balance
    balance -= stake

    draw_card(deck, player_hand)
    draw_card(deck, player_hand)

    draw_card(deck, dealer_hand)
    draw_card(deck, dealer_hand)

    show_hand("Jouw hand", player_hand)
    show_hand("Dealer hand", dealer_hand, True)

    player_value = calculate_hand_value(player_hand)
    print(f"Jouw totaal: {player_value}")

    while calculate_hand_value(player_hand) < 21:
        choice = input("Kies hit of stand: ")
        if choice == "stand":
            break
        elif choice == "hit":
            card = draw_card(deck, player_hand)
            print(f"Je trekt: {card}")
            show_hand("Jouw hand", player_hand)

            player_value = calculate_hand_value(player_hand)
            print(f"Jouw totaal: {player_value}")
            if player_value > 21:
                print("Je bent bust!")
                return balance
        else:
            print("Geen geldige keuze")
            continue

    show_hand("Dealer hand", dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        card = draw_card(deck, dealer_hand)
        print(f"Dealer trekt: {card}")
        show_hand("Dealer hand", dealer_hand)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Jouw totaal: {player_value}")
    print(f"Dealer totaal: {dealer_value}")

    if dealer_value > 21:
        balance += stake * 2
        print(f"""De dealer bust!\nNieuw saldo: € {balance:.2f}""")
    elif player_value > dealer_value:
        balance += stake * 1.5
        print(f"""Je wint van de dealer!\nNieuw saldo: € {balance:.2f}""")
    elif player_value == dealer_value:
        balance += stake
        print(f"""Gelijk met de dealer!\nNieuw saldo: € {balance:.2f}""")
    elif player_value < dealer_value:
        print(f"""De dealer wint!\nNieuw saldo: € {balance:.2f}""")

    return balance

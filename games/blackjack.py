import random
from games.helper import get_stake

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def create_deck():
    """Maak en schud een volledig blackjackdeck.

    Returns:
        list: Een geschud deck met 52 kaarten.
    """
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{suit}{rank}")
    return deck

def draw_card(deck,hand):
    """Trek een kaart uit het deck en voeg deze toe aan een hand.

    Parameters:
        deck (list): Het huidige deck met beschikbare kaarten.
        hand (list): De hand waaraan de getrokken kaart wordt toegevoegd.

    Returns:
        str: De kaart die uit het deck is getrokken.
    """
    card = deck.pop()
    hand.append(card)
    return card

def show_hand(label, hand, hide_card=False):
    """Toon de kaarten in een hand en verberg eventueel de tweede kaart.

        Parameters:
            label (str): Het label dat voor de hand wordt weergegeven.
            hand (list): De kaarten in de hand.
            hide_card (bool): Bepaalt of de tweede kaart verborgen wordt.
        """    if hide_card:
        visible_cards = hand[:1] + ["??"]
    else:
        visible_cards = hand
    print(f"{label}: {' | '.join(visible_cards)}")

def calculate_card_value(card):
    """Bereken de waarde van één blackjackkaart.

        Parameters:
            card (str): De kaart waarvan de waarde bepaald wordt.

        Returns:
            int: De waarde van de kaart.
        """    rank = card[1]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    """Bereken de totale waarde van een blackjackhand en verwerk eventuele azen.

        Parameters:
            hand (list): De kaarten in de blackjackhand.

        Returns:
            int: De totale waarde van de hand.
        """    total = 0
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
    """Start een blackjackspel en bepaalt het nieuwe saldo van de speler.

    Parameters:
        balance (float): Het huidige saldo van de speler.

    Returns:
        float: Het nieuwe saldo na afloop van het blackjackspel.
    """
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

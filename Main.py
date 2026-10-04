from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette
from games.blackjack import play_blackjack
from games.helper import show_account
from Profiles import *

ENTRY = 12.0
FLIPFLOPS = 5.0
SUNGLASSES = 7.0

total_cost = ENTRY + FLIPFLOPS + SUNGLASSES

def show_balance(balance):
    """Toon het huidige saldo van de speler.

    Parameters:
        balance (float): Het huidige saldo van de speler.
    """
    print(f"Huidig saldo: € {balance:.2f}")

def show_main_menu():
    """Toon het hoofdmenu van het casino."""
    print("""Casino de Gouden Driehoek - hoofdmenu
-------------------------------------
1. Spellen
2. Saldo
3. Account
0. Stop""")

def show_games_menu():
    """Toon het menu met de beschikbare casinospellen."""
    print("""Casino de Gouden Driehoek - spellen
-----------------------------------
1. Fruitmachine
2. Roulette
3. Blackjack
0. Terug""")

def show_account_menu():
    """Toon het account menu van het casino."""
    print("""Casino de Gouden Driehoek - account
------------------------------------
1. Toon alle accounts
2. Nieuw account
3. Wissel account
4. Verwijder account
0. Terug""")

def initialize_player(total_cost):
    global players
    global current_player

    # players = create_start_players()  # Deze functie is bonus
    firstname = input("Voornaam: ").capitalize()
    lastname = input("Achternaam: ").capitalize()
    name = firstname + " " + lastname
    current_player = name

    if name in players:
        profile = players[current_player]
        salutation = determine_salutation(profile["firstname"], profile["lastname"], profile["gender"])
        balance = profile["saldo"]
        print(f"""Casino de Gouden Driehoek
-------------------------
Welkom terug, {salutation}

huidige saldo: € {available_budget:.2f}""")

    else:
        profile, budget_statement = create_account(players, total_cost, name, firstname, lastname)
        profile = players[current_player]
        balance = profile["balance"]
        startbudget = balance + total_cost  # Het startbudget wordt opnieuw berekend omdat create_account alleen het saldo na de vaste kosten opslaat. Total_cost is een parameter van deze functie
        print(profile["gender"])
        salutation = determine_salutation(profile["firstname"], profile["lastname"], profile["gender"])
        show_welcome_message(startbudget, balance, salutation, total_cost, budget_statement)

    return profile, balance

def main():
    """Start het casino en verwerkt het hoofdmenu van de applicatie."""

    profile, balance = initialize_player(total_cost)
    while True:
        show_main_menu()
        choice_main = int(input("Maak een keuze (0 om te stoppen): "))
        match choice_main:
            case 0:
                break
            case 1:
                while True:
                    show_games_menu()
                    choice_game = int(input("Maak een keuze (0 om te stoppen): "))
                    match choice_game:
                        case 0:
                            break
                        case 1:
                            balance = play_fruitmachine(balance)
                        case 2:
                            balance = play_roulette(balance)
                        case 3:
                            balance = play_blackjack(balance)

            case 2:
                show_balance(profile["balance"])

            case 3:
                while True:
                    show_account_menu()
                    choice_account = int(input("Maak een keuze (0 om te stoppen): "))
                    match choice_account:
                        case 0:
                            break
                        case 1:
                            pass

if __name__ == "__main__":
    main()
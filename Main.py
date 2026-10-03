from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette
from games.blackjack import play_blackjack
from games.helper import show_account

ENTRY = 12.0
FLIPFLOPS = 5.0
SUNGLASSES = 7.0

TOTAL_COST = ENTRY + FLIPFLOPS + SUNGLASSES

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

def main():
    """Start het casino en verwerkt het hoofdmenu van de applicatie."""
    firstname = input("Voornaam: ").capitalize()
    lastname = input("Achternaam: ").capitalize()
    name = firstname + " " + lastname

    show_welcome_message(startbudget, available_budget, salutation, total_costs, budget_statement)

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
                show_balance(balance)

            case 3:
                while True:
                    show_account_menu()
                    choice_account = int(input("Maak een keuze (0 om te stoppen): "))
                    match choice_account:
                        case 0:
                            break
                        case 1:

if __name__ == "__main__":
    main()
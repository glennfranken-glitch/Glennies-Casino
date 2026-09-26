from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette

def show_balance(balance):
    """Toon het huidige saldo van de speler."""
    print(f"Huidig saldo: € {balance:.2f}")

def determine_salutation(firstname, lastname, gender):
    """Bepaal de juiste aanspreekvorm op basis van naam en geslacht."""
    if gender == "m":
        salutation = f"meneer {lastname}"

    elif gender == "v":
        salutation = f"mevrouw {lastname}"

    else:
        salutation = f"{firstname} {lastname}"
    return salutation

def calculate_age(birthdate):
    """Bereken de leeftijd op basis van de geboortedatum."""
    birth_day, birth_month, birth_year = birthdate.split("-")
    birth_year = int(birth_year)
    age = 2026 - birth_year
    return age

def check_age(birthdate):
    """Controleer of de speler minimaal 18 jaar oud is."""
    age = calculate_age(birthdate)
    MIN_AGE = 18
    if age < MIN_AGE:
        print("Je bent helaas niet oud genoeg om het casino te betreden.")
        exit(1)
    return age

def show_welcome_message(startbudget, available_budget, salutation,total_costs,budget_statement):
    """Toon het welkomstbericht met budget en huidig saldo."""
    print(f"""Casino de Gouden Driehoek
    -------------------------
    Welkom, {salutation}

    Startbudget:    € {startbudget:.2f}
    Vaste kosten:   € {total_costs:.2f}
    Saldo:          € {available_budget:.2f}

    {budget_statement}""")

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
0. Terug""")

def show_account(firstname, lastname, birthdate, salutation):
    age = calculate_age(birthdate)

    print(f"""Naam: {firstname} {lastname}
Geboortedatum: {birthdate}
Aanspreekvorm: {salutation}
Leeftijd: {age}""")

def main():
    firstname = input("Voornaam: ").capitalize()
    lastname = input("Achternaam: ").capitalize()

    gender = input("Geslacht: (m/v)")
    birthdate = input("Geboortedatum: dd-mm-yyyy")
    check_age(birthdate)

    salutation = determine_salutation(firstname, lastname, gender)

    startbudget = float(input("Wat is je startbudget in euro's?"))

    #Vaste kosten
    ENTRY = 12.0
    FLIPFLOPS = 5.0
    SUNGLASSES = 7.0

    total_costs = ENTRY + FLIPFLOPS + SUNGLASSES
    available_budget = startbudget - total_costs

    if startbudget >= total_costs:
        budget_statement = "Je hebt nog genoeg budget voor toegang tot het casino."

    else:
        budget_statement = "Je hebt niet voldoende budget voor toegang tot het casino."
    balance = available_budget

    show_welcome_message(startbudget, available_budget, salutation, total_costs, budget_statement)

    while True:
        show_main_menu()
        choice_main = int(input("Maak een keuze (0 om te stoppen): "))
        match choice_main:
            case 0:
                break
            case 1:
                show_games_menu()
                while True:
                    choice_game = int(input("Maak een keuze (0 om te stoppen): "))
                    match choice_game:
                        case 0:
                            break
                        case 1:
                            balance = play_fruitmachine(balance)
                        case 2:
                            balance = play_roulette(balance)

            case 2:
                show_balance(balance)

            case 3:
                show_account()

if __name__ == "__main__":
    main()
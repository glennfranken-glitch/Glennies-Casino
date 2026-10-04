def get_stake(balance):
    while True:
        stake = float(input("Hoeveel wil je inzetten?(0 om te stoppen): "))

        if stake == 0:
            return 0

        elif stake < 0:
            print("Graag een geldige inzet invoeren")
            continue

        elif stake > balance:
            print("Zoveel geld hedde ge niet!")
            continue

        return stake

def show_account(firstname, lastname, birthdate, salutation):
    """Toon de accountgegevens van de speler.

    Parameters:
        name (str): De naam van de speler.
        birthdate (str): De geboortedatum van de speler.
        salutation (str): De aanspreekvorm van de speler.
    """
    age = calculate_age(birthdate)

    print(f"""Naam: {firstname} {lastname}
Geboortedatum: {birthdate}
Aanspreekvorm: {salutation}
Leeftijd: {age}""")

def get_name():
    firstname = input("Voornaam: ").capitalize()
    lastname = input("Achternaam: ").capitalize()
    name = firstname + " " + lastname
    return name, firstname, lastname

def get_current_balance(players, current_player):
    balance = players[current_player]["balance"]
    return balance

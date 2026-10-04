#Global
from games.helper import get_name

players = {}
current_player = None
played_games = None

def determine_salutation(firstname, lastname, gender):
    """Bepaal de juiste aanspreekvorm op basis van naam en geslacht.

    Parameters:
        lastname (str): De achternaam van de speler.
        firstname (str): De voornaam van de speler.
        gender (str): Het geslacht van de speler.

    Returns:
        str: De gekozen aanspreekvorm.
    """
    if gender == "m":
        salutation = f"meneer {lastname}"

    elif gender == "v":
        salutation = f"mevrouw {lastname}"

    else:
        salutation = f"{firstname} {lastname}"
    return salutation

def calculate_age(birthdate):
    """Bereken de leeftijd op basis van de geboortedatum.

    Parameters:
        birthdate (str): De geboortedatum van de speler in dd-mm-yyyy formaat.

    Returns:
        int: De berekende leeftijd van de speler.
    """
    birth_day, birth_month, birth_year = birthdate.split("-")
    birth_year = int(birth_year)
    age = 2026 - birth_year
    return age

def check_age(birthdate):
    """Controleer of de speler minimaal 18 jaar oud is.

    Parameters:
        age (int): De leeftijd van de speler.

    Returns:
        int: De leeftijd van de speler als deze minimaal 18 jaar oud is.
    """
    age = calculate_age(birthdate)
    MIN_AGE = 18
    if age < MIN_AGE:
        print("Je bent helaas niet oud genoeg om het casino te betreden.")
        exit(1)
    return age

def show_welcome_message(startbudget, balance, salutation,total_costs,budget_statement):
    """Toon het welkomstbericht met budget en huidig saldo.

    Parameters:
        startbudget (float): Het startbudget van de speler.
        available_budget (float): Het beschikbare budget na aftrek van de vaste kosten.
        salutation (str): De aanspreekvorm van de speler.
        total_cost (float): Het totaalbedrag van de vaste kosten.
        budget_statement (str): De conclusie over het beschikbare budget.
    Returns:
        str: welkomsbericht van het Casino
    """
    print(f"""Casino de Gouden Driehoek
-------------------------
Welkom, {salutation}

Startbudget:    € {startbudget:.2f}
Vaste kosten:   € {total_costs:.2f}
Saldo:          € {balance:.2f}

{budget_statement}""")

def create_start_players():
    global players
    players = {
    "Jan Jansen": {
        "firstname": "Jan",
        "lastname": "Jansen",
        "birthdate": "15-03-1990",
        "gender": "M",
        "balance": 100.00
    },
    "Piet Peters": {
        "firstname": "Piet",
        "lastname": "Peters",
        "birthdate": "22-07-1985",
        "gender": "M",
        "balance": 75.00
    },
    "Anna de Vries": {
        "firstname": "Anna",
        "lastname": "de Vries",
        "birthdate": "10-11-1995",
        "gender": "V",
        "balance": 150.00
    },
    "Lisa Bakker": {
        "firstname": "Lisa",
        "lastname": "Bakker",
        "birthdate": "03-02-2000",
        "gender": "V",
        "balance": 50.00
    },
    "Kees Smit": {
        "firstname": "Kees",
        "lastname": "Smit",
        "birthdate": "28-09-1978",
        "gender": "M",
        "balance": 200.00
    }
}
    return players

def create_profile(name, firstname, lastname, birthdate, gender, balance):
    """Maakt een nieuw profiel voor de speler.

    Parameters:
        name (str): De voornaam van de speler.
        birthdate (str): De geboortedatum van de speler.
        gender (str): Het geslacht van de speler.
        balance (float): Het beschikbare budget van de speler."""

    profile = {name: {"firstname": firstname, "lastname": lastname, "birthdate": birthdate, "gender": gender,
                      "balance": balance, "played games": played_games}}

    return profile

def create_account(total_cost, name = None, firstname = None, lastname = None):
    global current_player
    global players

    if name in players:
        print(f"Het account: {name} bestaat al. Gebruik 'Wissel Account' om het te openen")
        return

    gender = input("Geslacht(m/v): ")
    birthdate = input("Geboortedatum(dd-mm-yyyy): ")
    startbudget = float(input("Wat is je startbudget in euro's? "))

    check_age(birthdate)

    balance = startbudget - total_cost

    if balance >= total_cost:
        budget_statement = "Je hebt nog genoeg budget voor toegang tot het casino."

    else:
        budget_statement = "Je hebt niet voldoende budget voor toegang tot het casino."

    profile = create_profile(name, firstname, lastname, birthdate, gender, balance)
    players.update(profile)
    current_player = name
    return players, budget_statement

    #salutation = determine_salutation(firstname, lastname, gender)

def show_accounts(players):
    for player in players:
        print(player)

def switch_player():
    global current_player

    print("Beschikbare accounts:")
    {show_accounts(players)}

    name = input("Welk account wil je gaan gebruiken? ")
    if name in players:
        current_player = name
        return players[current_player]

    print("Account bestaat niet")

def delete_player():
    global current_player

    print("Beschikbare accounts:")
    show_accounts(players)

    name = input("Welk account wil je verwijderen? ")

    if name in players:
        del players[name]
        print(f"Account {name} is verwijderd.")

        if name == current_player:
            switch_player()

        return True

    print("Account bestaat niet.")
    return False

# #Test
# name = "Glenn Franken"
# firstname = "Glenn"
# lastname = "Franken"
# played_games = None
# players = {
#     "Jan Jansen": {
#         "firstname": "Jan",
#         "lastname": "Jansen",
#         "birthdate": "15-03-1990",
#         "gender": "M",
#         "balance": 100.00
#     },
#     "Piet Peters": {
#         "firstname": "Piet",
#         "lastname": "Peters",
#         "birthdate": "22-07-1985",
#         "gender": "M",
#         "balance": 75.00
#     },
#     "Anna de Vries": {
#         "firstname": "Anna",
#         "lastname": "de Vries",
#         "birthdate": "10-11-1995",
#         "gender": "V",
#         "balance": 150.00
#     },
#     "Lisa Bakker": {
#         "firstname": "Lisa",
#         "lastname": "Bakker",
#         "birthdate": "03-02-2000",
#         "gender": "V",
#         "balance": 50.00
#     },
#     "Kees Smit": {
#         "firstname": "Kees",
#         "lastname": "Smit",
#         "birthdate": "28-09-1978",
#         "gender": "M",
#         "balance": 200.00
#     }
# }
#
# ENTRY = 12.0
# FLIPFLOPS = 5.0
# SUNGLASSES = 7.0
#
# total_cost = ENTRY + FLIPFLOPS + SUNGLASSES
# #aanroepen te testen functies
# show_accounts(players)
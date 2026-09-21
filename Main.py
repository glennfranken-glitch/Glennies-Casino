firstname = input("Voornaam: ")
lastname = input("Achternaam: ")

firstname = firstname.capitalize()
lastname = lastname.capitalize()

birthdate = input("Geboortedatum: dd-mm-yyyy")

gender = input("Geslacht: (m/v)")
if gender == "m":
    salutation = f"meneer {lastname}"

elif gender == "v":
    salutation = f"mevrouw {lastname}"

else:
    salutation = f"{firstname} {lastname}"

startbudget = float(input("Wat is je startbudget in euro's?"))

birth_day, birth_month, birth_year = birthdate.split("-")
birth_year = int(birth_year)
age = 2026 - birth_year
MIN_AGE = 18
if age < MIN_AGE:
    exit(1)

#Vaste kosten
ENTRY = 12.0
FLIPFLOPS = 5.0
SUNGLASSES = 7.0

TOTALCOST = ENTRY + FLIPFLOPS + SUNGLASSES

AVAILABLE_BUDGET = startbudget - TOTALCOST

if startbudget >= TOTALCOST:
    budget_statement = "Je hebt nog genoeg budget voor toegang tot het casino."

else:
    budget_statement = "Je hebt niet voldoende budget voor toegang tot het casino."

print(f"""Casino de Gouden Driehoek
-------------------------
Welkom, {salutation}

Startbudget:    € {startbudget:.2f}
Vaste kosten:   € {TOTALCOST:.2f}
Saldo:          € {AVAILABLE_BUDGET:.2f}

{budget_statement}""")

balance = AVAILABLE_BUDGET


round_number = 1

while True:
    print("""Kies één van de volgende opties:

1. Rood
2. Zwart
3. Even
4. Oneven
0. Stop""")
    choice = int(input("Kies je gok (0 om te stoppen): "))
    if choice == 0:
        break
    else:
        stake = float(input("Hoeveel wil je inzetten?: "))
        if stake <= 0:
            print("Graag een geldige inzet invoeren")
            continue
        elif stake > balance:
            print("Zoveel geld hedde ge niet!")
            continue
        else:
            balance -= stake
        spin = (round_number * 7) % 37
        if spin == 0:
            color = groen
            odd_even = geen
        elif spin <= 18:
            if spin % 2 == 0:
                color = zwart
            else:
                color = rood
        else spin >18:
            if spin % 2 == 0:
                color = rood
            else:
                color = zwart
        win = False

firstname = input("Voornaam: ")
lastname = input("Achternaam: ")

firstname = firstname.capitalize()
lastname = lastname.capitalize()

birthday = input("Geboortedatum: dd-mm-yyyy")

gender = input("Geslacht: (m/v)")
if gender == "m":
    salutation = f"meneer {lastname}"

elif gender == "v":
    salutation = f"mevrouw {lastname}"

else:
    salutation = f"{firstname} {lastname}"

startbudget = round(float(input("Wat is je startbudget in euro's?")),2)

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

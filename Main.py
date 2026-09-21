firstname = input("Voornaam: ")
lastname = input("Achternaam: ")

firstname = firstname.capitalize()
lastname = lastname.capitalize()

birthday = input("Geboortedatum: dd-mm-yyyy")

gender = input("Geslacht: (m/v)")
if gender == "m":
    salutation = "meneer", lastname

elif gender == "v":
    salutation = "mevrouw", lastname

else:
    salutation = firstname, lastname

startbudget = round(float(input("Wat is je startbudget in euro's?")),2)

#Vaste kosten
ENTRY = round(float(12),2)
FLIPFLOPS = round(float(5),2)
SUNGLASSES = round(float(7),2)

TOTALCOST = round(ENTRY + FLIPFLOPS + SUNGLASSES,2)

AVAILABLE_BUDGET = round(startbudget - TOTALCOST,2)

if startbudget > TOTALCOST:
    budget_statement = "Je hebt nog genoeg budget voor toegang tot het casino."

else:
    budget_statement = "Je hebt niet voldoende budget voor toegang tot het casino."

print(f"""Casino de Gouden Driehoek
-------------------------
Welkom, {salutation}

Startbudget:    € {startbudget}
Vaste kosten:   € {TOTALCOST}
Saldo:          € {AVAILABLE_BUDGET}

{budget_statement}""")

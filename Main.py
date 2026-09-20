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

startbudget = float(input("Wat is je startbudget in euro's?"))

#Vaste kosten
ENTRY = float(12)
FLIPFLOPS = float(5)
SUNGLASSES = float(7)



print("""Casino de Gouden Driehoek
-------------------------
Welkom, meneer Jansen

Startbudget:    € 50.00
Vaste kosten:   € 16.50
Saldo:          € 33.50

Je hebt nog genoeg budget voor toegang tot het casino.""")

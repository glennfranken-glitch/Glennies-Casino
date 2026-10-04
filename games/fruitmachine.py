from games.helper import get_stake

def determine_rolls(round_number):
    """Bepaal de drie symbolen van de fruitmachine op basis van het ronde-nummer.

        Parameters:
            round_number (int): Het nummer van de huidige speelronde.

        Returns:
            tuple: De drie symbolen van de fruitmachine.
        """
    roll = round_number % 9

    match roll:
        case 0:
            return "kers", "kers", "kers"
        case 1:
            return "kers", "kers", "citroen"
        case 2:
            return "kers", "kers", "ster"
        case 3:
            return "kers", "citroen", "ster"
        case 4:
            return "kers", "citroen", "citroen"
        case 5:
            return "kers", "ster", "ster"
        case 6:
            return "citroen", "citroen", "citroen"
        case 7:
            return "citroen", "ster", "ster"
        case 8:
            return "ster", "ster", "ster"

def determine_payout(rol1, rol2, rol3, stake):
    """Bereken de uitbetaling op basis van de drie symbolen en de inzet.

        Parameters:
            rol1 (str): Het eerste symbool van de fruitmachine.
            rol2 (str): Het tweede symbool van de fruitmachine.
            rol3 (str): Het derde symbool van de fruitmachine.
            stake (float): Het bedrag dat de speler heeft ingezet.

        Returns:
            float: Het bedrag dat aan de speler wordt uitgekeerd.
        """
    roll_result = rol1 + rol2 + rol3
    if roll_result.count("citroen") == 2 or roll_result.count("ster") == 2 or roll_result.count("kers") == 2:
        stake = stake * 2
    elif roll_result.count("citroen") == 3 or roll_result.count("ster") == 3 or roll_result.count("kers") == 3:
        stake = stake * 3
    else:
        stake = 0
    return stake

def play_fruitmachine(balance):
    """Start het fruitmachine-spel en verwerkt de speelrondes.

        Parameters:
            balance (float): Het huidige saldo van de speler.

        Returns:
            float: Het nieuwe saldo na het fruitmachine-spel.
        """
    round_number = 1
    while True:
        choice = input(f"""Huidig saldo: € {balance:.2f}

Druk op enter om te spelen of typ stop om terug te gaan:""")
        match choice:
            case "stop":
                return balance

            case _:
                stake = get_stake(balance)
                if stake == 0:
                    return balance
                balance -= stake

                rol1, rol2, rol3 = determine_rolls(round_number)

                print(f"Rollen: {rol1} | {rol2} | {rol3}")

                payout = determine_payout(rol1, rol2, rol3, stake)
                if payout > 0:
                    balance += payout
                else:
                    print("Je hebt verloren")
                round_number += 1

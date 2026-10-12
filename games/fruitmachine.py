from games.helper import get_stake
import random
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

def determine_rolls():
    """Bepaal de drie symbolen van de fruitmachine op basis van een vaste set symbolen. Er worden random 3 gekozen

        Parameters:

        Returns:
            tuple: De drie symbolen van de fruitmachine.
        """
    symbols = "kers", "citroen", "ster"
    roll = random.choice(symbols), random.choice(symbols), random.choice(symbols)
    return roll

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

                rol1, rol2, rol3 = determine_rolls()
                table = Table(show_header=False)
                table.add_row(f"[gold]{rol1}[/]",f"[gold]{rol2}[/]",f"[gold]{rol3}[/]")

                panel = Panel.fit(table,
                                  title="[bold yellow]Fruitmachine-rollen[/]",
                                  border_style="gold1",
                                  padding=(1, 4))
                console = Console()
                console.print(panel)

                payout = determine_payout(rol1, rol2, rol3, stake)
                if payout > 0:
                    balance += payout
                    console = Console()
                    console.print(f"Je hebt [bold]{payout:.2f}[/] [bold green]gewonnen[/]")
                else:
                    console = Console()
                    console.print("Je hebt [red]verloren[/]")
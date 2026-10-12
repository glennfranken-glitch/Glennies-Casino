from games.helper import get_stake
import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def show_roulette():
    """Toon de beschikbare inzetmogelijkheden van roulette."""

    table = Table()
    table.add_column("[magenta]Optie[/]", justify="center", style="bold gold1")
    table.add_column("[magenta]Actie[/]")

    table.add_row("1.", "Rood")
    table.add_row("2.", "Zwart")
    table.add_row("3.", "Even")
    table.add_row("4.", "Oneven")
    table.add_row("0.", "Stop")
    panel = Panel.fit(table,
                      title="[bold yellow]Kies één van de volgende opties:[/]",
                      border_style="gold1",
                      padding=(1, 4))
    console = Console()
    console.print(panel)
    choice = int(input("Keuze: "))
    return choice

def determine_win(choice, color, odd_even):
    """Bepaal of de gekozen inzet overeenkomt met de uitkomst van de roulette.

        Parameters:
            choice (int): De keuze van de speler voor de inzet.
            color (str): De kleur waarop de roulette is gevallen.
            odd_even (str): Geeft aan of het getal even of oneven is.

        Returns:
            bool: True als de speler heeft gewonnen, anders False.
        """
    match choice:
        case 1:
            return color == "rood"
        case 2:
            return color == "zwart"
        case 3:
            return odd_even == "even"
        case 4:
            return odd_even == "oneven"
        case _:
            return False

def play_roulette(balance):
    """Start het roulette-spel en verwerkt de inzetten en spelrondes.

        Parameters:
            balance (float): Het huidige saldo van de speler.

        Returns:
            float: Het nieuwe saldo na het roulette-spel.
        """

    while True:
        console = Console()
        choice = show_roulette()
        if choice == 0:
            return balance

        stake = get_stake(balance)
        if stake == 0:
            return balance

        balance -= stake

        spin = random.randint(0, 36)
        if spin == 0:
            color = "groen"
            odd_even = "geen"

        elif spin <= 18:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "rood"
                odd_even = "oneven"

        else:
            if spin % 2 == 0:
                color = "rood"
                odd_even = "even"
            else:
                color = "zwart"
                odd_even = "oneven"

        win = determine_win(choice, color, odd_even)

        if win:
            balance = balance + stake * 2
            console.print(f"""De bal valt op {color} ({spin}).
Je [green]wint[/] €{stake:.2f}
[bold]Nieuw saldo: €{balance:.2f}[/]""")
        else:
            console.print(f"""De bal valt op {color} ({spin}).
            Je [red]verliest[/] €{stake:.2f}
            [bold]Nieuw saldo: €{balance:.2f}[/]""")

    print(f"Je eindigt met €{balance:.2f}")

    return balance
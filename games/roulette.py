def show_roulette():
    print("""Kies één van de volgende opties:

1. Rood
2. Zwart
3. Even
4. Oneven
0. Stop""")


def determine_win(choice, color, odd_even):
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
    round_number = 1

    while True:
        show_roulette()

        from games.helper import get_stake
        choice, stake = get_stake(balance)

        if choice == 0:
            break

        balance -= stake

        spin = (round_number * 7) % 37

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
            win_loss = "wint"
        else:
            win_loss = "verliest"

        print(f"""De bal valt op {color} ({spin}).
Je {win_loss} €{stake:.2f}
Nieuw saldo: €{balance:.2f}""")

        round_number += 1

    print(f"Je eindigt met €{balance:.2f}")

    return balance
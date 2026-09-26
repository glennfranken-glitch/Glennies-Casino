def get_stake(balance):
    while True:
        stake = float(input("Hoeveel wil je inzetten?(0 om te stoppen): "))

        if stake == 0:
            return 0, 0

        elif stake < 0:
            print("Graag een geldige inzet invoeren")
            continue

        elif stake > balance:
            print("Zoveel geld hedde ge niet!")
            continue

        return stake
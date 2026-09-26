def get_stake(balance):
    while True:
        choice = int(input("Kies je gok (0 om te stoppen): "))

        if choice == 0:
            return 0, 0

        stake = float(input("Hoeveel wil je inzetten?: "))

        if stake <= 0:
            print("Graag een geldige inzet invoeren")
            continue

        if stake > balance:
            print("Zoveel geld hedde ge niet!")
            continue

        return choice, stake
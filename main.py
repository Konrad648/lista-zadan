"""Lista zadań – prosta aplikacja konsolowa w Pythonie."""

zadania = []


def pokaz_zadania():
    """Wyświetla wszystkie zadania z listy."""
    if not zadania:
        print("Brak zadań.")
        return
    for numer, zadanie in enumerate(zadania, start=1):
        znacznik = "x" if zadanie["zrobione"] else " "
        print(f"{numer}. [{znacznik}] {zadanie['tytul']}")


# TODO: dodawanie zadań – realizuje członek zespołu (karta Trello nr 1)
# TODO: usuwanie i oznaczanie zadań jako zrobione – członek zespołu (karta Trello nr 2)


def menu():
    """Główna pętla programu."""
    while True:
        print("\n=== LISTA ZADAŃ ===")
        print("1. Pokaż zadania")
        print("0. Wyjście")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            pokaz_zadania()
        elif wybor == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    menu()

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


def dodaj_zadanie():
    """Dodaje nowe zadanie do listy."""
    tytul = input("Podaj treść zadania: ").strip()
    if not tytul:
        print("Treść zadania nie może być pusta.")
        return
    zadania.append({"tytul": tytul, "zrobione": False})
    print(f"Dodano zadanie: {tytul}")


def wybierz_numer():
    """Pyta o numer zadania i zwraca jego indeks albo None."""
    pokaz_zadania()
    if not zadania:
        return None
    tekst = input("Podaj numer zadania: ").strip()
    if not tekst.isdigit() or not 1 <= int(tekst) <= len(zadania):
        print("Nieprawidłowy numer.")
        return None
    return int(tekst) - 1


def usun_zadanie():
    """Usuwa wybrane zadanie z listy."""
    indeks = wybierz_numer()
    if indeks is not None:
        usuniete = zadania.pop(indeks)
        print(f"Usunięto zadanie: {usuniete['tytul']}")


def oznacz_jako_zrobione():
    """Oznacza wybrane zadanie jako zrobione."""
    indeks = wybierz_numer()
    if indeks is not None:
        zadania[indeks]["zrobione"] = True
        print(f"Oznaczono jako zrobione: {zadania[indeks]['tytul']}")


def menu():
    """Główna pętla programu."""
    while True:
        print("\n=== LISTA ZADAŃ ===")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Oznacz jako zrobione")
        print("0. Wyjście")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            pokaz_zadania()
        elif wybor == "2":
            dodaj_zadanie()
        elif wybor == "3":
            usun_zadanie()
        elif wybor == "4":
            oznacz_jako_zrobione()
        elif wybor == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    menu()

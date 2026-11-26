# Zasady współpracy

## Przepływ pracy

1. Wykonaj **fork** głównego repozytorium.
2. Sklonuj swój fork na komputer.
3. Utwórz **gałąź roboczą** dla zadania – nie pracuj na `main`.
4. Wprowadź zmiany i wykonaj commity.
5. Wypchnij gałąź do swojego forka.
6. Utwórz **Pull Request** do gałęzi `main` głównego repozytorium.
7. Kierownik projektu przegląda PR i scala go po akceptacji.

## Nazwy gałęzi

Format: `typ/krotki-opis`

- `feature/` – nowa funkcja, np. `feature/dodawanie-zadan`
- `fix/` – poprawka błędu, np. `fix/pusta-lista`
- `docs/` – dokumentacja, np. `docs/readme`

## Commity

- Piszemy krótko, po polsku, w trybie rozkazującym: `Dodaj funkcję usuwania zadań`.
- Jeden commit = jedna logiczna zmiana.
- Nie commitujemy plików tymczasowych (patrz `.gitignore`).

## Pull Requesty

Każdy PR musi zawierać:

- **Tytuł** opisujący zmiany,
- **Opis** wykonanych prac,
- **Link do karty Trello**, której dotyczy,
- **Problemy / ograniczenia** (jeśli są).

Szablon opisu:

```
## Opis
Co zostało zrobione.

## Trello
Link do karty.

## Problemy / ograniczenia
Brak / opis.
```

## Styl kodu

- Zgodnie z PEP 8, wcięcia 4 spacje.
- Nazwy funkcji i zmiennych po polsku, `snake_case`.
- Każda funkcja ma krótki docstring.

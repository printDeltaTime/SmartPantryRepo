"""Moduł walidacji danych wejściowych od użytkownika."""


def get_int_input(prompt, min_val, max_val):
    """Pyta użytkownika o liczbę całkowitą z zakresu [min_val, max_val].

    Powtarza pytanie, dopóki dane nie będą poprawne.
    """
    while True:
        raw = input(prompt).strip()

        if not raw:
            print("Błąd: wpisałeś pustą wartość. Podaj liczbę.")
            continue

        try:
            value = int(raw)
        except ValueError:
            print(f"Błąd: '{raw}' nie jest liczbą całkowitą.")
            continue

        if value < min_val or value > max_val:
            print(f"Błąd: liczba musi być z zakresu {min_val}-{max_val}.")
            continue

        return value


def get_non_empty_string(prompt):
    """Pyta użytkownika o niepusty tekst (spacje na brzegach są usuwane)."""
    while True:
        value = input(prompt).strip()

        if not value:
            print("Błąd: tekst nie może być pusty.")
            continue

        return value

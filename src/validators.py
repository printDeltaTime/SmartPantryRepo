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


def get_float_input(prompt: str, min_val: float= 0.0) -> float:
    """Pobiera liczbę float; automatycznie zamienia ',' na '.'."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            val = float(raw)
            if val < min_val:
                print(f"Błąd: Wartość nie może być mniejsza niż {min_val:.2f}.")
                continue
            return val
        except ValueError:
            print(f"Błąd: '{raw}' nie jest poprawną liczbą.")


def get_choice_input(prompt: str, choices: list[str]) -> str:
    """Wymusza wybór ze ściśle zdefiniowanej listy wariantów."""
    valid_lower = [c.casefold() for c in choices]
    while True:
        val = input(prompt).strip()
        if val.casefold() in valid_lower:
            return val
        print(f"Błąd: Wybierz jedną z opcji: [{', '.join(choices)}]")
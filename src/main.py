"""Smart Pantry - prosty program CLI do zarządzania domową spiżarnią."""

from data import INITIAL_ITEMS
from services import (
    add_item,
    display_items,
    filter_by_category,
    filter_by_min_quantity,
)
from validators import get_int_input, get_non_empty_string

items = list(INITIAL_ITEMS)  # kopia, żeby nie zmieniać danych początkowych


def print_menu():
    """Wyświetla menu z nagłówkiem domeny."""
    print()
    print("=" * 36)
    print("       SMART PANTRY - MENU GŁÓWNE")
    print("=" * 36)
    print("1. Pokaż zawartość spiżarni")
    print("2. Dodaj nowy produkt")
    print("3. Filtruj produkty")
    print("0. Wyjście")
    print("-" * 36)


def show_items():
    display_items(items)


def add_new_item():
    name = get_non_empty_string("Nazwa produktu: ").lower()
    category = get_non_empty_string("Kategoria: ").lower()
    quantity = get_int_input("Ilość sztuk (1-1000): ", 1, 1000)
    new_item = add_item(
        items, {"name": name, "category": category, "quantity": quantity}
    )
    print(f"Dodano produkt o ID {new_item['id']}: {name}.")


def filter_items():
    print("1. Po kategorii")
    print("2. Po minimalnej ilości")
    choice = get_int_input("Wybierz filtr (1-2): ", 1, 2)

    match choice:
        case 1:
            category = get_non_empty_string("Podaj kategorię: ")
            result = filter_by_category(items, category)
        case 2:
            min_quantity = get_int_input("Minimalna ilość (1-1000): ", 1, 1000)
            result = filter_by_min_quantity(items, min_quantity)

    display_items(result)


def handle_choice(choice):
    """Obsługuje wybór z menu. Zwraca False, gdy program ma się zakończyć."""
    match choice:
        case 1:
            show_items()
        case 2:
            add_new_item()
        case 3:
            filter_items()
        case 0:
            print("Do widzenia!")
            return False
    return True


def main():
    running = True
    while running:
        print_menu()
        choice = get_int_input("Wybierz opcję (0-3): ", 0, 3)
        running = handle_choice(choice)


if __name__ == "__main__":
    main()

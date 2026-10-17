"""Smart Pantry - prosty program CLI do zarządzania domową spiżarnią."""

from validators import get_int_input, get_non_empty_string

pantry = {}  # słownik: nazwa produktu -> ilość sztuk


def print_menu():
    """Wyświetla menu z nagłówkiem domeny."""
    print()
    print("=" * 36)
    print("       SMART PANTRY - MENU GŁÓWNE")
    print("=" * 36)
    print("1. Dodaj produkt")
    print("2. Pokaż zawartość spiżarni")
    print("3. Zużyj produkt")
    print("0. Wyjście")
    print("-" * 36)


def add_product():
    name = get_non_empty_string("Nazwa produktu: ").lower()
    quantity = get_int_input("Ilość sztuk (1-1000): ", 1, 1000)
    pantry[name] = pantry.get(name, 0) + quantity
    print(f"Dodano: {name} x{quantity} (razem: {pantry[name]}).")


def show_pantry():
    if not pantry:
        print("Spiżarnia jest pusta.")
        return
    for i, (name, quantity) in enumerate(pantry.items(), start=1):
        print(f"{i}. {name} - {quantity} szt.")


def use_product():
    if not pantry:
        print("Spiżarnia jest pusta, nie ma czego zużyć.")
        return
    name = get_non_empty_string("Nazwa produktu do zużycia: ").lower()
    if name not in pantry:
        print(f"Nie ma produktu '{name}' w spiżarni.")
        return
    quantity = get_int_input(f"Ile sztuk zużyć (1-{pantry[name]}): ", 1, pantry[name])
    pantry[name] -= quantity
    if pantry[name] == 0:
        del pantry[name]
        print(f"Zużyto wszystko: {name} (usunięto z listy).")
    else:
        print(f"Zużyto {quantity} szt. Zostało: {pantry[name]}.")


def handle_choice(choice):
    """Obsługuje wybór z menu. Zwraca False, gdy program ma się zakończyć."""
    match choice:
        case 1:
            add_product()
        case 2:
            show_pantry()
        case 3:
            use_product()
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

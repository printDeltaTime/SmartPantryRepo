"""Logika biznesowa Smart Pantry: wyświetlanie, dodawanie i filtrowanie."""


def display_items(items_list):
    """Wyświetla produkty jako sformatowaną tabelę."""
    if not items_list:
        print("Spiżarnia jest pusta.")
        return

    line = "-" * 44
    print(line)
    print(f"{'ID':<5}{'Nazwa':<18}{'Kategoria':<14}{'Ilość':>7}")
    print(line)
    for item in items_list:
        print(
            f"{item['id']:<5}"
            f"{item['name']:<18}"
            f"{item['category']:<14}"
            f"{item['quantity']:>7}"
        )
    print(line)


def add_item(items_list, new_item_data):
    """Dodaje nowy rekord z unikalnym ID i zwraca go."""
    new_id = max((item["id"] for item in items_list), default=0) + 1
    new_item = {"id": new_id, **new_item_data}
    items_list.append(new_item)
    return new_item


def filter_by_category(items_list, category):
    """Zwraca produkty z podanej kategorii (bez względu na wielkość liter)."""
    category = category.lower()
    return [item for item in items_list if item["category"].lower() == category]


def filter_by_min_quantity(items_list, min_quantity):
    """Zwraca produkty, których ilość jest co najmniej min_quantity."""
    return [item for item in items_list if item["quantity"] >= min_quantity]

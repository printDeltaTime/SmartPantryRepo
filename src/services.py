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


def delete_by_id(items: list[dict], item_id: int) -> bool:
    """Wyszukuje i usuwa rekord z kolekcji."""
    target = find_by_id(items, item_id)
    if target is not None:
        items.remove(target)
        return True
    return False


def find_by_id(items: list[dict], item_id: int) -> dict| None:
    """Wyszukuje słownik po ID za pomocą pętli for."""
    for item in items:
        if item["id"] == item_id:
            return item
    return None


def filter_by_category(items_list, category):
    """Zwraca produkty z podanej kategorii (bez względu na wielkość liter)."""
    category = category.lower()
    return [item for item in items_list if item["category"].lower() == category]


def filter_by_min_quantity(items_list, min_quantity):
    """Zwraca produkty, których ilość jest co najmniej min_quantity."""
    return [item for item in items_list if item["quantity"] >= min_quantity]


# def filter_menu(catalog: list[dict], query: str, max_price: float) -> list[dict]:
#     """Zwraca pozycje spełniające kryteria frazy i ceny."""
#     results = []
#     q = query.strip().casefold()
#     for item in catalog:
#         if q in item["name"].casefold() and item["price"] <= max_price:
#             results.append(item)
#     return results
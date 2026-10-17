# Sprawozdanie z Zadania Laboratoryjnego nr 1
**Przedmiot:** Programowanie w języku Python (`IwIK-S1`)  
**Projekt:** Smart Pantry  
**Zespół (Autorzy):**  
1. [Paweł Szwarocki] (nr albumu: 164883) – login Git: PawelSzwarocki
2. [Łukasz Sojka] (nr albumu: 164880) – login Git: printDeltaTime 
**Data oddania:** [17.10.2026r.]  

---

## 1. Cel i Zakres Inżynierski Zadania
Celem etapu było przygotowanie stanowiska pracy i repozytorium Git, a następnie zbudowanie konsolowej aplikacji do zarządzania domową spiżarnią wraz z bezpieczną obsługą danych wprowadzanych przez użytkownika. Zaimplementowano pętlę menu opartą o `while` i instrukcję `match-case`, moduł walidatorów odporny na błędne dane oraz warstwę danych i usług (wyświetlanie tabeli, dodawanie rekordów z unikalnym ID, filtrowanie).

---

## 2. Architektura Rozwiązania i Struktura Modułów

* `src/__init__.py` – plik oznaczający katalog `src/` jako pakiet Pythona (utworzony w Kroku 1).
* `src/data.py` – lista słowników `INITIAL_ITEMS` z danymi początkowymi domeny (4 produkty, każdy z atrybutami `id`, `name`, `category`, `quantity`).
* `src/validators.py` – funkcje `get_int_input` i `get_non_empty_string`, które w pętli pytają użytkownika do czasu podania poprawnych danych.
* `src/services.py` – logika biznesowa: `display_items` (tabela z wyrównaniem f-stringami), `add_item` (nowy rekord z unikalnym ID), `filter_by_category` i `filter_by_min_quantity`.
* `src/main.py` – menu CLI (`print_menu`), pętla `while running`, obsługa wyboru przez `match-case` w `handle_choice` oraz formularz dodawania i filtrowania podpięte pod menu.

---

## 3. Kluczowy Fragment Kodu i Uzasadnienie Inżynierskie
Poniżej przedstawiono funkcję get_int_input, która odpowiada za walidację danych liczbowych wprowadzanych przez użytkownika. 
```python
def get_int_input(prompt, min_val, max_val):
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
```

**Uzasadnienie wyboru:**  
Funkcja jest podstawą odporności całego programu na błędne dane. Pętla `while True` powtarza pytanie, aż użytkownik poda poprawną wartość, więc program nigdy nie przechodzi dalej z niepoprawnymi danymi. Metoda `.strip()` usuwa spacje, dzięki czemu wpisanie samych spacji jest traktowane tak samo jak pusta linia. Konwersję `int()` objęto blokiem `try/except ValueError`, żeby litery nie powodowały przerwania programu wyjątkiem, a na końcu sprawdzany jest zakres `min_val`–`max_val`. Funkcja jest użyta zarówno w menu głównym, jak i w formularzu dodawania produktu, więc walidacja jest zapisana w jednym miejscu.

---

## 4. Scenariusze Weryfikacji i Wyniki Testów

### Scenariusz A: Ścieżka poprawna (Happy Path)
* **Dane wejściowe:** wybór opcji `1` (wyświetlenie rejestru), następnie opcji `2` i dodanie produktu: nazwa `ser`, kategoria `nabiał`, ilość `4`.
* **Oczekiwany i uzyskany wynik:**
```text
Wybierz opcję (0-3): 1
--------------------------------------------
ID   Nazwa             Kategoria       Ilość
--------------------------------------------
1    mleko             nabiał              5
2    makaron           sypkie              8
3    jabłka            owoce              12
4    ser żółty         nabiał              2
--------------------------------------------

Wybierz opcję (0-3): 2
Nazwa produktu: ser
Kategoria: nabiał
Ilość sztuk (1-1000): 4
Dodano produkt o ID 5: ser.
```

### Scenariusz B: Obsługa błędów i wartości brzegowych
* **Dane wejściowe (błędne):** w menu głównym litera `a` oraz liczba `9`; w formularzu pusta nazwa produktu oraz ilość `abc`, `0` i `5000`.
* **Reakcja programu:**
```text
Wybierz opcję (0-3): a
Błąd: 'a' nie jest liczbą całkowitą.
Wybierz opcję (0-3): 9
Błąd: liczba musi być z zakresu 0-3.

Nazwa produktu:
Błąd: tekst nie może być pusty.
Ilość sztuk (1-1000): abc
Błąd: 'abc' nie jest liczbą całkowitą.
Ilość sztuk (1-1000): 0
Błąd: liczba musi być z zakresu 1-1000.
Ilość sztuk (1-1000): 5000
Błąd: liczba musi być z zakresu 1-1000.
```
Po każdym błędzie program zgłasza komunikat i ponownie zadaje to samo pytanie, nie kończąc działania. Puste wejście i same spacje są obsługiwane w ten sam sposób jak pusty tekst.

---

## 5. Podział Pracy w Zespole
* **[Paweł Szwarocki]:**
  * Odpowiedzialność za moduły: src/data.py, src/validators.py, src/services.py, src/main.py
  * Zaimplementowane funkcjonalności: funkcjonalności: obsługa menu konsolowego, dodawanie produktów, wyświetlanie listy oraz filtrowanie produktów, funkcjonalności: przygotowanie danych początkowych oraz walidacja danych wprowadzanych przez użytkownika.
  * Liczba wykonanych commitów: 5
* **[Łukasz Sojka]:**
  * Odpowiedzialność za moduły: Dodanie modułów
  * Zaimplementowane funkcjonalności: funkcjonalności: przygotowanie danych początkowych 
  * Liczba wykonanych commitów: 1

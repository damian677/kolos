# Importowanie modułów
from bstArray import BSTArray
from testing import test

# Definicja funkcji, która tworzy drzewo BST i wstawia do niego elementy
def create_and_populate_bst(elements):
    bst = BSTArray()
    for element in elements:
        bst.insert(element)
    return bst

# Definicja głównej funkcji
def main():
    # Lista elementów do wstawienia do drzewa BST
    elements_to_insert = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]

    # Tworzenie i wypełnianie drzewa BST
    bst = create_and_populate_bst(elements_to_insert)

    # Wyświetlanie struktury drzewa BST
    bst.print_array()

    # Wywołanie funkcji testowej
    test()

# Sprawdzenie, czy skrypt jest uruchamiany bezpośrednio
if __name__ == '__main__':
    # Jeśli tak, wywołanie funkcji main
    main()

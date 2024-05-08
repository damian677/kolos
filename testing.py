# Importowanie potrzebnych modułów
import csv
import random
from time import time
from bstArray import BSTArray

# Funkcja testowa
def test():
    time_p = time()
    # Lista rozmiarów do przetestowania
    n_arr = [25, 50, 100, 500, 1_000, 10000, 25000, 50000, 100000, 250000, 1000000]

    # Otwarcie pliku do zapisu wyników
    f = open('results2.csv', 'w')
    # Nagłówek pliku CSV
    header = ['N ', 'Insert ', 'Min ', 'Max ', 'Search ']
    # Tworzenie obiektu piszącego do pliku CSV
    writer = csv.writer(f, dialect='excel')
    # Zapisanie nagłówka do pliku
    writer.writerow(header)

    # Pętla po wszystkich rozmiarach do przetestowania
    for N in n_arr:
        # Generowanie listy N losowych liczb zmiennoprzecinkowych od 0.00 do 10.00
        elems_to_insert = [round(random.uniform(.00, 10.00), 2) for _ in range(N)]

        # Tworzenie nowego obiektu BSTArray
        tree_array = BSTArray()  # generowanie korzeni od 0.5 do 10 z krokiem 1

        multiplication = 100_000  # mnożnik do pomiaru czasu

        # Pomiar czasu wstawiania elementów do drzewa
        insert_start = time()
        for elem in elems_to_insert:
            tree_array.insert(elem)  # wstawianie elementów do drzewa
        insert_end = time()

        # Pomiar czasu wyszukiwania minimalnego elementu w drzewie
        min_start = time()
        for i in range(N):
            minimum = tree_array.minimum_in_node(random.uniform(.00, 10.00))
        min_end = time()

        # Pomiar czasu wyszukiwania maksymalnego elementu w drzewie
        max_start = time()
        for i in range(N):
            maximum = tree_array.maximum_in_node(random.uniform(.00, 10.00))
        max_end = time()

        # Generowanie losowej liczby zmiennoprzecinkowej
        random_float = round(random.uniform(.0, 10.0), 2)

        # Pomiar czasu wyszukiwania elementu w drzewie
        search_start = time()
        for i in range(N):
            search = tree_array.exists(random_float)
        search_end = time()

        # Zapisanie wyników do pliku CSV
        writer.writerow(
            [N, " ", (insert_end - insert_start) ," ", (min_end - min_start) ," ",
             (max_end - max_start) ," ", (search_end - search_start) ])

        time_k = time()
        time_c = time_k - time_p
    writer.writerow([" czas wykonania testowania wynosi : ",  time_c])
    print(" czas wykonania testowania wynosi : ",  time_c)

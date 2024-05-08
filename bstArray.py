# Importowanie potrzebnych modułów
import math
import numpy as np
from bstNode import BSTNode

# Klasa BSTArray reprezentująca tablicę drzew BST
class BSTArray:
    # Konstruktor klasy BSTArray
    def __init__(self, length=11):
        self.length = length  # Długość tablicy
        # Tworzenie tablicy drzew BST
        self.array = self._create_bst_array()

    def _create_bst_array(self):
        return [BSTNode(i) for i in np.arange(start=0.5, stop=self.length + 0.5, step=1)]

    # Metoda do wstawiania wartości do odpowiedniego drzewa BST w tablicy
    def insert(self, val):
        self._get_node(val).insert(val)

    def _get_node(self, val):
        return self.array[math.floor(val)]

    # Metoda do znalezienia minimalnej wartości w odpowiednim drzewie BST w tablicy
    def minimum_in_node(self, val):
        return self._get_node(val).get_min()

    # Metoda do znalezienia maksymalnej wartości w odpowiednim drzewie BST w tablicy
    def maximum_in_node(self, val):
        return self._get_node(val).get_max()

    # Metoda do sprawdzenia, czy wartość istnieje w odpowiednim drzewie BST w tablicy
    def exists(self, val):
        return self._get_node(val).exists(val)

    # Metoda do drukowania drzew BST w tablicy
    def print_array(self):
        for node in self.array:
            if node.left is not None or node.right is not None:
                node.print_tree()

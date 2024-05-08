class BSTNode:
    # Konstruktor klasy BSTNode
    def __init__(self, val=None):
        self.left = None  # Lewe dziecko węzła
        self.right = None  # Prawe dziecko węzła
        self.val = val  # Wartość przechowywana w węźle

    # Metoda do wstawiania wartości do drzewa BST
    def insert(self, val):
        if not self.val:  # Jeśli węzeł jest pusty, wstawiamy wartość
            self.val = val
            return

        if self.val == val:  # Jeśli wartość już istnieje w drzewie, nie robimy nic
            return

        if val < self.val:  # Jeśli wartość jest mniejsza od wartości węzła, idziemy do lewego dziecka
            if self.left:  # Jeśli lewe dziecko istnieje, rekurencyjnie wstawiamy wartość
                self.left.insert(val)
                return
            self.left = BSTNode(val)  # Jeśli lewe dziecko nie istnieje, tworzymy nowy węzeł
            return

        if self.right:  # Jeśli wartość jest większa lub równa wartości węzła, idziemy do prawego dziecka
            self.right.insert(val)  # Jeśli prawe dziecko istnieje, rekurencyjnie wstawiamy wartość
            return
        self.right = BSTNode(val)  # Jeśli prawe dziecko nie istnieje, tworzymy nowy węzeł

    # Metoda do znalezienia minimalnej wartości w drzewie BST
    def get_min(self):
        current = self
        while current.left is not None:  # Idziemy do najbardziej lewego węzła
            current = current.left
        return current.val  # Zwracamy wartość najbardziej lewego węzła

    # Metoda do znalezienia maksymalnej wartości w drzewie BST
    def get_max(self):
        current = self
        while current.right is not None:  # Idziemy do najbardziej prawego węzła
            current = current.right
        return current.val  # Zwracamy wartość najbardziej prawego węzła

    # Metoda do sprawdzenia, czy wartość istnieje w drzewie BST
    def exists(self, val):
        if val == self.val:  # Jeśli wartość jest równa wartości węzła, zwracamy prawdę
            return True

        if val < self.val:  # Jeśli wartość jest mniejsza od wartości węzła, idziemy do lewego dziecka
            if self.left is None:  # Jeśli lewe dziecko nie istnieje, zwracamy fałsz
                return False
            return self.left.exists(val)  # Jeśli lewe dziecko istnieje, rekurencyjnie sprawdzamy wartość

        if self.right is None:  # Jeśli wartość jest większa od wartości węzła, idziemy do prawego dziecka
            return False  # Jeśli prawe dziecko nie istnieje, zwracamy fałsz
        return self.right.exists(val)  # Jeśli prawe dziecko istnieje, rekurencyjnie sprawdzamy wartość

    # Metoda do drukowania drzewa BST
    def print_tree(self, level=0, is_right=False):
        if is_right:  # Jeśli węzeł jest prawym dzieckiem, drukujemy odpowiednią ilość spacji
            print(' ' * 4, (level - 1) * 5 * ' ', end='', sep='')
        print('-' * level, self.val, end='', sep='')  # Drukujemy wartość węzła
        if len(str(self.val).split('.')[1]) == 1:  # Jeśli wartość jest liczbą zmiennoprzecinkową z jednym miejscem po przecinku, drukujemy dodatkową spację
            print(' ', end='', sep='')
        if self.left:  # Jeśli lewe dziecko istnieje, rekurencyjnie drukujemy drzewo
            self.left.print_tree(level + 1)
        if self.right:  # Jeśli prawe dziecko istnieje, rekurencyjnie drukujemy drzewo
            self.right.print_tree(level + 1, is_right=self.left is not None)
        if (not self.left) and (not self.right):  # Jeśli węzeł jest liściem, drukujemy nową linię
            print()
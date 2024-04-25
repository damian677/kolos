import time


def hanoi(ni, sour, dest, buff, licznik):
    if ni == 1:
        print(f"Move disk '{sour}' to '{dest}'")
        licznik[0] += 1
        return
    hanoi(ni-1, sour, buff, dest, licznik)
    print(f"Move disk '{sour}' to '{dest}'")
    licznik[0] += 1
    hanoi(ni-1, buff, dest, sour, licznik)


n = 997
liczniki = [0]
start_time = time.time()
hanoi(n, "a", "b", "c", liczniki)
end_time = time.time()
hole_time = end_time - start_time
print(liczniki)
print(hole_time)

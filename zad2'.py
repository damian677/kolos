import time


def hanoi(n, sour, dest, buff):
    i = 1

    while sour or buff and len(buff) < n:
        if i % 3 == 1:
            if sour and (not dest or sour[-1] < dest[-1]):
                print(f"przeniesiono klocek {sour[-1]} z {sour} do {dest} ")
                dest.append(sour.pop())
            elif dest and (not sour or dest[-1] < sour[-1]):
                print(f"przeniesiono klocek {dest[-1]} z {dest} do {sour} ")
                sour.append(dest.pop())

        if i % 3 == 2:
            if sour and (not buff or sour[-1] < buff[-1]):
                print(f"przeniesiono klocek {sour[-1]} z {sour} do {buff} ")
                buff.append(sour.pop())
            elif buff and (not sour or buff[-1] < sour[-1]):
                print(f"przeniesiono klocek {buff[-1]}z {buff} do {sour} ")
                sour.append(buff.pop())

        if i % 3 == 0:
            if buff and (not dest or buff[-1] < dest[-1]):
                print(f"przeniesiono klocek {buff[-1]} z {buff} do {dest} ")
                dest.append(buff.pop())
            elif dest and (not buff or dest[-1] < buff[-1]):
                print(f"przeniesiono klocek {dest[-1]} z {dest} do {buff} ")
                buff.append(dest.pop())
        i += 1

    print("zrobiłeś ", i-1, " kroków")


n = 7
licznik = [0]
sour = []
sour = [klocek for klocek in range(n, 0, -1)]
print("ilo")

dest = []
buff = []
start_time = time.time()
hanoi(n, sour, dest, buff)
end_time = time.time()
hole_time = end_time - start_time
print(hole_time)

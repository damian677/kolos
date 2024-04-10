import os
import shutil



sciezka_katalogu = 'zadanie1'
if not os.path.exists(sciezka_katalogu):
    print("Podany katalog nie istnieje.")
nowa_sciezka = 'nowy_katalog'
for plik in os.listdir(sciezka_katalogu):
    if not os.path.exists(nowa_sciezka):
        os.makedirs(nowa_sciezka)
    if os.path.isfile(os.path.join(sciezka_katalogu, plik)):
        shutil.copy(os.path.join(sciezka_katalogu, plik),nowa_sciezka)

for plik in os.listdir(nowa_sciezka):
    if os.path.isfile(os.path.join(nowa_sciezka, plik)):
        pierwsza_litera = plik[0].upper()
        nowa_sciezka_katalogu = os.path.join(nowa_sciezka, pierwsza_litera)
        os.makedirs(nowa_sciezka_katalogu, exist_ok=True)
        shutil.move(os.path.join(nowa_sciezka, plik), os.path.join(nowa_sciezka_katalogu, plik))
        print(f"Przeniesiono plik '{plik}' z katalogu ' {nowa_sciezka}' do katalogu '{pierwsza_litera}'.")




import random


def ustawienia():
    while True:
        try:
            ile = int(input("Podaj ilość typowanych liczb: "))
            maks = int(input("Podaj maksymalną losowaną liczbę: "))
            if ile > maks:
                print("Blędne dane")
                continue
            ilelos = int(input("Ile losowań: "))
            return (ile, maks, ilelos)
        except ValueError:
            print("Błędne dane")
            continue

def losujliczby(ile, maks):
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1,maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i+1
    return liczby

def pobierztypy(ile,maks):
    print("Wytypuj %s z %s liczba: " % (ile,maks))
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbe %s: " %(i+1)))
        except ValueError:
            print("Błędne dane")
            continue

        if 0 < typ <=maks and typ not in typy:
            typy.add(typ)
            i = i +1

    return typy

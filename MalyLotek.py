import sys, random

liczba = random.randint(1, 10)
# print("Wylosowana liczba:", liczba)

for i in range(3):
    print("Próba ", i + 1)
    odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
    # print("Podałeś liczbę: ", odp)

    if liczba == int(odp):
        print("Zgadłeś! Dostajesz długopis!")
        break
    elif i == 2:
        print("Miałem na myśli liczbę: ", liczba)
    else:
        print("Nie zgadłeś. Spróbuj jeszcze raz.")
    print()

from funkcje import ustawienia, losujliczby, pobierztypy


def main(args):
    ileliczb, maksliczba, ilerazy = ustawienia()

    liczby = losujliczby(ileliczb, maksliczba)

    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        trafione = set(liczby) & typy
        if trafione:
            print("\nIlość trafień: %s" % len(trafione))
            print("Trafione liczby: %s" % trafione)
        else:
            print("Brak trafień. Spróbuj jeszcze raz")

        print("\n" + "x"*40 + "\n")

    print("Wylosowane liczby:", liczby)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

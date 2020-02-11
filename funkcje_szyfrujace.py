def funkcje_szyfrujace(dane, klucz, metoda):
    if len(dane) != len(klucz):
        print("Różne długości")
    dlugosc_danych = len(dane)
    zaszyfrowany = []

    if metoda == "XOR":
        for i in range(dlugosc_danych):
            if dane[i] == klucz[i]:
                zaszyfrowany.append(0)
            else:
                zaszyfrowany.append(1)

    if metoda == "XNOR":
        for i in range(dlugosc_danych):
            if dane[i] == klucz[i]:
                zaszyfrowany.append(1)
            else:
                zaszyfrowany.append(0)

    if metoda == "AND":
        for i in range(dlugosc_danych):
            if dane[i] == "1" and klucz[i] == "1":
                zaszyfrowany.append(1)
            else:
                zaszyfrowany.append(0)

    if metoda == "OR":
        for i in range(dlugosc_danych):
            if dane[i] == "0" and klucz[i] == "0":
                zaszyfrowany.append(0)
            else:
                zaszyfrowany.append(1)

    if metoda == "NOR":
        for i in range(dlugosc_danych):
            if dane[i] == "0" and klucz[i] == "0":
                zaszyfrowany.append(1)
            else:
                zaszyfrowany.append(0)

    if metoda == "NAND":
        for i in range(dlugosc_danych):
            if dane[i] == "1" and klucz[i] == "1":
                zaszyfrowany.append(0)
            else:
                zaszyfrowany.append(1)
    return zaszyfrowany
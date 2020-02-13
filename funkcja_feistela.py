from PyQt5 import QtCore


def funkcja_szyfrujaca(lewa, prawa, klucz_szyfrujacy):
    wartosc1 = int(lewa, 2) ^ (int(prawa, 2) & int(klucz_szyfrujacy, 2))
    return bin(wartosc1)[2:].zfill(16)

print(funkcja_szyfrujaca("01100001", "01100010", "01100011"))

def szyfrowanie(tekst, klucz, liczb_rund, interfejs, odszyfrowanie=False):
    czesc_zaszyfrowana = []
    # tekst_w_liste_znakow = [ord(i) for i in list(tekst)]
    tekst_w_liste_znakow = [bin(ord(x))[2:].zfill(16) for x in tekst]
    klucz_w_liste_znakow = [bin(ord(c))[2:].zfill(16) for c in klucz]
    while (len(tekst_w_liste_znakow) / 2) % len(klucz):
        tekst_w_liste_znakow.append("0000000000000000")
    # klucz_w_liste_znakow = [ord(c) for c in klucz]
    # petla przeskakujaca po calym tekscie co ilosc bitow
    licznik = 0
    for czesc in range(0, len(tekst_w_liste_znakow), len(klucz)*2):
        QtCore.QCoreApplication.processEvents()
        licznik += 1
        interfejs.progressBar.setValue(mapowanie_procentow(licznik, 0, len(tekst_w_liste_znakow)/(len(klucz)*2), 0, 100))
        lewa_czesc_czesci_tekstu = tekst_w_liste_znakow[czesc:len(klucz) + czesc]
        prawa_czesc_czesci_tekstu = tekst_w_liste_znakow[czesc + len(klucz): czesc + (2*len(klucz))]
        # petla przeskakujaca ilosc wyznaczonych rund
        for runda in range(liczb_rund):
            if not odszyfrowanie:
                lewa1 = prawa_czesc_czesci_tekstu
                prawa1 = []
            else:
                lewa1 = []
                prawa1 = lewa_czesc_czesci_tekstu
        # petla przeskakujaca po kazdym znaku w ciagu
            for znak in range(0, len(klucz)):
                if not odszyfrowanie:
                    prawa1.append(
                        funkcja_szyfrujaca(
                            lewa_czesc_czesci_tekstu[znak],
                            prawa_czesc_czesci_tekstu[znak],
                            klucz_w_liste_znakow[znak]
                        )
                    )
                else:
                    lewa1.append(
                        funkcja_szyfrujaca(
                            prawa_czesc_czesci_tekstu[znak],
                            lewa_czesc_czesci_tekstu[znak],
                            klucz_w_liste_znakow[znak]
                        )
                    )
            lewa_czesc_czesci_tekstu = lewa1
            prawa_czesc_czesci_tekstu = prawa1
        czesc_zaszyfrowana += lewa_czesc_czesci_tekstu + prawa_czesc_czesci_tekstu
    ciag = ''.join(c for c in czesc_zaszyfrowana)
    ciag2 = bity_do_tekstu(ciag)
    return ciag2

def bity_do_tekstu(bity):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bity)] * 16))

def mapowanie_procentow(wartosc, lewa_min, lewa_max, prawa_min, prawa_max):
    lewa = lewa_max - lewa_min
    prawa = prawa_max - prawa_min
    wartosc_przeskalowana = float(wartosc - lewa_min) / float(lewa)
    return prawa_min + (wartosc_przeskalowana * prawa)


from PyQt5 import QtCore
import hashlib

SECRET = "3f788083-77d3-4502-9d71-gf86556er5kide9i"


def funkcja_szyfrujaca(lewa, prawa, klucz_szyfrujacy):
    """
    @param lewa: Lewa strona tekstu wejściowego
    @param prawa: Prawa strona tekstu wejściowego
    @param klucz_szyfrujacy: Klucz szyfrujący
    @return: Zwraca wynik funkcji szyfrującej prawą stronę i klucz xorowanej lewą strona
    """
    wartosc1 = int(lewa, 2) ^ (int(prawa, 2) ^ int(klucz_szyfrujacy, 2))
    return bin(wartosc1)[2:].zfill(16)


def mieszaj_klucz(klucz, dlugosc):
    """

    :param klucz: Przesyłany klucz do tworzenia podkluczy
    :param dlugosc: długość tekstu do której mają być generowane klucze
    :return: zwraca wygenerowane klucze
    """
    wygenerowany_ciag = ""
    for znak in klucz:
        wygenerowany = bin(int(hashlib.sha512((klucz + SECRET).encode('utf-8')).hexdigest(), 16))[2:]
        wygenerowany = wygenerowany.ljust(512, '1')
        wygenerowany_ciag += wygenerowany
    pociety_ciag = [wygenerowany_ciag[i:i + int(dlugosc)] for i in range(0, len(wygenerowany_ciag), int(dlugosc))]
    return pociety_ciag


def szyfrowanie(tekst, klucz, liczb_rund, interfejs, odszyfrowanie=False):
    """
    Główna funkcja szyfrująca
    :param tekst: Tekst do zaszyfrowania lub odszyfrowania
    :param klucz: Klucz którym tekst będzie szyfrowany lub odszyfrowany
    :param liczb_rund: Ilośc rund które zostana wykonane
    :param interfejs: Przekazanie interfejsu okna GUI
    :param odszyfrowanie: Sprawdzenie czy ma wykonać operacje szyfrowania czy odszyfrowywania
    :return: Zwraca zaszyfrowany ciąg znaków
    """
    czesc_zaszyfrowana = []
    tekst_w_liste = [bin(ord(x))[2:].zfill(16) for x in tekst]
    mieszany_klucz = mieszaj_klucz(klucz, 16)[:liczb_rund]
    if odszyfrowanie:
        mieszany_klucz.reverse()
    while (len(tekst_w_liste) / 2) % len(klucz):
        tekst_w_liste.append("0000000000000000")

    licznik = 0
    for czesc in range(0, len(tekst_w_liste), len(klucz) * 2):
        QtCore.QCoreApplication.processEvents()
        licznik += 1
        interfejs.progressBar.setValue(mapowanie_procentow(licznik, 0, len(tekst_w_liste) / (len(klucz) * 2), 0, 100))
        lewa_czesc_czesci_tekstu = tekst_w_liste[czesc:len(klucz) + czesc]
        prawa_czesc_czesci_tekstu = tekst_w_liste[czesc + len(klucz): czesc + (2 * len(klucz))]
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
                            mieszany_klucz[runda]
                        )
                    )
                else:
                    lewa1.append(
                        funkcja_szyfrujaca(
                            prawa_czesc_czesci_tekstu[znak],
                            lewa_czesc_czesci_tekstu[znak],
                            mieszany_klucz[runda]
                        )
                    )
            lewa_czesc_czesci_tekstu = lewa1
            prawa_czesc_czesci_tekstu = prawa1
        czesc_zaszyfrowana += lewa_czesc_czesci_tekstu + prawa_czesc_czesci_tekstu
    ciag = ''.join(c for c in czesc_zaszyfrowana)
    ciag2 = bity_do_tekstu(ciag)
    return ciag2


def bity_do_tekstu(bity):
    """
    :param bity: Wprowadzone bity które mają być zamienione na string
    :return: Zwraca string z podanych bitów
    """
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bity)] * 16))


def mapowanie_procentow(wartosc, lewa_min, lewa_max, prawa_min, prawa_max):
    """
    Funkcja służy do sprawdzenia ilości przebiegów i przypisanie tego procentowo do paska postępu
    """
    lewa = lewa_max - lewa_min
    prawa = prawa_max - prawa_min
    wartosc_przeskalowana = float(wartosc - lewa_min) / float(lewa)
    return prawa_min + (wartosc_przeskalowana * prawa)

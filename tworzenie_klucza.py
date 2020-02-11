import hashlib


SECRET = "3f788083-77d3-4502-9d71-gf86556er5kide9i"


def mieszaj_klucz(klucz, dlugosc, interfejs):
    wygenerowany_ciag = ""
    for znak in klucz:
        wygenerowany = bin(int(hashlib.sha512((znak + SECRET).encode('utf-8')).hexdigest(), 16))[2:]
        wygenerowany = wygenerowany.ljust(512, '1')
        wygenerowany_ciag += wygenerowany
    pociety_ciag = [wygenerowany_ciag[i:i + int(dlugosc)] for i in range(0, len(wygenerowany_ciag), int(dlugosc))]
    return pociety_ciag[:int(interfejs.liczbaPrzebiegow.text())]


def zmiana_dlugosci_klucza(interfejs):
    dlugosc_tekstu = int(interfejs.dlugoscKlucza.currentText()) * 2
    interfejs.klucz.setMaxLength((dlugosc_tekstu / 16) / 2)

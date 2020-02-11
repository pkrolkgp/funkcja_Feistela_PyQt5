from funkcje_szyfrujace import funkcje_szyfrujace
from dzielenie_tekstu import podziel_do_dlugosci


def funkcja_feistela(bity_jawne, bity_klucza, interfejs,  odwrotnie=False):
    dlugosc_tekstu = len(bity_jawne)
    dlugosc_klucza = len(bity_klucza[0])
    szyfrogram = ""
    if dlugosc_tekstu / 2 == dlugosc_klucza:
        bity_do_podzielenia = podziel_do_dlugosci(bity_jawne, dlugosc_klucza)

        if odwrotnie:
            lewa_czesc = bity_do_podzielenia[1]
            prawa_czesc = bity_do_podzielenia[0]
        else:
            lewa_czesc = bity_do_podzielenia[0]
            prawa_czesc = bity_do_podzielenia[1]

        for x in range(0, int(interfejs.liczbaPrzebiegow.text())):
            l_prim = prawa_czesc
            r_mid = ''.join(
                [str(x) for x in funkcje_szyfrujace(prawa_czesc, bity_klucza[x], interfejs.drugaMetoda.currentText())])
            r_prim = ''.join([str(x) for x in funkcje_szyfrujace(lewa_czesc, r_mid, "XOR")])
            lewa_czesc = l_prim
            prawa_czesc = r_prim

        if odwrotnie:
            szyfrogram = str(prawa_czesc) + str(lewa_czesc)
        else:
            szyfrogram = str(lewa_czesc) + str(prawa_czesc)

    return szyfrogram

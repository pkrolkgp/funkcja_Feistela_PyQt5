import string
from random import random, randrange, choice, getrandbits

import cypari


def kodowanie_tekstu(tekst):
    liczba = 0
    for index, znak in enumerate(tekst):
        liczba += ord(znak) * (381 ** index)
    return liczba


def kodowanie_tekstu_z_dzieleniem(tekst):
    liczba = 0
    licznikZnakow = -1
    tabelaLiczb = []
    for index, znak in enumerate(tekst):
        licznikZnakow += 1
        liczba += ord(znak) * (381 ** licznikZnakow)
        if licznikZnakow >= 100:
            tabelaLiczb.append(liczba)
            liczba = 0
            licznikZnakow = 0
    tabelaLiczb.append(liczba)
    return tabelaLiczb


def odkodowanie_znakow(ciag_znakow):
    tekst = ""
    while ciag_znakow != 0:
        tekst += chr(ciag_znakow % 381)
        ciag_znakow = ciag_znakow // 381
    return tekst


def generator_ciagu(dlugosc=8):
    ciag = string.hexdigits
    wynik = ''.join(choice(ciag) for i in range(int(dlugosc / 8)))
    return wynik


# tekst_klucza_publicznego = kodowanie_tekstu("Piotr Król SSINF 2018")
# tekst_do_zaszyfrowania = kodowanie_tekstu("My jesteśmy krasnoludki hopsSA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA
# HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA
# HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA
# HOPSA SA HOPSA SA HOPSA SA HOPSA SA HOPSA SA")
# print("Zakodowany Tekst: " + str(tekst_do_zaszyfrowania))

# def generuj_pierwsza(dlugosc, seed=None):
#     # generator liczby pierwszej
#     if not seed:
#         seed = randrange(0, pow(2, int(dlugosc)))
#     pierwsza = cypari.pari('nextprime(2^'+str(dlugosc)+'+'+str(seed)+')')
#     print("liczba pierwsza: " + str(pierwsza))
#     return pierwsza

def generuj_pierwsza(dlugosc, seed=None):
    # generator liczby pierwszej
    if not seed:
        dlugoscMini = int(int(dlugosc) / 2)
        mini = getrandbits(dlugoscMini + 1)
        # print("min:" + str(mini))

        maxi = getrandbits(int(dlugosc))
        # print("max:" + str(maxi))
        while mini > maxi:
            maxi = getrandbits(int(dlugosc))
            # print("max:" + str(maxi))
        seed = randrange(mini, maxi)
        print(seed)
    pierwsza = cypari.pari('nextprime(' + str(seed) + ')')
    # print("liczba pierwsza: " + str(pierwsza))
    return pierwsza


def generuj_n(p, q):
    # n jawna składowa klucza publicznego i prywatnego, to iloczyn p * q
    n = p * q
    # print("skladowa n: " + str(n))
    return n


def generuj_e(tekst):
    # jawna składowa klucza publicznego, może być wygenerowane jako tekst jawny i zakodowany
    # e = cypari.pari('nextprime(2^900+4654165421651616816)')
    e = cypari.pari('nextprime(' + str(tekst) + "0000000000"')')
    # print("publiczny e: " + str(e))
    # print("e odkodowany: " + str(odkodowanie_znakow(int(str(e)[0:-10]))))
    return e


def generuj_d(p, q, e):
    # niejawna składowa klucza prywatnego
    pmq = cypari.pari('(' + str(p) + '-1)*(' + str(q) + '-1)')
    prq = cypari.pari('Mod(' + str(e) + ',' + str(pmq) + ')')
    d = cypari.pari('lift(' + str(prq) + '^-1)')
    # print("prywatny d: " + str(d))
    return d


def generuj_M(n, tekst):
    # M = wiadomość zakodowana gotowa do zaszyfrowania, pobierana od użytownika. M nie może być większe niż n
    # M = cypari.pari('nextprime(2^600+465454165421651616816)')
    stringLiczba = str(tekst) + "0000000000"
    M = cypari.pari('nextprime(' + stringLiczba + ')')
    # print("M: " + str(M))
    if int(M) > int(n):
        print("\"M\" jest większe od \"n\" o " + str(int(M) - int(n)))
        exit(1)
    return M


def generuj_M_tablicowe(n, tablicaLiczb):
    # M = wiadomość zakodowana gotowa do zaszyfrowania, pobierana od użytownika. M nie może być większe niż n
    # M = cypari.pari('nextprime(2^600+465454165421651616816)')
    M = []
    for tekst in tablicaLiczb:
        stringLiczba = str(tekst) + "0000000000"
        M.append(cypari.pari('nextprime(' + stringLiczba + ')'))
        # print("M: " + str(M))
        if int(tekst) > int(n):
            print("\"M\" jest większe od \"n\" ")
            # exit(1)
    return M


def generuj_C(n, e, M):
    # C = szyfowanie wiadomosci M kluczem publicznym e lub odszyrowywanie wiadomości zaszyfrowanej kluczem prywatnym d
    C = cypari.pari('lift(Mod(' + str(M) + ',' + str(n) + ')^' + str(e) + ')')
    # print("C: " + str(C))
    return C


def generuj_C_z_tablicy(n, e, M):
    # C = szyfowanie wiadomosci M kluczem publicznym e lub odszyrowywanie wiadomości zaszyfrowanej kluczem prywatnym d
    C = []
    for tabliczka in M:
        C.append(cypari.pari('lift(Mod(' + str(tabliczka) + ',' + str(n) + ')^' + str(e) + ')'))
        # print("C: " + str(tabliczka))
    return C


def generuj_D(n, d, C):
    # D =  szyfowanie wiadomosci C kluczem prywatnym d lub odszyrowywanie wiadomości zaszyfrowanej kluczem publicznym e
    D = cypari.pari('lift(Mod(' + str(C) + ',' + str(n) + ')^' + str(d) + ')')
    # print("Od: " + str(D))
    # print("Odszyfrowany i odkodowany: " + str(odkodowanie_znakow(int(str(D)[0:-10]))))
    return D


def generuj_D_z_tablicy(n, d, C):
    # D =  szyfowanie wiadomosci C kluczem prywatnym d lub odszyrowywanie wiadomości zaszyfrowanej kluczem publicznym e
    D = []
    for tabliczka in C:
        D.append(cypari.pari('lift(Mod(' + str(tabliczka) + ',' + str(n) + ')^' + str(d) + ')'))
        # print("Od: " + str(tabliczka))
        # print("Odszyfrowany i odkodowany: " + str(odkodowanie_znakow(int(str(tabliczka)[0:-10]))))
    return D


def odkodowanie_liczby_w_tekst(tablicaLiczb):
    tekst = ""
    for liczba in tablicaLiczb:
        tekst += str(odkodowanie_znakow(int(str(liczba)[0:-10])))
    return tekst

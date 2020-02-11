# szyfrowanie siecia Feistlea
# autor: Piotr Król
# ver 0.6
# https://pl.wikipedia.org/wiki/Sie%C4%87_Feistela
import hashlib
import sys
from PyQt5 import QtWidgets


from funkcje_szyfrujace import funkcje_szyfrujace
from dzielenie_tekstu import podziel_do_dlugosci
from konwersja_bitowa import *
from mapowanie_procentowe import mapowanie_procentow
from tworzenie_klucza import mieszaj_klucz
from funkcja_feistela import funkcja_feistela
from okno_aplikacji import OknoAplikacji

SECRET = "3f788083-77d3-4502-9d71-gf86556er5kide9i"


def main():
    interfejs = okno.ui
    kod_binarny = ""
    kod_binarny_zaszyfrowany = ""
    klucz_binarnie = ""
    tekst_zaszyfrowany_wynik = ""
    if len(interfejs.klucz.text()) == (int(interfejs.dlugoscKlucza.currentText()) / 16):
        if interfejs.tekstJawny.text() != "":
            jawny_tekst = tekst_do_bitow(interfejs.tekstJawny.text())
            klucz = mieszaj_klucz(interfejs.klucz.text(), int(interfejs.dlugoscKlucza.currentText()), interfejs)
            lista_tekst = podziel_do_dlugosci(jawny_tekst, int(interfejs.dlugoscKlucza.currentText()) * 2)
            lista_klucz = podziel_do_dlugosci(
                tekst_do_bitow(interfejs.klucz.text()),
                int(interfejs.dlugoscKlucza.currentText())
            )
            tekst_zaszyfrowany_lista = []
            dlugosc_listy = len(lista_tekst)
            licznik = 0

            if interfejs.odszyfrujRadio.isChecked():
                klucz.reverse()
                lista_tekst.reverse()

            for i in lista_tekst:
                if interfejs.odszyfrujRadio.isChecked():
                    wynik_feistla = funkcja_feistela(i, klucz, interfejs,  True)
                else:
                    wynik_feistla = funkcja_feistela(i, klucz, interfejs)

                tekst_zaszyfrowany_lista.append((str(wynik_feistla)))
                licznik += 1
                interfejs.progressBar.setValue(mapowanie_procentow(licznik, 0, dlugosc_listy, 0, 100))
                lista_zaszyfrowanych_bitow = podziel_do_dlugosci(wynik_feistla, 16)
                lista_kod_binarny = podziel_do_dlugosci(i, 16)

                for ii in lista_kod_binarny:
                    kod_binarny += ii
                for iii in lista_zaszyfrowanych_bitow:
                    kod_binarny_zaszyfrowany += iii

            for i in lista_klucz:
                kod_klucz = podziel_do_dlugosci(i, 16)
                for ii in kod_klucz:
                    klucz_binarnie += ii

            if interfejs.odszyfrujRadio.isChecked():
                tekst_zaszyfrowany_lista.reverse()

            tekst_zaszyfrowany = ''.join([str(x) for x in tekst_zaszyfrowany_lista])
            tekst_zaszyfrowany_wynik = bity_do_tekstu(tekst_zaszyfrowany)
        else:
            okno.blad_pokaz("Brak tekstu jawnego")
    else:
        okno.blad_pokaz("Za krótki klucz")

    if interfejs.pokazSzczegoly.isChecked():
        interfejs.kodBinarny.setPlainText(kod_binarny)
        interfejs.binarnyZaszyfrowany.setPlainText(kod_binarny_zaszyfrowany)

    interfejs.kluczBinarnie.setPlainText(klucz_binarnie)
    interfejs.tekstZaszyfrowany.setPlainText(tekst_zaszyfrowany_wynik)

    interfejs.licznikKoduBinarnego.display(len(kod_binarny))
    interfejs.licznikKoduBinarnegoZaszyfrowanego.display(len(kod_binarny_zaszyfrowany))
    interfejs.licznikKluczaBinarnego.display(len(klucz_binarnie))
    interfejs.licznikTekstuZaszyfrowanego.display(len(tekst_zaszyfrowany_wynik))


aplikacja = QtWidgets.QApplication(sys.argv)
okno = OknoAplikacji()
okno.ui.buttonSzyfruj.clicked.connect(main)
okno.show()
sys.exit(aplikacja.exec_())

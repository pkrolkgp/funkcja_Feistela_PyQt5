# szyfrowanie siecia Feistlea
# autor: Piotr Król
# ver 0.8
# https://pl.wikipedia.org/wiki/Sie%C4%87_Feistela
import sys
from PyQt5 import QtWidgets

from funkcja_feistela import *
from okno_aplikacji import OknoAplikacji



def main():
    interfejs = okno.ui
    if len(interfejs.klucz.text()) == (int(interfejs.dlugoscKlucza.currentText()) / 16):
        if interfejs.tekstJawny.toPlainText() != "":
            jawny_tekst = interfejs.tekstJawny.toPlainText()
            klucz = interfejs.klucz.text()

            if interfejs.szyfrujRadio.isChecked():
                tekst_zaszyfrowany = szyfrowanie(
                    jawny_tekst, klucz, int(interfejs.liczbaPrzebiegow.text()), interfejs
                )
            else:
                tekst_zaszyfrowany = szyfrowanie(
                    jawny_tekst, klucz, int(interfejs.liczbaPrzebiegow.text()), interfejs, True
                )
            interfejs.tekstZaszyfrowany.setPlainText(tekst_zaszyfrowany)
            interfejs.licznikTekstuZaszyfrowanego.display(len(tekst_zaszyfrowany))
        else:
            okno.blad_pokaz("Brak tekstu jawnego")
    else:
        okno.blad_pokaz("Za krótki klucz")


aplikacja = QtWidgets.QApplication(sys.argv)
okno = OknoAplikacji()
okno.ui.buttonSzyfruj.clicked.connect(main)
okno.show()
sys.exit(aplikacja.exec_())

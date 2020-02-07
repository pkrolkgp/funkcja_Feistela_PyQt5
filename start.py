# szyfrowanie siecia Feistlea
# autor: Piotr Król
# ver 0.5
# https://pl.wikipedia.org/wiki/Sie%C4%87_Feistela
import hashlib
import sys
from PyQt5 import QtWidgets

from startui import Ui_Dialog as startUI

SECRET = "3f788083-77d3-4502-9d71-gf86556er5kide9i"


def tekst_do_bitow(tekst):
    return ''.join([bin(ord(x))[2:].zfill(16) for x in tekst])


def bity_do_tekstu(bity):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bity)] * 16))


def podziel_do_dlugosci(bity_wyslane, dlugosc_wyslana):
    def _f(bity, dlugosc):
        while bity:
            if len(bity) < dlugosc:
                x = bity.ljust(dlugosc, '0')
                bity = x
            yield bity[:dlugosc]
            bity = bity[dlugosc:]

    return list(_f(bity_wyslane, dlugosc_wyslana))


def mapowanie_procentow(wartosc, lewa_min, lewa_max, prawa_min, prawa_max):
    lewa = lewa_max - lewa_min
    prawa = prawa_max - prawa_min
    wartosc_przeskalowana = float(wartosc - lewa_min) / float(lewa)
    return prawa_min + (wartosc_przeskalowana * prawa)


def funkcje_szyfrujace(dane, klucz, metoda):
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


def mieszaj_klucz(klucz, dlugosc):
    wygenerowanyCiag = bin(int(hashlib.sha512((klucz + SECRET).encode('utf-8')).hexdigest(), 16))[2:]
    wygenerowanyCiag = wygenerowanyCiag.ljust(512, '1')
    wygenerowanyCiag += wygenerowanyCiag
    pocietyCiag = [wygenerowanyCiag[i:i + int(dlugosc)] for i in range(0, len(wygenerowanyCiag), int(dlugosc))]
    return pocietyCiag[:int(w.ui.liczbaPrzebiegow.text())]


def funkcja_feistla(bity_jawne, bity_klucza, odwrotnie=False):
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
        for x in range(0, int(w.ui.liczbaPrzebiegow.text())):
            l_prim = prawa_czesc
            r_mid = ''.join(
                [str(x) for x in funkcje_szyfrujace(prawa_czesc, bity_klucza[x], w.ui.drugaMetoda.currentText())])
            r_prim = ''.join([str(x) for x in funkcje_szyfrujace(lewa_czesc, r_mid, "XOR")])
            lewa_czesc = l_prim
            prawa_czesc = r_prim

        if odwrotnie:
            szyfrogram = str(prawa_czesc) + str(lewa_czesc)
        else:
            szyfrogram = str(lewa_czesc) + str(prawa_czesc)
    return szyfrogram


def zaszyfruj():
    kod_binarny = ""
    kod_binarny_zaszyfrowany = ""
    klucz_binarnie = ""
    tekst_zaszyfrowany_wynik = ""
    if len(w.ui.klucz.text()) == (int(w.ui.dlugoscKlucza.currentText()) / 16):
        if w.ui.tekstJawny.text() != "":
            jawny_tekst = tekst_do_bitow(w.ui.tekstJawny.text())
            klucz = mieszaj_klucz(w.ui.klucz.text(), int(w.ui.dlugoscKlucza.currentText()))
            lista_tekst = podziel_do_dlugosci(jawny_tekst, int(w.ui.dlugoscKlucza.currentText()) * 2)
            lista_klucz = podziel_do_dlugosci(tekst_do_bitow(w.ui.klucz.text()), int(w.ui.dlugoscKlucza.currentText()))
            tekst_zaszyfrowany_lista = []
            dlugosc_listy = len(lista_tekst)
            licznik = 0

            if w.ui.odszyfrujRadio.isChecked():
                klucz.reverse()
                lista_tekst.reverse()

            for i in lista_tekst:
                if w.ui.odszyfrujRadio.isChecked():
                    wynik_feistla = funkcja_feistla(i, klucz, True)
                else:
                    wynik_feistla = funkcja_feistla(i, klucz)

                tekst_zaszyfrowany_lista.append((str(wynik_feistla)))
                licznik += 1
                w.ui.progressBar.setValue(mapowanie_procentow(licznik, 0, dlugosc_listy, 0, 100))
                lista_zaszyfrowanych_bitow = podziel_do_dlugosci(wynik_feistla, 16)
                lista_kod_binarny = podziel_do_dlugosci(i, 16)

                # for ii in lista_kod_binarny:
                #     kod_binarny += ii + "-"
                # for iii in lista_zaszyfrowanych_bitow:
                #     kod_binarny_zaszyfrowany += iii + "-"

            # for i in lista_klucz:
            #     kod_klucz = podziel_do_dlugosci(i, 16)
            #     for ii in kod_klucz:
            #         klucz_binarnie += ii

            if w.ui.odszyfrujRadio.isChecked():
                tekst_zaszyfrowany_lista.reverse()

            tekst_zaszyfrowany = ''.join([str(x) for x in tekst_zaszyfrowany_lista])
            tekst_zaszyfrowany_wynik = bity_do_tekstu(tekst_zaszyfrowany)
        else:
            blad_pokaz("Brak tekstu jawnego")
    else:
        blad_pokaz("Za krótki klucz")

    if w.ui.pokazSzczegoly.isChecked():
        w.ui.kodBinarny.setPlainText(kod_binarny)
        w.ui.binarnyZaszyfrowany.setPlainText(kod_binarny_zaszyfrowany)

    w.ui.kluczBinarnie.setPlainText(klucz_binarnie)
    w.ui.tekstZaszyfrowany.setPlainText(tekst_zaszyfrowany_wynik)

    w.ui.licznikKoduBinarnego.display(len(kod_binarny))
    w.ui.licznikKoduBinarnegoZaszyfrowanego.display(len(kod_binarny_zaszyfrowany))
    w.ui.licznikKluczaBinarnego.display(len(klucz_binarnie))
    w.ui.licznikTekstuZaszyfrowanego.display(len(tekst_zaszyfrowany_wynik))


def zmiana_dlugosci_klucza():
    dlugoscTekstu = int(w.ui.dlugoscKlucza.currentText()) * 2
    w.ui.klucz.setMaxLength((dlugoscTekstu / 16) / 2)
    w.ui.liczbaPrzebiegow.setMaximum((512 / (dlugoscTekstu / 4)))


def zmiana_szczegolow():
    if w.ui.pokazSzczegoly.isChecked():
        w.ui.kodBinarny.setEnabled(True)
        w.ui.binarnyZaszyfrowany.setEnabled(True)
    else:
        w.ui.kodBinarny.setEnabled(False)
        w.ui.binarnyZaszyfrowany.setEnabled(False)
        w.ui.kodBinarny.setPlainText("")
        w.ui.binarnyZaszyfrowany.setPlainText("")


def blad_pokaz(tekst, nazwa_okna="Błąd"):
    mb = QtWidgets.QMessageBox()
    mb.setIcon(QtWidgets.QMessageBox.Information)
    mb.setWindowTitle(nazwa_okna)
    mb.setText(tekst)
    mb.setStandardButtons(QtWidgets.QMessageBox.Ok)
    mb.show()
    mb.exec_()


def licznik_tesktu():
    w.ui.licznikTekstuJawnego.display(len(w.ui.tekstJawny.text()))


def otwarcie_pliku(lokalizacja_pliku):
    with open(lokalizacja_pliku, 'r', encoding="utf-8") as plik:
        try:
            dane_z_pliku = plik.read()
            w.ui.tekstJawny.setText(dane_z_pliku)
        except:
            blad_pokaz("Błędny plik, musi być tekstowy")


class AppWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = startUI()
        self.ui.setupUi(self)
        self.ui.dlugoscKlucza.setCurrentIndex(2)
        self.ui.drugaMetoda.setCurrentIndex(0)

        self.ui.buttonSzyfruj.clicked.connect(zaszyfruj)
        self.ui.dlugoscKlucza.currentIndexChanged.connect(zmiana_dlugosci_klucza)
        self.ui.klucz.setMaxLength(int(self.ui.dlugoscKlucza.currentText()) / 16)
        self.ui.liczbaPrzebiegow.setMaximum(512 / int(self.ui.dlugoscKlucza.currentText()) * 2 )
        self.ui.pokazSzczegoly.stateChanged.connect(zmiana_szczegolow)
        self.ui.tekstJawny.textChanged.connect(licznik_tesktu)
        self.show()

    def debugPrint(self, msg):
        print(msg)

    def browseSlot(self):
        self.debugPrint("Browse button pressed")
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Otwórz plik",
            "",
            "Pliki tekstowe (*.txt);;Wszystkie pliki (*)",
            options=options)
        if fileName:
            self.debugPrint("setting file name: " + fileName)
            # self.model.setFileName( fileName )
            # self.refreshAll()
            otwarcie_pliku(fileName)

    def file_save(self):
        # name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            text = w.ui.tekstZaszyfrowany.toPlainText()
            if text is not "":
                options = QtWidgets.QFileDialog.Options()
                nazwaPliku, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    'Zapisz plik', "",
                    "Pliki tekstowe (*.txt)",
                    options=options)
                self.debugPrint(nazwaPliku)
                file = open(nazwaPliku, 'w')
                file.write(text)
                file.close()
                blad_pokaz("Zapisano!", "Sukces")
            else:
                blad_pokaz("Brak zaszyfrowanego tekstu!")
        except:
            blad_pokaz("Błąd zapisu pliku")


app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

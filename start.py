# szyfrowanie siecia Feistlea
# autor: Piotr Król
# ver 0.4
# https://pl.wikipedia.org/wiki/Sie%C4%87_Feistela
import sys
from PyQt5 import QtWidgets

from startui import Ui_Dialog as startUI

dlugosc = 64
liczba_przebiegow = 3
pokaz_szczegoly = True


def tekst_do_bitow(tekst):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in tekst])


def bity_do_tekstu(bity):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bity)] * 8))


def podziel_do_dlugosci(bity, dlugosc):
    def _f(bity, dlugosc):
        while bity:
            if len(bity) < dlugosc:
                x = bity.ljust(dlugosc, '0')
                bity = x
            yield bity[:dlugosc]
            bity = bity[dlugosc:]
    return list(_f(bity, dlugosc))


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


def funkcja_feistla(bity_jawne, bity_klucza):
    global liczba_przebiegow
    dlugosc_tekstu = len(bity_jawne)
    dlugosc_klucza = len(bity_klucza)
    l_prim = ""
    r_prim = ""
    if dlugosc_tekstu / 2 == dlugosc_klucza:
        bity_do_podzielenia = podziel_do_dlugosci(bity_jawne, dlugosc_klucza)
        lewa_czesc = bity_do_podzielenia[0]
        prawa_czesc = bity_do_podzielenia[1]
        for x in range(0, int(liczba_przebiegow)):
            l_prim = prawa_czesc
            r_mid = funkcje_szyfrujace(prawa_czesc, bity_klucza, w.ui.drugaMetoda.currentText())
            r_prim = funkcje_szyfrujace(lewa_czesc, ''.join([str(x) for x in r_mid]), w.ui.pierwszaMetoda.currentText())
            lewa_czesc = l_prim
            prawa_czesc = ''.join([str(x) for x in r_prim])
    szyfrogram = str(l_prim) + (''.join([str(x) for x in r_prim]))
    return szyfrogram


def zaszyfruj():
    kod_binarny = ""
    kod_binarny_zaszyfrowany = ""
    klucz_binarnie = ""
    tekst_zaszyfrowany_wynik = ""
    if len(w.ui.klucz.text()) == (dlugosc / 8) / 2:
        if w.ui.tekstJawny.text() != "":
            jawny_tekst = tekst_do_bitow(w.ui.tekstJawny.text())
            klucz = tekst_do_bitow(w.ui.klucz.text())
            lista_tekst = podziel_do_dlugosci(jawny_tekst, dlugosc)
            lista_klucz = podziel_do_dlugosci(klucz, int(dlugosc / 2))
            tekst_zaszyfrowany = ""
            dlugosc_listy = len(lista_tekst)
            licznik = 0
            for i in lista_tekst:
                licznik += 1
                w.ui.progressBar.setValue(mapowanie_procentow(licznik, 0, dlugosc_listy, 0, 100))
                wynik_feistla = funkcja_feistla(i, klucz)
                tekst_zaszyfrowany += (str(wynik_feistla))
                lista_zaszyfrowanych_bitow = podziel_do_dlugosci(wynik_feistla, 8)
                lista_kod_binarny = podziel_do_dlugosci(i, 8)
                for ii in lista_kod_binarny:
                    kod_binarny += ii
                for iii in lista_zaszyfrowanych_bitow:
                    kod_binarny_zaszyfrowany += iii

            for i in lista_klucz:
                kod_klucz = podziel_do_dlugosci(i, 8)
                for ii in kod_klucz:
                    klucz_binarnie += ii

            tekst_zaszyfrowany_wynik = bity_do_tekstu(tekst_zaszyfrowany)
        else:
            blad_pokaz("Brak tekstu jawnego")
    else:
        blad_pokaz("Za krótki klucz")

    if pokaz_szczegoly:
        w.ui.kodBinarny.setPlainText(kod_binarny)
        w.ui.binarnyZaszyfrowany.setPlainText(kod_binarny_zaszyfrowany)

    w.ui.kluczBinarnie.setPlainText(klucz_binarnie)
    w.ui.tekstZaszyfrowany.setPlainText(tekst_zaszyfrowany_wynik)

    w.ui.licznikKoduBinarnego.display(len(kod_binarny))
    w.ui.licznikKoduBinarnegoZaszyfrowanego.display(len(kod_binarny_zaszyfrowany))
    w.ui.licznikKluczaBinarnego.display(len(klucz_binarnie))
    w.ui.licznikTekstuZaszyfrowanego.display(len(tekst_zaszyfrowany_wynik))


def zmiana_dlugosci_klucza():
    global dlugosc
    dlugosc = int(w.ui.dlugoscKlucza.currentText()) * 2
    w.ui.klucz.setMaxLength((dlugosc / 8) / 2)


def zmiana_metody():
    global metoda
    metoda = w.ui.drugaMetoda.currentText()


def zmiana_przebiegu():
    global liczba_przebiegow
    liczba_przebiegow = int(w.ui.liczbaPrzebiegow.value())


def zmiana_szczegolow():
    global pokaz_szczegoly
    if w.ui.pokazSzczegoly.isChecked():
        w.ui.kodBinarny.setEnabled(True)
        w.ui.binarnyZaszyfrowany.setEnabled(True)
        pokaz_szczegoly = True
    else:
        w.ui.kodBinarny.setEnabled(False)
        w.ui.binarnyZaszyfrowany.setEnabled(False)
        w.ui.kodBinarny.setPlainText("")
        w.ui.binarnyZaszyfrowany.setPlainText("")
        pokaz_szczegoly = False


def blad_pokaz(tekst, nazwaOkna = "Błąd"):
    mb = QtWidgets.QMessageBox()
    mb.setIcon(QtWidgets.QMessageBox.Information)
    mb.setWindowTitle(nazwaOkna)
    mb.setText(tekst)
    mb.setStandardButtons(QtWidgets.QMessageBox.Ok)
    mb.show()
    mb.exec_()


def licznik_tesktu():
    w.ui.licznikTekstuJawnego.display(len(w.ui.tekstJawny.text()))

def otwarcie_pliku(lokalizacjaPliku):
    with open(lokalizacjaPliku, 'r') as plik:
        try:
            dane_z_pliku = plik.read()
            w.ui.tekstJawny.setText(dane_z_pliku)
        except:
            blad_pokaz("Błędny plik, musi być tekstowy")
        #print(dane_z_pliku)
        #return dane_z_pliku



class AppWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # self.ui = uic.loadUi('start.ui', self)
        self.ui = startUI()
        self.ui.setupUi(self)
        self.ui.dlugoscKlucza.setCurrentIndex(2)
        self.ui.drugaMetoda.setCurrentIndex(0)
        self.ui.buttonSzyfruj.clicked.connect(zaszyfruj)
        self.ui.dlugoscKlucza.currentIndexChanged.connect(zmiana_dlugosci_klucza)
        self.ui.drugaMetoda.currentIndexChanged.connect(zmiana_metody)
        self.ui.liczbaPrzebiegow.valueChanged.connect(zmiana_przebiegu)
        self.ui.pokazSzczegoly.stateChanged.connect(zmiana_szczegolow)
        self.ui.tekstJawny.textChanged.connect(licznik_tesktu)
        #regex = QRegExp("[!-~-\s-a-z-A-Z-0-9_]+")
        #validator = QRegExpValidator(regex)
        #self.ui.tekstJawny.setValidator(validator)
        #self.ui.klucz.setValidator(validator)
        self.show()

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        print(msg)
        #self.debugTextBrowser.append( msg )

    def browseSlot(self):
        ''' Called when the user presses the Browse button
        '''
        self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Otwórz plik",
                        "",
                        "Pliki tekstowe (*.txt);;Wszystkie pliki (*)",
                        options=options)
        if fileName:
            self.debugPrint( "setting file name: " + fileName )
            #self.model.setFileName( fileName )
            #self.refreshAll()
            otwarcie_pliku(fileName)

    def file_save(self):
        #name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            text = w.ui.tekstZaszyfrowany.toPlainText()
            if(text is not ""):
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


import sys

from PyQt5 import QtWidgets, QtGui
from funkcja_RSA import *
from okno_aplikacji import OknoGeneratora
from okno_aplikacji import GlowneOkno
from okno_aplikacji import OknoBiblioteki
from okno_aplikacji import OknoPodpisywania
from okno_aplikacji import OknoSprawdzenia
from okno_aplikacji import potwierdzenieUsuwania
from kodekoder import Kodekoder


def main():
    """
    Generowanie RSA
    autor: Piotr Król
    ver 0.1
    """
    interfejs = oknoGeneratora.ui
    if interfejs.tekstJawny.toPlainText() != "":
        pass
    else:
        oknoGeneratora.blad_pokaz("Brak tekstu jawnego")


def zmianaP():
    seed = ''
    if oknoGeneratora.ui.seed_p:
        seed = oknoGeneratora.ui.seed_p.text()
    try:
        oknoGeneratora.ui.tekstP.setPlainText(str(generuj_pierwsza(oknoGeneratora.ui.dlugoscP.currentText(), seed)))
    except:
        oknoGeneratora.blad_pokaz("Błędne dane dla p")


def zmianaQ():
    seed = ''
    if oknoGeneratora.ui.seed_q:
        seed = oknoGeneratora.ui.seed_q.text()
    try:
        oknoGeneratora.ui.tekstQ.setPlainText(str(generuj_pierwsza(oknoGeneratora.ui.dlugoscQ.currentText(), seed)))
    except:
        oknoGeneratora.blad_pokaz("Błędne dane dla q")


def obliczanieN():
    try:
        n = generuj_n(int(oknoGeneratora.ui.tekstP.toPlainText()), int(oknoGeneratora.ui.tekstQ.toPlainText()))
        oknoGeneratora.ui.tekstN.setPlainText(str(n))
    except:
        oknoGeneratora.blad_pokaz("Błędne dane do obliczenia n")


def generujE():
    try:
        gotowe = generator_ciagu(int(oknoGeneratora.ui.dlugoscE.currentText()))
        e = generuj_e(kodowanie_tekstu(gotowe))
        oknoGeneratora.ui.tekstE.setPlainText(str(e))
    except:
        oknoGeneratora.blad_pokaz("Błąd generowania klucza publicznego")


def generujD():
    try:
        d = generuj_d(oknoGeneratora.ui.tekstP.toPlainText(), oknoGeneratora.ui.tekstQ.toPlainText(),
                      oknoGeneratora.ui.tekstE.toPlainText())
        oknoGeneratora.ui.tekstD.setPlainText(str(d))
    except:
        oknoGeneratora.blad_pokaz("Błąd generowania klucza prywatnego")


def wczytajN():
    try:
        oknoGeneratora.ui.tekstN.setPlainText(oknoGeneratora.otworz_plik())
    except:
        oknoGeneratora.blad_pokaz("Błąd wczytywania n")


def zapiszN():
    try:
        oknoGeneratora.zapisz_plik(oknoGeneratora.ui.tekstN.toPlainText(), "n")
    except:
        oknoGeneratora.blad_pokaz("Błąd Zapisu n")


def wczytajE():
    try:
        oknoGeneratora.ui.tekstE.setPlainText(oknoGeneratora.otworz_plik())
    except:
        oknoGeneratora.blad_pokaz("Błąd wczytywania e")


def zapiszE():
    try:
        oknoGeneratora.zapisz_plik(oknoGeneratora.ui.tekstE.toPlainText(), "e")
    except:
        oknoGeneratora.blad_pokaz("Błąd Zapisu e")


def wczytajD():
    try:
        oknoGeneratora.ui.tekstD.setPlainText(oknoGeneratora.otworz_plik())
    except:
        oknoGeneratora.blad_pokaz("Błąd wczytywania d")


def zapiszD():
    try:
        oknoGeneratora.zapisz_plik(oknoGeneratora.ui.tekstD.toPlainText(), "d")
    except:
        oknoGeneratora.blad_pokaz("Błąd Zapisu d")


def konwertujE():
    try:
        kodowanyTekst = kodowanie_tekstu(oknoGeneratora.ui.tekstE.toPlainText())
        wygenerowanyTekst = generuj_e(kodowanyTekst)
        oknoGeneratora.ui.tekstE.setPlainText(str(wygenerowanyTekst))
    except:
        oknoGeneratora.blad_pokaz("Błąd konwersji tekstu na liczbe")


def rekonwertujE():
    try:
        odkodowanyTekst = odkodowanie_znakow(int(oknoGeneratora.ui.tekstE.toPlainText()[0:-10]))
        oknoGeneratora.ui.tekstE.setPlainText(str(odkodowanyTekst))
    except:
        oknoGeneratora.blad_pokaz("Błąd konwersji liczby na tekst")


def zapiszwBibliotece():
    try:
        if oknoGeneratora.ui.tekstNazwa.text() != "" and oknoGeneratora.ui.tekstN.toPlainText() != "" and \
                oknoGeneratora.ui.tekstE.toPlainText() != "" and oknoGeneratora.ui.tekstD.toPlainText() != "":
            klucz = [oknoGeneratora.ui.tekstNazwa.text(), oknoGeneratora.ui.tekstN.toPlainText(),
                     oknoGeneratora.ui.tekstE.toPlainText(), oknoGeneratora.ui.tekstD.toPlainText()]
            # print(klucz)
            if oknoBiblioteki.dodajDoBiblioteki(klucz) != 0:
                oknoBiblioteki.odswiezBiblioteke()
                wczytajKlucze()
                oknoGeneratora.blad_pokaz("Zapisano", "Sukces!")
        else:
            oknoGeneratora.blad_pokaz("Pola n, e, d i nazwa muszą być wypełnione")
    except:
        oknoGeneratora.blad_pokaz("Nie można zapisać w bibliotece!")


def zapiszZtabeliDoPliku():
    try:
        tabela = oknoBiblioteki.ui.tabelaKluczy
        dane = []
        for wiersz in range(tabela.rowCount()):
            dane.append(tworzenieLiniDoZapisu(wiersz))
        oknoBiblioteki.zapisanieBiblioteki(dane)
    except:
        oknoGeneratora.blad_pokaz("Nie można zapisać zmian, czy plik biblioteki jest używany w innym programie?")


def tworzenieLiniDoZapisu(linia, publiczny=False):
    tabela = oknoBiblioteki.ui.tabelaKluczy
    if publiczny:
        ciag = tabela.item(linia, 0).text() + "," + tabela.item(linia, 1).text() + "," + \
               tabela.item(linia, 2).text() + ",,\n"
    else:
        ciag = tabela.item(linia, 0).text() + "," + tabela.item(linia, 1).text() + "," + \
               tabela.item(linia, 2).text() + "," + tabela.item(linia, 3).text() + ",\n"
    return ciag


def usunzBiblioteki():
    try:
        wynik = potwierdzenieUsuwania(oknoBiblioteki)
        if wynik == 1:
            wybrany = oknoBiblioteki.ui.tabelaKluczy.selectionModel().selectedRows()[0].row()
            oknoBiblioteki.ui.tabelaKluczy.removeRow(wybrany)
            zapiszZtabeliDoPliku()
    except:
        oknoGeneratora.blad_pokaz("Nie można usunąć z biblioteki!")


def exportCalegoKlucza():
    try:
        wybrany = oknoBiblioteki.ui.tabelaKluczy.selectionModel().selectedRows()[0].row()
        nazwa = oknoBiblioteki.ui.tabelaKluczy.item(wybrany, 0).text()
        ciag = tworzenieLiniDoZapisu(wybrany)
        # print(ciag)
        oknoGeneratora.zapisz_plik(ciag, "Klucz prywatny " + nazwa, "Plik klucza (*.klucz)")
    except:
        oknoGeneratora.blad_pokaz("Nie można exportować klucza!")


def exportPublicznegoKlucza():
    try:
        wybrany = oknoBiblioteki.ui.tabelaKluczy.selectionModel().selectedRows()[0].row()
        nazwa = oknoBiblioteki.ui.tabelaKluczy.item(wybrany, 0).text()
        ciag = tworzenieLiniDoZapisu(wybrany, True)
        # print(ciag)
        oknoGeneratora.zapisz_plik(ciag, "Klucz publiczny " + nazwa, "Plik klucza publicznego (*.kluczpub)")
    except:
        oknoGeneratora.blad_pokaz("Nie można exportować klucza!")


def importKlucza():
    try:
        klucz = oknoGeneratora.otworz_plik("klucza", "Pliki klucza publicznego (*.kluczpub);;Pliki klucza (*.klucz)")
        nowyKlucz = klucz.split(",")
        oknoBiblioteki.dodajDoBiblioteki(nowyKlucz)
        oknoBiblioteki.odswiezBiblioteke()
    except:
        oknoGeneratora.blad_pokaz("Błąd importowania klucza!")


def odczytajPublicznyKlucz():
    try:
        wybrany = oknoBiblioteki.ui.tabelaKluczy.selectionModel().selectedRows()[0].row()
        kluczPubliczny = oknoBiblioteki.ui.tabelaKluczy.item(wybrany, 2).text()[0:-10]
        oknoBiblioteki.ui.odczytKluczaPublicznego.setText(odkodowanie_znakow(int(kluczPubliczny)))
    except:
        pass


def odczytajPublicznyKluczGlowneMenu():
    try:
        wybrany = oknoBiblioteki.pobranieKluczaPoNazwie(glowneOkno.ui.wybranyKlucz.currentText())
        kluczPubliczny = wybrany[2][0:-10]
        glowneOkno.ui.tekstKluczaPublicznego.setText(odkodowanie_znakow(int(kluczPubliczny)))
    except:
        pass


def pokazGenerowanie():
    oknoGeneratora.show()
    oknoGeneratora.activateWindow()


def pokazPodpis():
    wczytajKluczeDoGeneratoraPodpisu()
    oknoPodpisywania.show()
    oknoPodpisywania.activateWindow()


def pokazSprawdzenie():
    wczytajKluczeDoSprawdzenia()
    oknoSprawdzenia.show()
    oknoSprawdzenia.activateWindow()


def pokazBiblioteka():
    oknoBiblioteki.odswiezBiblioteke()
    oknoBiblioteki.show()
    oknoBiblioteki.activateWindow()


def wczytajTekst():
    try:
        tekst = oknoGeneratora.otworz_plik()
        if tekst is not None:
            glowneOkno.ui.obslugaTekstu.setText(str(tekst))
    except:
        oknoGeneratora.blad_pokaz("Błąd wczytywania tekstu!")


def zapiszTekst():
    try:
        tekst = glowneOkno.ui.obslugaTekstu.toPlainText()
        oknoGeneratora.zapisz_plik(tekst)
    except:
        oknoGeneratora.blad_pokaz("Błąd zapisywania tekstu!")


def wczytajKlucze():
    try:
        klucze = oknoBiblioteki.odczytanieBiblioteki()
    except:
        return
    wynik = []
    for wiersz in klucze:
        komorka = wiersz.split(",")
        if glowneOkno.ui.RadioPrywatny.isChecked():
            if komorka[3] != "":
                wynik.append(komorka[0])
        else:
            if komorka[2] != "":
                wynik.append(komorka[0])
    # print(wynik)
    glowneOkno.ui.wybranyKlucz.clear()
    wynik.sort()
    glowneOkno.ui.wybranyKlucz.addItems(wynik)
    if not wynik:
        glowneOkno.ui.wybranyKlucz.setDisabled(True)
        glowneOkno.ui.wybranyKlucz.addItem("Brak wybranych kluczy!")
    else:
        glowneOkno.ui.wybranyKlucz.setDisabled(False)


def szyfrowanieWiadomosci():
    if glowneOkno.ui.wybranyKlucz.currentText() != "":
        wybranyKlucz = oknoBiblioteki.pobranieKluczaPoNazwie(glowneOkno.ui.wybranyKlucz.currentText())
        tekstDoPrzemielenia = glowneOkno.ui.obslugaTekstu.toPlainText()
        polaczonyD = ""
        nWybranegoKlucza = wybranyKlucz[1]
        dWybranegoKlucza = wybranyKlucz[3]

        if glowneOkno.ui.actionNowe_szyfrowanie.isChecked():
            przemielonyTekst = kodowanie_tekstu_z_dzieleniem(tekstDoPrzemielenia)
            zakodowaneDane = generuj_M_tablicowe(nWybranegoKlucza, przemielonyTekst)
            wygenerowanyD = generuj_D_z_tablicy(nWybranegoKlucza, dWybranegoKlucza, zakodowaneDane)
            for kawalek in wygenerowanyD:
                polaczonyD += str(kawalek) + "\n"
            glowneOkno.ui.obslugaTekstu.setText(str(polaczonyD))
        else:
            przemielonyTekst = kodekoder.szyfrowanie(tekstDoPrzemielenia)
            try:
                zakodowaneDane = generuj_M(nWybranegoKlucza, przemielonyTekst)
                wygenerowanyD = generuj_D(nWybranegoKlucza, dWybranegoKlucza, zakodowaneDane)
                glowneOkno.ui.obslugaTekstu.setText(str(wygenerowanyD))
            except:
                oknoGeneratora.blad_pokaz("Zaszyfrowana wiadomość jest dłuższa niż \"n\"!")
                return


def odszyfrowanieWiadomosci():
    if glowneOkno.ui.wybranyKlucz.currentText() != "":
        wybranyKlucz = oknoBiblioteki.pobranieKluczaPoNazwie(glowneOkno.ui.wybranyKlucz.currentText())
        tekstDoPrzemielenia = glowneOkno.ui.obslugaTekstu.toPlainText()
        nWybranegoKlucza = wybranyKlucz[1]
        eWybranegoKlucza = wybranyKlucz[2]

        if glowneOkno.ui.actionNowe_szyfrowanie.isChecked():
            tablicaLiczb = tekstDoPrzemielenia.split("\n")
            tablicaLiczb.pop()
            wygenerowanyD = generuj_C_z_tablicy(nWybranegoKlucza, eWybranegoKlucza, tablicaLiczb)
            odkodowaneDane = odkodowanie_liczby_w_tekst(wygenerowanyD)
        else:
            wygenerowanyD = generuj_C(nWybranegoKlucza, eWybranegoKlucza, tekstDoPrzemielenia)
            odkodowaneDane = kodekoder.deszyfrowanie(str(wygenerowanyD)[0:-10])

        glowneOkno.ui.obslugaTekstu.setText(str(odkodowaneDane))


def wykonanieAkcji():
    if glowneOkno.ui.radioSzyfruj.isChecked():
        try:
            szyfrowanieWiadomosci()
        except:
            oknoGeneratora.blad_pokaz("Błąd szyfrowania wiadomości!")
    else:
        try:
            odszyfrowanieWiadomosci()
        except:
            oknoGeneratora.blad_pokaz("Błąd odszyfrowywania wiadomości!")


def wczytajKluczeDoGeneratoraPodpisu():
    try:
        klucze = oknoBiblioteki.odczytanieBiblioteki()
    except:
        return
    prywatne = []
    publiczne = []
    for wiersz in klucze:
        komorka = wiersz.split(",")
        if komorka[3] != "":
            prywatne.append(komorka[0])
        if komorka[2] != "":
            publiczne.append(komorka[0])
    oknoPodpisywania.ui.kluczePodpisywania.clear()
    oknoPodpisywania.ui.kluczePodpisywane.clear()
    prywatne.sort()
    publiczne.sort()
    oknoPodpisywania.ui.kluczePodpisywania.addItems(prywatne)
    oknoPodpisywania.ui.kluczePodpisywane.addItems(publiczne)
    if not prywatne:
        oknoPodpisywania.ui.kluczePodpisywania.setDisabled(True)
        oknoPodpisywania.ui.kluczePodpisywania.addItem("Brak wybranych kluczy!")
    else:
        oknoPodpisywania.ui.kluczePodpisywania.setDisabled(False)
    if not publiczne:
        oknoPodpisywania.ui.kluczePodpisywane.setDisabled(True)
        oknoPodpisywania.ui.kluczePodpisywane.addItem("Brak wybranych kluczy!")
    else:
        oknoPodpisywania.ui.kluczePodpisywane.setDisabled(False)


def wczytajKluczeDoSprawdzenia():
    try:
        klucze = oknoBiblioteki.odczytanieBiblioteki()
    except:
        return
    publiczne = []
    for wiersz in klucze:
        komorka = wiersz.split(",")
        if komorka[2] != "":
            publiczne.append(komorka[0])
    oknoSprawdzenia.ui.kluczeSprawdzenia.clear()
    publiczne.sort()
    oknoSprawdzenia.ui.kluczeSprawdzenia.addItems(publiczne)
    if not publiczne:
        oknoSprawdzenia.ui.kluczeSprawdzenia.setDisabled(True)
        oknoSprawdzenia.ui.kluczeSprawdzenia.addItem("Brak wybranych kluczy!")
    else:
        oknoSprawdzenia.ui.kluczeSprawdzenia.setDisabled(False)


def podpisywanieKlucza():
    if oknoPodpisywania.ui.kluczePodpisywania.isEnabled() and oknoPodpisywania.ui.kluczePodpisywane.isEnabled():
        # print("Istnieją klucze")
        podpisujacyKlucz = oknoBiblioteki.pobranieKluczaPoNazwie(oknoPodpisywania.ui.kluczePodpisywania.currentText())
        podpisywanyKlucz = oknoBiblioteki.pobranieKluczaPoNazwie(oknoPodpisywania.ui.kluczePodpisywane.currentText())
        nWybranegoKlucza = podpisujacyKlucz[1]
        dWybranegoKlucza = podpisujacyKlucz[3]
        zakodowaneDane = generuj_M(nWybranegoKlucza, podpisywanyKlucz[2])
        wygenerowanyD = generuj_D(nWybranegoKlucza, dWybranegoKlucza, zakodowaneDane)
        oknoPodpisywania.ui.poleKlucza.setText(str(wygenerowanyD))


def sprawdzeniePodpisu():
    if oknoSprawdzenia.ui.kluczeSprawdzenia.isEnabled():
        podpisujacyKlucz = oknoBiblioteki.pobranieKluczaPoNazwie(oknoSprawdzenia.ui.kluczeSprawdzenia.currentText())
        nWybranegoKlucza = podpisujacyKlucz[1]
        eWybranegoKlucza = podpisujacyKlucz[2]
        wygenerowanyD = generuj_C(nWybranegoKlucza, eWybranegoKlucza, oknoSprawdzenia.ui.poleKlucza.toPlainText())
        odkodowaneDane = odkodowanie_znakow(int(str(wygenerowanyD)[0:-20]))
        oknoSprawdzenia.ui.poleKlucza.setText(str(odkodowaneDane))


def zapiszPodpisanyKlucz():
    tekst = oknoPodpisywania.ui.poleKlucza.toPlainText()
    oknoGeneratora.zapisz_plik(tekst, "Podpisany Klucz " + oknoPodpisywania.ui.kluczePodpisywane.currentText(),
                               "Podpisany klucz(*.certed)")


def wczytajPodpisanyKlucz():
    tekstKlucza = oknoGeneratora.otworz_plik("podpisanego klucza", "Podpisany klucz(*.certed)")
    oknoSprawdzenia.ui.poleKlucza.setText(tekstKlucza)


aplikacja = QtWidgets.QApplication(sys.argv)
kodekoder = Kodekoder()

oknoGeneratora = OknoGeneratora()
oknoBiblioteki = OknoBiblioteki()
oknoPodpisywania = OknoPodpisywania()
oknoSprawdzenia = OknoSprawdzenia()
glowneOkno = GlowneOkno()
wczytajKlucze()
odczytajPublicznyKluczGlowneMenu()

oknoGeneratora.ui.przyciskGenerujP.clicked.connect(zmianaP)
oknoGeneratora.ui.przyciskGenerujQ.clicked.connect(zmianaQ)
oknoGeneratora.ui.obliczN.clicked.connect(obliczanieN)
oknoGeneratora.ui.generujE.clicked.connect(generujE)
oknoGeneratora.ui.generujD.clicked.connect(generujD)
oknoGeneratora.ui.wczytajN.clicked.connect(wczytajN)
oknoGeneratora.ui.zapiszN.clicked.connect(zapiszN)
oknoGeneratora.ui.wczytajE.clicked.connect(wczytajE)
oknoGeneratora.ui.zapiszE.clicked.connect(zapiszE)
oknoGeneratora.ui.wczytajD.clicked.connect(wczytajD)
oknoGeneratora.ui.konwertujE.clicked.connect(konwertujE)
oknoGeneratora.ui.rekonwertujE.clicked.connect(rekonwertujE)
oknoGeneratora.ui.zapiszD.clicked.connect(zapiszD)
oknoGeneratora.ui.zapiszwBibliotece.clicked.connect(zapiszwBibliotece)

oknoBiblioteki.ui.usunWybrany.clicked.connect(usunzBiblioteki)
oknoBiblioteki.ui.exportujCaly.clicked.connect(exportCalegoKlucza)
oknoBiblioteki.ui.exportujWybrany.clicked.connect(exportPublicznegoKlucza)
oknoBiblioteki.ui.wczytajNowy.clicked.connect(importKlucza)
oknoBiblioteki.ui.tabelaKluczy.clicked.connect(odczytajPublicznyKlucz)

oknoPodpisywania.ui.podpisz.clicked.connect(podpisywanieKlucza)
oknoPodpisywania.ui.zapiszPodpisany.clicked.connect(zapiszPodpisanyKlucz)

oknoSprawdzenia.ui.wczytajPodpisany.clicked.connect(wczytajPodpisanyKlucz)
oknoSprawdzenia.ui.Sprawdz.clicked.connect(sprawdzeniePodpisu)

glowneOkno.ui.actionGeneruj.triggered.connect(pokazGenerowanie)
glowneOkno.ui.actionBiblioteka.triggered.connect(pokazBiblioteka)
glowneOkno.ui.actionPodpisz.triggered.connect(pokazPodpis)
glowneOkno.ui.actionWczytaj.triggered.connect(wczytajTekst)
glowneOkno.ui.actionSprawd_podpis.triggered.connect(pokazSprawdzenie)
glowneOkno.ui.actionZapisz.triggered.connect(zapiszTekst)
glowneOkno.ui.RadioPrywatny.toggled.connect(wczytajKlucze)
glowneOkno.ui.wybranyKlucz.currentTextChanged.connect(odczytajPublicznyKluczGlowneMenu)
glowneOkno.ui.SzyfrowanieWykonaj.clicked.connect(wykonanieAkcji)

glowneOkno.show()

sys.exit(aplikacja.exec_())

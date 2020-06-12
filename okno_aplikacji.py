import random

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from startui import Ui_Okno as startUI
from mainui import Ui_MainWindow as startMain
from bibliotekaui import Ui_Form as startBiblioteka
from podpisywanieui import Ui_Form as startPodpisywanie
from sprawdzenieui import Ui_Form as startSprawdzenie



class GlowneOkno(QtWidgets.QMainWindow):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """

    def __init__(self):
        super().__init__()
        self.ui = startMain()
        self.ui.setupUi(self)
        self.show()


class OknoPodpisywania(QtWidgets.QDialog):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """

    def __init__(self):
        super().__init__()
        self.ui = startPodpisywanie()
        self.ui.setupUi(self)
        # self.show()


class OknoSprawdzenia(QtWidgets.QDialog):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """

    def __init__(self):
        super().__init__()
        self.ui = startSprawdzenie()
        self.ui.setupUi(self)
        # self.show()


class OknoBiblioteki(QtWidgets.QDialog):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """
    nazwaPliku = "klucze.biblioteka"
    nazwaCCK = "CCK.biblioteka"

    def __init__(self):
        super().__init__()
        self.ui = startBiblioteka()
        self.ui.setupUi(self)
        # self.show()

    def odczytanieBiblioteki(self):
        try:
            biblioteka = open(self.nazwaPliku, "r", encoding="utf-8")
            zawartosc = biblioteka.readlines()
            biblioteka.close()
            return zawartosc
        except:
            biblioteka = open(self.nazwaPliku, "w+", encoding="utf-8")
            zawartosc = biblioteka.readlines()
            biblioteka.close()
            return zawartosc

    def zapisanieBiblioteki(self, dane):
        biblioteka = open(self.nazwaPliku, "w+", encoding="utf-8")
        biblioteka.writelines(dane)
        biblioteka.close()

    def odswiezBiblioteke(self):
        tabela = self.ui.tabelaKluczy
        tabela.setRowCount(0)
        licznikWierszy = 0
        biblioteka = self.odczytanieBiblioteki()
        for pozycja in biblioteka:
            tabela.insertRow(licznikWierszy)
            komorka = pozycja.split(",")
            licznikKomorek = 0
            for dane in komorka:
                tabela.setItem(licznikWierszy, licznikKomorek, QtWidgets.QTableWidgetItem(dane))
                licznikKomorek += 1
            licznikWierszy += 1

    def dodajDoBiblioteki(self, klucz):
        try:
            t = klucz[4]
            if t == '\n':
                klucz[4] = ""
        except IndexError:
            klucz.append("")
        try:
            t = klucz[5]
        except IndexError:
            klucz.append("")
        gotowyCiag = klucz[0] + "," + klucz[1] + "," + klucz[2] + "," + klucz[3] + "," + klucz[4] + "," + klucz[5] + ",\n"
        if self.sprawdzenieCzyKluczIstnieje(klucz[0]) == 0:
            biblioteka = open(self.nazwaPliku, "a+", encoding="utf-8")
            biblioteka.writelines(gotowyCiag)
            biblioteka.close()
        else:
            OknoGeneratora.blad_pokaz("Taki klucz już istnieje w bibliotece!")
            return 0

    def sprawdzenieCzyKluczIstnieje(self, dodawanaNazwa):
        try:
            klucze = self.odczytanieBiblioteki()
        except:
            return
        for wiersz in klucze:
            komorka = wiersz.split(",")
            if komorka[0] == dodawanaNazwa:
                return 1
        return 0

    def pobranieKluczaPoNazwie(self, szukany):
        try:
            biblioteka = open(self.nazwaPliku, "r", encoding="utf-8")
            zawartosc = biblioteka.readlines()
            biblioteka.close()
            for wiersz in zawartosc:
                komorka = wiersz.split(",")
                if komorka[0] == szukany:
                    return komorka
        except:
            OknoGeneratora.blad_pokaz("Nie można pobrać kluczy z pliku biblioteki!")


def potwierdzenieUsuwania(self):
    box = QMessageBox()
    box.setIcon(QMessageBox.Question)
    box.setWindowTitle('Uwaga!')
    box.setText('Czy na pewno chcesz usunąć?')
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = box.button(QMessageBox.Yes)
    buttonY.setText('Tak')
    buttonN = box.button(QMessageBox.No)
    buttonN.setText('Nie')
    box.exec_()

    if box.clickedButton() == buttonY:
        return 1
    else:
        pass
        # box.information(self, '', "Nie zapisano zmian")


class OknoGeneratora(QtWidgets.QDialog):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """

    def __init__(self):
        super().__init__()
        self.ui = startUI()
        self.ui.setupUi(self)
        # self.show()

    @staticmethod
    def blad_pokaz(tekst, nazwa_okna="Błąd"):
        """
        Generuje okno z informacją dla użytkownika
        :param tekst: Wyświetlana wiadomość
        :param nazwa_okna: Nazwa wyświetlonego okna
        """
        mb = QtWidgets.QMessageBox()
        mb.setIcon(QtWidgets.QMessageBox.Information)
        mb.setWindowTitle(nazwa_okna)
        mb.setText(tekst)
        mb.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mb.show()
        mb.exec_()

    def otworz_plik(self, nazwa="", typy="Pliki tekstowe (*.txt);;Wszystkie pliki (*)"):
        """
        Otwiera plik i ładuje go do pola tekstu do obsługi
        """
        interfejs = self.ui
        options = QtWidgets.QFileDialog.Options()
        nazwa_pliku, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Otwórz plik " + nazwa,
            "",
            typy,
            options=options)
        if nazwa_pliku:
            with open(nazwa_pliku, 'r', encoding="utf-8") as plik:
                try:
                    dane_z_pliku = plik.read()
                    return dane_z_pliku
                    # interfejs.tekstJawny.setPlainText(dane_z_pliku)
                except UnicodeDecodeError:
                    self.blad_pokaz("Błędny plik, musi być tekstowy")

    def zapisz_plik(self, text, domyslna_nazwa=None, typy="Pliki tekstowe (*.txt)"):
        """
        Zapisuje plik wynikowy do pliku na komputerze
        """
        try:
            if text != "":
                options = QtWidgets.QFileDialog.Options()
                nazwa_pliku, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    'Zapisz plik', domyslna_nazwa,
                    typy,
                    options=options)
                file = open(nazwa_pliku, 'w', encoding="utf-8")
                file.write(text)
                file.close()
                self.blad_pokaz("Zapisano!", "Sukces")
            else:
                self.blad_pokaz("Brak tekstu do zapisu!")
        except UnicodeEncodeError:
            self.blad_pokaz("Błąd zapisu pliku")

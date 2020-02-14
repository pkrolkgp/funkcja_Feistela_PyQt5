import random

from PyQt5 import QtWidgets
from startui import Ui_calaSiatka as startUI


class OknoAplikacji(QtWidgets.QDialog):
    """
    Klasa obsługująca operacje w graficznym interfejsie
    """
    def __init__(self):
        super().__init__()
        self.ui = startUI()
        self.ui.setupUi(self)
        self.ui.dlugoscKlucza.setCurrentIndex(2)

        self.ui.klucz.setMaxLength(int(self.ui.dlugoscKlucza.currentText()) / 16)

        self.ui.tekstJawny.textChanged.connect(self.licznik_tesktu)
        self.ui.dlugoscKlucza.currentIndexChanged.connect(self.zmiana_dlugosci_klucza)
        self.ui.szyfrujRadio.toggled.connect(self.zmiana_wartosci_klawisza_szyfrowania)
        self.show()

    def zmiana_wartosci_klawisza_szyfrowania(self):
        """
        Zmienia tekst na klawiszu szyforwania
        """
        if self.ui.szyfrujRadio.isChecked():
            self.ui.buttonSzyfruj.setText("Zaszyfruj")
        else:
            self.ui.buttonSzyfruj.setText("Odszyfruj")

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

    def otworz_plik(self):
        """
        Otwiera plik i ładuje go do pola tekstu do obsługi
        """
        interfejs = self.ui
        options = QtWidgets.QFileDialog.Options()
        nazwa_pliku, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Otwórz plik",
            "",
            "Pliki tekstowe (*.txt);;Wszystkie pliki (*)",
            options=options)
        if nazwa_pliku:
            with open(nazwa_pliku, 'r', encoding="utf-8") as plik:
                try:
                    dane_z_pliku = plik.read()
                    interfejs.tekstJawny.setPlainText(dane_z_pliku)
                except UnicodeDecodeError:
                    self.blad_pokaz("Błędny plik, musi być tekstowy")

    def zapisz_plik(self):
        """
        Zapisuje plik wynikowy do pliku na komputerze
        """
        try:
            text = self.ui.tekstZaszyfrowany.toPlainText()
            if text is not "":
                options = QtWidgets.QFileDialog.Options()
                nazwa_pliku, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    'Zapisz plik', "",
                    "Pliki tekstowe (*.txt)",
                    options=options)
                file = open(nazwa_pliku, 'w', encoding="utf-8")
                file.write(text)
                file.close()
                self.blad_pokaz("Zapisano!", "Sukces")
            else:
                self.blad_pokaz("Brak zaszyfrowanego tekstu!")
        except UnicodeEncodeError:
            self.blad_pokaz("Błąd zapisu pliku")

    def zapisz_klucz(self):
        """
        Zapisuje klucz na komputerze
        """
        try:
            text = self.ui.klucz.text()
            if text is not "":
                options = QtWidgets.QFileDialog.Options()
                nazwa_pliku, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    'Zapisz klucz', "",
                    "Pliki tekstowe (*.txt)",
                    options=options)
                file = open(nazwa_pliku, 'w', encoding="utf-8")
                file.write(text)
                file.close()
                self.blad_pokaz("Zapisano!", "Sukces")
            else:
                self.blad_pokaz("Brak klucza!")
        except UnicodeEncodeError:
            self.blad_pokaz("Błąd zapisu pliku")

    def licznik_tesktu(self):
        """
        Liczy ilość znaków w tekście pierwotnym i wyświetla to jako liczbe
        """
        interfejs = self.ui
        interfejs.licznikTekstuJawnego.display(len(interfejs.tekstJawny.toPlainText()))

    def zmiana_dlugosci_klucza(self):
        """
        Ustawienie ograniczeń po zmianie długości klucz
        """
        interfejs = self.ui
        dlugosc_tekstu = int(interfejs.dlugoscKlucza.currentText()) * 2
        interfejs.klucz.setMaxLength((dlugosc_tekstu / 16) / 2)
        interfejs.liczbaPrzebiegow.setMaximum(int(interfejs.dlugoscKlucza.currentText()) * 2)

    def wstaw_szyfrowany(self):
        """
        Przeniesienie tekstu z pola wynikowego do pola wprowadzania
        """
        interfejs = self.ui
        interfejs.tekstJawny.setPlainText(interfejs.tekstZaszyfrowany.toPlainText())

    def generuj_klucz(self):
        """
        Przycisk generowania klucza
        """
        interfejs = self.ui
        dlugosc_tekstu = int(interfejs.dlugoscKlucza.currentText()) * 2
        wygenerowany_klucz = ""
        for x in range(0, int((dlugosc_tekstu / 16) / 2)):
            wygenerowany_klucz += chr(random.randrange(49, 122))
        interfejs.klucz.setText(wygenerowany_klucz)

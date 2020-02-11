from PyQt5 import QtWidgets
from startui import Ui_Dialog as startUI


class OknoAplikacji(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = startUI()
        self.ui.setupUi(self)
        self.ui.dlugoscKlucza.setCurrentIndex(2)
        self.ui.drugaMetoda.setCurrentIndex(0)

        self.ui.klucz.setMaxLength(int(self.ui.dlugoscKlucza.currentText()) / 16)
        self.ui.liczbaPrzebiegow.setMaximum(512 / 16)

        self.ui.tekstJawny.textChanged.connect(self.licznik_tesktu)
        self.ui.dlugoscKlucza.currentIndexChanged.connect(self.zmiana_dlugosci_klucza)
        self.ui.pokazSzczegoly.stateChanged.connect(self.zmiana_szczegolow)
        self.ui.szyfrujRadio.toggled.connect(self.zmiana_wartosci_klawisza_szyfrowania)
        self.show()

    def otwarcie_pliku(self, lokalizacja_pliku):
        interfejs = self.ui
        with open(lokalizacja_pliku, 'r', encoding="utf-8") as plik:
            try:
                dane_z_pliku = plik.read()
                interfejs.tekstJawny.setText(dane_z_pliku)
            except:
                self.blad_pokaz("Błędny plik, musi być tekstowy")

    def zmiana_wartosci_klawisza_szyfrowania(self):
        if self.ui.szyfrujRadio.isChecked():
            self.ui.buttonSzyfruj.setText("Zaszyfruj")
        else:
            self.ui.buttonSzyfruj.setText("Odszyfruj")

    @staticmethod
    def blad_pokaz(tekst, nazwa_okna="Błąd"):
        mb = QtWidgets.QMessageBox()
        mb.setIcon(QtWidgets.QMessageBox.Information)
        mb.setWindowTitle(nazwa_okna)
        mb.setText(tekst)
        mb.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mb.show()
        mb.exec_()

    def otworz_plik(self):
        options = QtWidgets.QFileDialog.Options()
        nazwa_pliku, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Otwórz plik",
            "",
            "Pliki tekstowe (*.txt);;Wszystkie pliki (*)",
            options=options)
        if nazwa_pliku:
            self.otwarcie_pliku(nazwa_pliku)

    def zapisz_plik(self):
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
        except:
            self.blad_pokaz("Błąd zapisu pliku")

    def licznik_tesktu(self):
        interfejs = self.ui
        interfejs.licznikTekstuJawnego.display(len(interfejs.tekstJawny.text()))

    def zmiana_dlugosci_klucza(self):
        interfejs = self.ui
        dlugosc_tekstu = int(interfejs.dlugoscKlucza.currentText()) * 2
        interfejs.klucz.setMaxLength((dlugosc_tekstu / 16) / 2)

    def zmiana_szczegolow(self):
        interfejs = self.ui
        if interfejs.pokazSzczegoly.isChecked():
            interfejs.kodBinarny.setEnabled(True)
            interfejs.binarnyZaszyfrowany.setEnabled(True)
        else:
            interfejs.kodBinarny.setEnabled(False)
            interfejs.binarnyZaszyfrowany.setEnabled(False)
            interfejs.kodBinarny.setPlainText("")
            interfejs.binarnyZaszyfrowany.setPlainText("")

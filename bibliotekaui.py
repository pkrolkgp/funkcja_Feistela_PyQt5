# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Piotr\PycharmProjects\Test\biblioteka.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 438)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.wczytajNowy = QtWidgets.QPushButton(Form)
        self.wczytajNowy.setObjectName("wczytajNowy")
        self.horizontalLayout.addWidget(self.wczytajNowy)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exportujWybrany = QtWidgets.QPushButton(Form)
        self.exportujWybrany.setObjectName("exportujWybrany")
        self.verticalLayout_2.addWidget(self.exportujWybrany)
        self.exportujCaly = QtWidgets.QPushButton(Form)
        self.exportujCaly.setObjectName("exportujCaly")
        self.verticalLayout_2.addWidget(self.exportujCaly)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.usunWybrany = QtWidgets.QPushButton(Form)
        self.usunWybrany.setObjectName("usunWybrany")
        self.horizontalLayout.addWidget(self.usunWybrany)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.labelOdczytKlucza = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelOdczytKlucza.setFont(font)
        self.labelOdczytKlucza.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOdczytKlucza.setObjectName("labelOdczytKlucza")
        self.verticalLayout.addWidget(self.labelOdczytKlucza)
        self.odczytKluczaPublicznego = QtWidgets.QLineEdit(Form)
        self.odczytKluczaPublicznego.setObjectName("odczytKluczaPublicznego")
        self.verticalLayout.addWidget(self.odczytKluczaPublicznego)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.tabelaKluczy = QtWidgets.QTableWidget(Form)
        self.tabelaKluczy.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaKluczy.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaKluczy.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabelaKluczy.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabelaKluczy.setWordWrap(False)
        self.tabelaKluczy.setObjectName("tabelaKluczy")
        self.tabelaKluczy.setColumnCount(4)
        self.tabelaKluczy.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaKluczy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaKluczy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaKluczy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaKluczy.setHorizontalHeaderItem(3, item)
        self.tabelaKluczy.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelaKluczy.horizontalHeader().setStretchLastSection(True)
        self.tabelaKluczy.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tabelaKluczy)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Biblioteka kluczy"))
        self.wczytajNowy.setText(_translate("Form", "Importuj nowy klucz"))
        self.exportujWybrany.setText(_translate("Form", "Eksportuj wybrany publiczny"))
        self.exportujCaly.setText(_translate("Form", "Eksportuj wybrany prywatny"))
        self.usunWybrany.setText(_translate("Form", "Usuń wybrany"))
        self.labelOdczytKlucza.setText(_translate("Form", "Klucz publiczny"))
        item = self.tabelaKluczy.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nazwa"))
        item = self.tabelaKluczy.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Liczba - n"))
        item = self.tabelaKluczy.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Publiczny - e"))
        item = self.tabelaKluczy.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Prywatny - d"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
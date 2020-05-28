# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Piotr\PycharmProjects\Test\sprawdzenie.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(347, 348)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutSzyfrujacego = QtWidgets.QHBoxLayout()
        self.layoutSzyfrujacego.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layoutSzyfrujacego.setObjectName("layoutSzyfrujacego")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.kluczeSprawdzenia = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kluczeSprawdzenia.sizePolicy().hasHeightForWidth())
        self.kluczeSprawdzenia.setSizePolicy(sizePolicy)
        self.kluczeSprawdzenia.setObjectName("kluczeSprawdzenia")
        self.verticalLayout_2.addWidget(self.kluczeSprawdzenia)
        self.layoutSzyfrujacego.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.layoutSzyfrujacego)
        self.layoutSzyfrowanego = QtWidgets.QHBoxLayout()
        self.layoutSzyfrowanego.setObjectName("layoutSzyfrowanego")
        self.verticalLayout.addLayout(self.layoutSzyfrowanego)
        self.layoutGenerowania = QtWidgets.QVBoxLayout()
        self.layoutGenerowania.setObjectName("layoutGenerowania")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wczytajPodpisany = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wczytajPodpisany.setFont(font)
        self.wczytajPodpisany.setObjectName("wczytajPodpisany")
        self.verticalLayout_4.addWidget(self.wczytajPodpisany)
        self.poleKlucza = QtWidgets.QTextEdit(Form)
        self.poleKlucza.setObjectName("poleKlucza")
        self.verticalLayout_4.addWidget(self.poleKlucza)
        self.Sprawdz = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sprawdz.setFont(font)
        self.Sprawdz.setObjectName("Sprawdz")
        self.verticalLayout_4.addWidget(self.Sprawdz)
        spacerItem1 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.layoutGenerowania.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.layoutGenerowania)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Podpisywanie Kluczy"))
        self.label.setText(_translate("Form", "Wybierz klucz osoby certyfikującej"))
        self.wczytajPodpisany.setText(_translate("Form", "Wczytaj podpisany klucz"))
        self.Sprawdz.setText(_translate("Form", "Sprawdź"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

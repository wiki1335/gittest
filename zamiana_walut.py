#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class ZamianaWalut(QWidget):
    def __init__(self, parent=None):
        super(ZamianaWalut, self).__init__(parent)

        self.interfejs()

    def interfejs(self):

        #etykiety
        etykieta1 = QLabel("Zamień z: ")
        etykieta2 = QLabel("Zamień na: ")
        etykieta3 = QLabel("Cena w złotówkach: ")
        etykieta4 = QLabel("Aktualny kurs: ")
        etykieta5 = QLabel("Wynik: ")

        #pola edycyjne
        self.cena = QLineEdit()
        self.kurs = QLineEdit()
        self.wynik = QLineEdit()
        self.zamienz = QLineEdit()
        self.zamienna = QLineEdit()

        #uklad tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 2, 0)
        ukladT.addWidget(etykieta4, 2, 1)
        ukladT.addWidget(etykieta5, 2, 2)

        ukladT.addWidget(self.zamienz,1, 0)
        ukladT.addWidget(self.zamienna,1, 1)

        ukladT.addWidget(self.cena, 3, 0)
        ukladT.addWidget(self.kurs, 3, 1)
        ukladT.addWidget(self.wynik, 3, 2)


        #przyciski
        zamienBtn = QPushButton("&Zamień", self)
        koniecBtn = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(zamienBtn)


        ukladT.addLayout(ukladH, 4, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 5, 0, 1, 3)


        self.setLayout(ukladT)

        # obsluga zdarzen
        koniecBtn.clicked.connect(self.koniec)
        zamienBtn.clicked.connect(self.dzialanie)


        self.resize(500, 200)
        self.setWindowTitle("ZamianaWalut")
        self.show()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def koniec(self):
        self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:

            cena = float(self.cena.text())
            kurs = float(self.kurs.text())

            if nadawca.text() == "&Zamień":
                wynik = cena * kurs
            else:
                pass

            self.wynik.setText(str(wynik))
        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = ZamianaWalut()
    sys.exit(app.exec_())

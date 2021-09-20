from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prenotazione.model.Prenotazione import Prenotazione
from PyQt5.QtCore import QSize, QRect
from PyQt5 import QtCore, QtWidgets
import images3

class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        self.setObjectName("VistaInserisciPrenotazione")
        self.resize(500, 400)
        self.setMinimumSize(QSize(500, 400))
        self.setMaximumSize(QSize(500, 400))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 500, 400))
        self.sfondo.setPixmap(QPixmap(u"sfondoInserisciPrenotazione.jpg"))
        self.sfondo.setScaledContents(True)

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome_cliente", "Nome Cliente")
        self.add_info_text("cognome_cliente", "Cognome Cliente")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("email", "Email")
        self.add_info_text("data", "Data Prenotazione")
        self.add_info_text("tavola", "Tavolo Prenotato")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.Button_OK = QtWidgets.QPushButton(self)
        self.Button_OK.setGeometry(QtCore.QRect(150, 300, 200, 60))
        self.Button_OK.setStyleSheet("QPushButton#Button_OK{\n"
                                     "  background-color:#663300;\n"
                                     "  border-radius: 10px;\n"
                                     "  color: white;\n"
                                     "  padding: 16px 32px;\n"
                                     "  text-align: center;\n"
                                     "  text-decoration: none;\n"
                                     "  display: inline-block;\n"
                                     "  font-size: 16px;\n"
                                     "  margin: 4px 2px;\n"
                                     "  transition-duration: 0.4s;\n"
                                     "  cursor: pointer;\n"
                                     "}\n"
                                     "QPushButton#Button_OK:pressed{\n"
                                     " background-color: white; \n"
                                     "  color: black; \n"
                                     "  border: 3px solid #4CAF50;\n"
                                     "}\n"
                                     "QPushButton#Button_OK:hover {background-color:      #ffe066;}\n"
                                     "")
        self.Button_OK.setObjectName("Button_OK")
        self.Button_OK.clicked.connect(self.add_prenotazione)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.v_layout)


    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_prenotazione(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_prenotazione(Prenotazione(
            (self.qlines["nome_cliente"].text()+self.qlines["cognome_cliente"].text()).lower(),
            self.qlines["nome_cliente"].text(),
            self.qlines["cognome_cliente"].text(),
            self.qlines["telefono"].text(),
            self.qlines["email"].text(),
            self.qlines["data"].text(),
            self.qlines["tavola"].text())

        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_OK.setText(_translate("VistaInserisciPrenotazione", "OK"))
        self.callback()
        self.close()


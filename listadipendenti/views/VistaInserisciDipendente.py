from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from dipendente.model.Dipendente import Dipendente
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QRect
import images3

class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        self.setObjectName("VistaInserisciDipendente")
        self.resize(600, 500)
        self.setMinimumSize(QSize(600, 500))
        self.setMaximumSize(QSize(600, 500))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 600, 500))
        self.sfondo.setPixmap(QPixmap(u"sfondoInserisciDip.jpg"))
        self.sfondo.setScaledContents(True)

        #self.LogoDipendente = QLabel(self)
        #self.LogoDipendente.setObjectName(u"LogoDipendente")
        #self.LogoDipendente.setGeometry(QRect(200, 10, 141, 131))
        #self.LogoDipendente.setPixmap(QPixmap(u":/newPrefix/logoDipendente.png"))
        #self.LogoDipendente.setScaledContents(True)

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("residenza", "Residenza")
        self.add_info_text("cap", "CAP")
        self.add_info_text("professione", "Professione")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.Button_OK = QtWidgets.QPushButton(self)
        self.Button_OK.setGeometry(QtCore.QRect(180, 420, 200, 60))
        self.Button_OK.setStyleSheet("QPushButton#Button_OK{\n"
                                     "  background-color:#293d3d;\n"
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
                                     "QPushButton#Button_OK:hover {background-color:      #d1e0e0;}\n"
                                     "")
        self.Button_OK.setObjectName("Button_OK")
        self.Button_OK.clicked.connect(self.add_dipendente)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.v_layout)



    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_dipendente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_dipendente(Dipendente(
            (self.qlines["nome"].text()+self.qlines["cognome"].text()).lower(),
            self.qlines["nome"].text(),
            self.qlines["cognome"].text(),
            self.qlines["cf"].text(),
            self.qlines["data_n"].text(),
            self.qlines["email"].text(),
            self.qlines["telefono"].text(),
            self.qlines["residenza"].text(),
            self.qlines["cap"].text(),
            self.qlines["professione"].text())
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_OK.setText(_translate("VistaInserisciDipendente", "OK"))
        self.callback()
        self.close()


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prenotazione.model.Prenotazione import Prenotazione
from PyQt5.QtCore import QSize, QRect
import images3

class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        self.setObjectName("VistaInserisciPrenotazione")
        self.resize(600, 500)
        self.setMinimumSize(QSize(600, 500))
        self.setMaximumSize(QSize(600, 500))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 600, 500))
        self.sfondo.setPixmap(QPixmap(u":/newPrefix/texture.jpg"))
        self.sfondo.setScaledContents(True)

        #self.LogoDipendente = QLabel(self)
        #self.LogoDipendente.setObjectName(u"LogoDipendente")
        #self.LogoDipendente.setGeometry(QRect(200, 10, 141, 131))
        #self.LogoDipendente.setPixmap(QPixmap(u":/newPrefix/logoDipendente.png"))
        #self.LogoDipendente.setScaledContents(True)

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome_cliente", "Nome Cliente")
        self.add_info_text("cognome_cliente", "Cognome Cliente")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("email", "Email")
        self.add_info_text("data", "Data Prenotazione")
        self.add_info_text("tavola", "Tavolo Prenotato")
        #self.resize(600, 500)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        #self.setWindowTitle("Nuovo Dipendente")

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
        self.callback()
        self.close()


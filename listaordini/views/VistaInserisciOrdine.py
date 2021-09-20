from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QMessageBox, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtWidgets
from ordine.model.Ordine import Ordine


class VistaInserisciOrdine(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciOrdine, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.setObjectName("VistaInserisciOrdine")
        self.resize(500, 400)
        self.setMinimumSize(QSize(500, 400))
        self.setMaximumSize(QSize(500, 400))


        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 500, 400))
        self.sfondo.setPixmap(QPixmap(u"texture.jpg"))
        self.sfondo.setScaledContents(True)

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("cod_fattura", "Codice fattura")
        self.add_info_text("stato", "Stato")
        self.add_info_text("numero_tavola", "Numero tavola")
        self.add_info_text("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
        self.add_info_text("importo_totale", "importo totale")
        self.add_info_text("quantita_totale", "Quantita totale")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.Button_OK = QtWidgets.QPushButton(self)
        self.Button_OK.setGeometry(QtCore.QRect(150, 300, 200, 70))
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
        self.Button_OK.clicked.connect(self.inserisci_ordine)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setLayout(self.v_layout)
        self.setWindowTitle("New")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)




    def inserisci_ordine(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return

        #cod_fattura = self.info["cod_fattura"].text()
        #stato = self.info["stato"].text()
        #numero_tavola = self.info["numero_tavola"].text()
        #data_ordine = self.info["data_ordine"].text()
        #importo_totale = self.info["importo_totale"].text()
        #quantita_totale = self.info["quantita_totale"].text()
        self.controller.aggiungi_ordine(Ordine(
            (self.qlines["cod_fattura"].text()).lower(),
            #self.qlines["cod_fattura"].text(),
            self.qlines["stato"].text(),
            self.qlines["numero_tavola"].text(),
            self.qlines["data_ordine"].text(),
            self.qlines["importo_totale"].text(),
            self.qlines["quantita_totale"].text())
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_OK.setText(_translate("VistaInserisciOrdine", "OK"))

        self.callback()
        self.close()
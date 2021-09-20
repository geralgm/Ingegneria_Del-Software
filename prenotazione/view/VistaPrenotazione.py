from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from PyQt5 import QtCore,QtWidgets

class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, elimina_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.elimina_prenotazione = elimina_prenotazione
        self.elimina_callback = elimina_callback

        self.setObjectName("VistaPrenotazione")
        self.resize(407, 453)
        self.setMinimumSize(QSize(407, 453))
        self.setMaximumSize(QSize(407, 453))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"label")
        self.sfondo.setGeometry(QRect(0, 0, 407, 453))
        self.sfondo.setPixmap(QPixmap(u"sfondoPrenotazione.jpg"))

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente_prenotazione() + " " + self.controller.get_cognome_cliente_prenotazione())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Nome Cliente: {}".format(self.controller.get_nome_cliente_prenotazione())))
        v_layout.addWidget(self.get_info("Cognome Ciente: {}".format(self.controller.get_cognome_cliente_prenotazione())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_cliente_prenotazione())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email_cliente_prenotazione())))
        v_layout.addWidget(self.get_info("Data Prenotata: {}".format(self.controller.get_data_prenotazione())))
        v_layout.addWidget(self.get_info("Tavola Prenotata: {}".format(self.controller.get_telefono_cliente_prenotazione())))




        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.Button_Elimina = QtWidgets.QPushButton(self)
        self.Button_Elimina.setGeometry(QtCore.QRect(120, 380, 150, 68))
        self.Button_Elimina.setStyleSheet("QPushButton#Button_Elimina{\n"
                                          "  background-color:#663300;\n"
                                          "  border-radius: 30px;\n"
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
                                          "QPushButton#Button_Elimina:pressed{\n"
                                          " background-color: white; \n"
                                          "  color: black; \n"
                                          "  border: 3px solid #4CAF50;\n"
                                          "}\n"
                                          "QPushButton#Button_Elimina:hover {background-color:      #ffe066;}\n"
                                          "")
        self.Button_Elimina.setObjectName("Button_Elimina")
        self.Button_Elimina.clicked.connect(self.elimina_prenotazione_click)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente_prenotazione())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_prenotazione_click(self):
        self.elimina_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_Elimina.setText(_translate("VistaPrenotazione", "Elimina"))
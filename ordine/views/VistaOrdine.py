import time

from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from ordine.controller.ControllerOrdine import ControllerOrdine
from PyQt5 import QtCore,QtWidgets


class VistaOrdine(QWidget):
    def __init__(self, ordine, elimina_ordine, elimina_callback, parent=None):
        super(VistaOrdine, self).__init__(parent)
        self.controller = ControllerOrdine(ordine)
        self.elimina_ordine = elimina_ordine
        self.elimina_callback = elimina_callback

        self.setObjectName("VistaOrdine")
        self.resize(407, 453)
        self.setMinimumSize(QSize(407, 453))
        self.setMaximumSize(QSize(407, 453))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"label")
        self.sfondo.setGeometry(QRect(0, 0, 407, 453))
        self.sfondo.setPixmap(QPixmap(u"sfondoOrdine.jpg"))

        self.Button_Elimina = QtWidgets.QPushButton(self)
        self.Button_Elimina.setGeometry(QtCore.QRect(120, 380, 150, 68))
        self.Button_Elimina.setStyleSheet("QPushButton#Button_Elimina{\n"
                                          "  background-color:#293d3d;\n"
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
                                          "QPushButton#Button_Elimina:hover {background-color:      #d1e0e0;}\n"
                                          "")
        self.Button_Elimina.setObjectName("Button_Elimina")
        self.Button_Elimina.clicked.connect(self.elimina_ordine_click)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        v_layout = QVBoxLayout()

        label_nome = QLabel(str(self.controller.get_cod_fattura()))
        font_nome = label_nome.font()
        font_nome.setPointSize(40)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        v_layout.addWidget(self.get_info("Numero di tavola: {}".format(self.controller.get_numero_tavola())))
        v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        v_layout.addWidget(self.get_info("Importo totale : {}".format(self.controller.get_importo_totale())))
        v_layout.addWidget(self.get_info("Quantita_totale: {}".format(self.controller.get_quantita_totale())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


       # btn_modifica = QPushButton("Modifica")
       # btn_modifica.clicked.connect(self.modifica_prodotto_click)
       # v_layout.addWidget(btn_modifica)

       # btn_back = QPushButton("Indietro")
        #btn_back.clicked.connect(self.show_back_click)
        #v_layout.addWidget(btn_back)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_cod_fattura())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_ordine_click(self):
        self.elimina_ordine(self.controller.get_cod_fattura())
        self.elimina_callback
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_Elimina.setText(_translate("VistaDipendente", "Elimina"))


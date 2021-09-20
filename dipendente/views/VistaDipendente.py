from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente

from PyQt5 import QtCore, QtWidgets


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        self.setObjectName(u"Form")
        self.resize(400, 600)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 400, 600))
        self.label.setPixmap(QPixmap(u"sfondoDip.jpg"))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 20, 161, 151))
        self.label_2.setPixmap(QPixmap(u"logoDip.png"))
        self.label_2.setScaledContents(True)

        self.Button_Elimina = QtWidgets.QPushButton(self)
        self.Button_Elimina.setGeometry(QtCore.QRect(125, 540, 150, 55))
        self.Button_Elimina.setStyleSheet("QPushButton#Button_Elimina{\n"
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
                                          "QPushButton#Button_Elimina:pressed{\n"
                                          " background-color: white; \n"
                                          "  color: black; \n"
                                          "  border: 3px solid #4CAF50;\n"
                                          "}\n"
                                          "QPushButton#Button_Elimina:hover {background-color:      #d1e0e0;}\n"
                                          "")
        self.Button_Elimina.setObjectName("Button_Elimina")
        self.Button_Elimina.clicked.connect(self.elimina_dipendente_click)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        v_layout = QVBoxLayout()

        v_layout.addItem(QSpacerItem(200, 180, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_dipendente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_datanascita_dipendente())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email_dipendente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("Residenza: {}".format(self.controller.get_residenza_dipendente())))
        v_layout.addWidget(self.get_info("CAP: {}".format(self.controller.get_cap_dipendente())))
        v_layout.addWidget(self.get_info("Professione: {}".format(self.controller.get_professione_dipendente())))



        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        #btn_elimina.clicked.connect(self.elimina_dipendente_click)
        #btn_elimina = QPushButton("Elimina")

        #v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_Elimina.setText(_translate("VistaDipendente", "Elimina"))
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QWidget, QApplication
import images
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listaportate.view.GUI_ListaPortate import GUI_ListaPortate
from listaordini.views.VistaListaOrdine import VistaListaOrdini
from listadipendenti.views.GUI_ListaDipendenti import VistaListaDipendenti
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni




class Home(QWidget):


    def __init__(self, parent=None):
        super(Home, self).__init__(parent)

        self.setObjectName("Home")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.resize(730, 584)
        self.setMinimumSize(QtCore.QSize(730, 584))
        self.setMaximumSize(QtCore.QSize(730, 584))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.setStyleSheet("")

        self.sfondo = QtWidgets.QLabel(self)
        self.sfondo.setGeometry(QtCore.QRect(0, 0, 730, 584))
        self.sfondo.setStyleSheet("")
        self.sfondo.setText("")
        self.sfondo.setPixmap(QtGui.QPixmap(":/newPrefix/texture4.jpg"))
        self.sfondo.setScaledContents(True)
        self.sfondo.setObjectName("sfondo")

        self.label_Logo = QtWidgets.QLabel(self)
        self.label_Logo.setGeometry(QtCore.QRect(230, 20, 241, 201))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap(":/newPrefix/logoRistorante.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")

        self.Button_Ordini = QtWidgets.QPushButton(self)
        self.Button_Ordini.setGeometry(QtCore.QRect(80, 250, 250, 100))
        self.Button_Ordini.setStyleSheet("QPushButton#Button_Ordini{\n"
                                            "  background-color: #663300;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Ordini:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#Button_Ordini:hover {background-color:     #1f2e2e;}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.Button_Ordini.setObjectName("Button_Ordini")


        self.Button_Prenotazioni = QtWidgets.QPushButton(self)
        self.Button_Prenotazioni.setGeometry(QtCore.QRect(400, 250, 250, 100))
        self.Button_Prenotazioni.setStyleSheet("QPushButton#Button_Prenotazioni{\n"
                                                "  background-color: #804d00;\n"
                                                "  border-radius: 45px;\n"
                                                "  color: white;\n"
                                                "  padding: 16px 32px;\n"
                                                "  text-align: center;\n"
                                                "  text-decoration: none;\n"
                                                "  display: inline-block;\n"
                                                "  font-size: 22px;\n"
                                                "  margin: 4px 2px;\n"
                                                "  transition-duration: 0.4s;\n"
                                                "  cursor: pointer;\n"
                                                "}\n"
                                                "QPushButton#Button_Prenotazioni:pressed{\n"
                                                " background-color: white; \n"
                                                "  color: black; \n"
                                                "  border: 2px solid #4CAF50;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton#Button_Prenotazioni:hover {background-color:     #ffe066;}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
        self.Button_Prenotazioni.setObjectName("Button_Prenotazioni")

        self.Button_Dipendenti = QtWidgets.QPushButton(self)
        self.Button_Dipendenti.setGeometry(QtCore.QRect(80, 400, 250, 100))
        self.Button_Dipendenti.setStyleSheet("QPushButton#Button_Dipendenti{\n"
                                                "  background-color:#804d00;\n"
                                                "  border-radius: 45px;\n"
                                                "  color: white;\n"
                                                "  padding: 16px 32px;\n"
                                                "  text-align: center;\n"
                                                "  text-decoration: none;\n"
                                                "  display: inline-block;\n"
                                                "  font-size: 22px;\n"
                                                "  margin: 4px 2px;\n"
                                                "  transition-duration: 0.4s;\n"
                                                "  cursor: pointer;\n"
                                                "}\n"
                                                "QPushButton#Button_Dipendenti:pressed{\n"
                                                " background-color: white; \n"
                                                "  color: black; \n"
                                                "  border: 2px solid #4CAF50;\n"
                                                "}\n"
                                                "QPushButton#Button_Dipendenti:hover {background-color:      #ffe066;}\n"
                                                "")
        self.Button_Dipendenti.setObjectName("Button_Dipendenti")

        self.Button_Menu = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Menu.sizePolicy().hasHeightForWidth())
        self.Button_Menu.setSizePolicy(sizePolicy)
        self.Button_Menu.setGeometry(QRect(590, 35, 80, 100))
        self.Button_Menu.setFont(font)
        self.Button_Menu.setObjectName("Button_Menu")
        self.Button_Menu.setStyleSheet("QPushButton {\n"
                                       "    border-radius:5px;\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 0px;\n"

                                       "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('dinner-menu-icon-28.jpg'))
        self.Button_Menu.setIcon(icon)
        self.Button_Menu.setIconSize(QSize(self.width / 7, self.height / 7))
        self.gridLayout_2.addWidget(self.Button_Menu, 5, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.Button_Fornitori = QtWidgets.QPushButton(self)
        self.Button_Fornitori.setGeometry(QtCore.QRect(400, 400, 250, 100))
        self.Button_Fornitori.setStyleSheet("QPushButton#Button_Fornitori{\n"
                                            "  background-color:#663300;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Fornitori:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "QPushButton#Button_Fornitori:hover {background-color:      #1f2e2e;}\n"
                                            "")
        self.Button_Fornitori.setObjectName("Button_Fornitori")


        self.Button_Dipendenti.clicked.connect(self.go_lista_dipendenti)
        self.Button_Menu.clicked.connect(self.go_lista_portate)
        self.Button_Fornitori.clicked.connect(self.go_lista_fornitori)
        self.Button_Ordini.clicked.connect(self.go_lista_ordini)
        self.Button_Prenotazioni.clicked.connect(self.go_lista_prenotazioni)


        self.setWindowTitle("Home")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_Ordini.setText(_translate("Home", "Ordini"))
        self.Button_Prenotazioni.setText(_translate("Home", "Prenotazioni"))
        self.Button_Dipendenti.setText(_translate("Home", "Dipendenti"))
        self.Button_Fornitori.setText(_translate("Home", "Fornitori"))



    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_portate(self):
        self.vista_lista_portate= GUI_ListaPortate()
        self.vista_lista_portate.showMaximized()

    def go_lista_fornitori(self):
        self.VistaListaFornitori= VistaListaFornitori()
        self.VistaListaFornitori.showMaximized()

    def go_lista_prenotazioni(self):
        self.VistaListaPrenotazioni= VistaListaPrenotazioni()
        self.VistaListaPrenotazioni.showMaximized()

    def go_lista_ordini(self):
        self.VistaListaOrdini = VistaListaOrdini()
        self.VistaListaOrdini.showMaximized()

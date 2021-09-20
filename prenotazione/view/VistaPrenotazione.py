from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, elimina_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.elimina_prenotazione = elimina_prenotazione
        self.elimina_callback = elimina_callback

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

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_prenotazione_click)
        v_layout.addWidget(btn_elimina)

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
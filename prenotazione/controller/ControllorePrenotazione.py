class ControllorePrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        return self.model.id

    def get_nome_cliente_prenotazione(self):
        return self.model.nome_cliente

    def get_cognome_cliente_prenotazione(self):
        return self.model.cognome_cliente

    def get_telefono_cliente_prenotazione(self):
        return self.model.telefono

    def get_email_cliente_prenotazione(self):
        return self.model.email

    def get_data_prenotazione(self):
        return self.model.data
    def get_tavola_prenotazione(self):
        return self.model.tavola
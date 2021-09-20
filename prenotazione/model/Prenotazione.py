class Prenotazione():
    def __init__(self, id, nome_cliente, cognome_cliente,telefono,email,data,tavola):
        super(Prenotazione, self).__init__()
        self.id = id
        self.nome_cliente=nome_cliente
        self.cognome_cliente=cognome_cliente
        self.telefono=telefono
        self.email=email
        self.data = data
        self.tavoa=tavola
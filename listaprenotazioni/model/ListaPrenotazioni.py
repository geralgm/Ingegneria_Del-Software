import os
import pickle


class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.lista_prenotazioni = []
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni = pickle.load(f)

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def rimuovi_prenotazione_by_id(self, id):
        def is_selected_prenotazione(prenotazione):
            if prenotazione.id == id:
                return True
            return False
        self.lista_prenotazioni.remove(list(filter(is_selected_prenotazione, self.lista_prenotazioni))[0])

    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)
import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_ddCorso(self):
        corsi = self._model.get_corsi()
        for corso in corsi:
            self._view._ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def handle_get_iscritti_by_codins(self, e):
        self.__clear()
        iscritti = self._model.get_iscritti_by_codins(self.__getCodins())
        self._view._txt_result.controls.append(ft.Text(f'Ci sono {len(iscritti)} studenti iscritti al corso:'))
        for iscritto in iscritti:
            self._view._txt_result.controls.append(ft.Text(f'{iscritto.nome}, {iscritto.cognome} ({iscritto.matricola})'))
        self._view.update()
    
    def handle_get_studente_by_matricola(self, e):
        studente = self._model.get_studente_by_matricola(self.__getMatricola())
        self._view._txtNome.value = studente.nome
        self._view._txtCognome.value = studente.cognome
        self._view.update()

    def handle_get_corsi_by_matricola(self, e):
        self.__clear()
        corsi_studente = self._model.get_corsi_by_matricola(self.__getMatricola())
        self._view._txt_result.controls.append(ft.Text(f'Risultano {len(corsi_studente)} corsi:'))
        for corso in corsi_studente:
            self._view._txt_result.controls.append(ft.Text(f'{corso.__str__()}'))
        self._view.update()

    def handle_iscrivi_studente(self, e):
        self.__clear()
        iscrizione = False
        iscrizione = self._model.iscrivi_studente(self.__getMatricola(), self.__getCodins())
        if iscrizione:
            self._view._txt_result.controls.append(ft.Text('Iscrizione effettuata con successo!', color='green'))
        self._view.update()

    def __clear(self):
        self._view._txt_result.controls.clear()

    def __getCodins(self):
        return self._view._ddCorso.value
    
    def __getMatricola(self):
        return self._view._txtMatricola.value    
    
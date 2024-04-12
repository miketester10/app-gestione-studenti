from database.studente_DAO import studente_DAO
from database.corso_DAO import corso_DAO

class Model:
    def __init__(self):
        pass

    def get_corsi(self):
        self._corsi = corso_DAO.get_corsi()
        return self._corsi
    
    def get_iscritti_by_codins(self, codins):
        self._iscritti = studente_DAO.get_iscritti_by_codins(codins)
        return self._iscritti
    
    def get_studente_by_matricola(self, matricola):
        self._studente = studente_DAO.get_studente_by_matricola(matricola)
        return self._studente
    
    def get_corsi_by_matricola(self, matricola):
        self._corsi_studente = corso_DAO.get_corsi_by_matricola(matricola)
        return self._corsi_studente
    
    def iscrivi_studente(self, matricola, codins):
        success = studente_DAO.iscrivi_studente(matricola, codins)
        return success


    


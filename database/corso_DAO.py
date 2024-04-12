# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

class corso_DAO():
    def __init__(self):
        pass

    def get_corsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM corso;
                """
        cursor.execute(query,)
        result = cursor.fetchall()

        corsi = [Corso(codins=row['codins'], crediti=row['crediti'], nome=row['nome'], pd=row['pd']) for row in result]

        cursor.close()
        cnx.close()
        return corsi
    
    def get_corsi_by_matricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT corso.*
                FROM studente
                JOIN iscrizione ON studente.matricola  = iscrizione.matricola 
                JOIN corso ON iscrizione.codins  = corso.codins 
                WHERE studente.matricola = (%s);
                """
        cursor.execute(query, (matricola,))
        result = cursor.fetchall()

        corsi = [Corso(codins=row['codins'], crediti=row['crediti'], nome=row['nome'], pd=row['pd']) for row in result]

        cursor.close()
        cnx.close()
        return corsi
    

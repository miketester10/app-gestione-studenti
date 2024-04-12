# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import get_connection
from model.studente import Studente

class studente_DAO:
    def __init__(self):
        pass

    def get_iscritti_by_codins(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.*
                FROM studente
                JOIN iscrizione ON studente.matricola  = iscrizione.matricola 
                JOIN corso ON iscrizione.codins  = corso.codins 
                WHERE corso.codins = (%s);
                """
        cursor.execute(query, (codins,))
        result = cursor.fetchall()

        studenti = [Studente(matricola=row['matricola'], cognome=row['cognome'], nome=row['nome'], CDS=row['CDS']) for row in result]

        cursor.close()
        cnx.close()
        return studenti
    
    def get_studente_by_matricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM studente
                WHERE matricola = (%s);
                """
        cursor.execute(query, (matricola,))
        result = cursor.fetchone()

        studente = Studente(matricola=result['matricola'], cognome=result['cognome'], nome=result['nome'], CDS=result['CDS'])

        cursor.close()
        cnx.close()
        return studente

    def iscrivi_studente(matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO iscrizione 
                (matricola, codins)
                VALUES (%s, %s);
                """
        cursor.execute(query, (matricola, codins))
        cnx.commit()

        cursor.close()
        cnx.close()
        return True 

# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import DBConnect
from model.studente import Studente

class studente_DAO:
    '''
    @staticmethod: 
    Questo decoratore definisce un metodo statico. I metodi statici non ricevono automaticamente alcun argomento 
    relativo alla classe o all'istanza. Sono simili alle funzioni definite all'interno della classe, 
    ma non accedono né modificano gli attributi della classe o dell'istanza. 
    Sono utilizzati quando un metodo appartiene logicamente a una classe ma non dipende né dalle istanze né dalla classe stessa.
    '''
    
    @staticmethod
    def get_iscritti_by_codins(codins):
        cnx = DBConnect.get_connection()
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

        cursor.close() # chiudo il cursore
        cnx.close() # chiudo la connessione e la restituisco alla pool
        print('Query avvenuta con successo. Restituisco la connessione alla pool.')
        return studenti
    
    @staticmethod
    def get_studente_by_matricola(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM studente
                WHERE matricola = (%s);
                """
        cursor.execute(query, (matricola,))
        result = cursor.fetchone()

        studente = Studente(matricola=result['matricola'], cognome=result['cognome'], nome=result['nome'], CDS=result['CDS'])

        cursor.close() # chiudo il cursore
        cnx.close() # chiudo la connessione e la restituisco alla pool
        print('Query avvenuta con successo. Restituisco la connessione alla pool.')
        return studente

    @staticmethod
    def iscrivi_studente(matricola, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO iscrizione 
                (matricola, codins)
                VALUES (%s, %s);
                """
        cursor.execute(query, (matricola, codins))
        cnx.commit()

        cursor.close() # chiudo il cursore
        cnx.close() # chiudo la connessione e la restituisco alla pool
        print('Query avvenuta con successo. Restituisco la connessione alla pool.')
        return True 

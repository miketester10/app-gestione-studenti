# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import DBConnect
from model.corso import Corso

class corso_DAO:
    '''
    @staticmethod: 
    Questo decoratore definisce un metodo statico. I metodi statici non ricevono automaticamente alcun argomento 
    relativo alla classe o all'istanza. Sono simili alle funzioni definite all'interno della classe, 
    ma non accedono né modificano gli attributi della classe o dell'istanza. 
    Sono utilizzati quando un metodo appartiene logicamente a una classe ma non dipende né dalle istanze né dalla classe stessa.
    '''

    @staticmethod
    def get_corsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM corso;
                """
        cursor.execute(query,)
        result = cursor.fetchall()

        corsi = [Corso(codins=row['codins'], crediti=row['crediti'], nome=row['nome'], pd=row['pd']) for row in result]

        cursor.close() # chiudo il cursore
        cnx.close() # chiudo la connessione e la restituisco alla pool
        print('Query avvenuta con successo. Restituisco la connessione alla pool.')
        return corsi
    
    @staticmethod
    def get_corsi_by_matricola(matricola):
        cnx = DBConnect.get_connection()
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

        cursor.close() # chiudo il cursore
        cnx.close() # chiudo la connessione e la restituisco alla pool
        print('Query avvenuta con successo. Restituisco la connessione alla pool.')
        return corsi
    

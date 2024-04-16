import mysql.connector
from mysql.connector import errorcode

class DBConnect:
    '''
    @classmethod: 
    Questo decoratore definisce un metodo di classe. Il primo argomento di un metodo di classe è sempre la classe stessa, 
    convenzionalmente denominata cls. I metodi di classe possono accedere e modificare l'attributo di classe, 
    ma non possono accedere agli attributi specifici dell'istanza (cioè gli attributi non statici). 
    I metodi di classe sono spesso usati come costruttori alternativi o per operazioni che coinvolgono la classe stessa anziché le istanze.
    '''

    _cnxPool = None

    def __init__(self):
        raise RuntimeError('Non creare istanze. Usare il metodo di classe get_connection() !!')
    
    @classmethod
    def get_connection(cls, pool_name='my_pool', size=4) -> mysql.connector.pooling.MySQLConnectionPool:
        
        if cls._cnxPool is None:
            print('Provo a connettermi a MySQL..')
            try:
                cls._cnxPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size = size,
                    pool_name = pool_name,
                    option_files = './database/connector.cnf'
                )
                print('Conessione a MySQL avvenuta con successo. Richiedo una connessione alla pool..')
                return cls._cnxPool.get_connection() # questo get_connection() non è il metodo della classe DBConnect ma il metodo della classe MySQLConnectionPool per ottenere la connessione
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                    return None
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    return None
                else:
                    print(err)
                    return None
        else:
            print('Richiedo una connessione alla pool..')
            return cls._cnxPool.get_connection()




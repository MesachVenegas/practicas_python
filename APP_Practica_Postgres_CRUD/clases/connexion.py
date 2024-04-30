from psycopg2 import pool
from clases.looger_info import log
import sys


class Connexion:
    """Connexion:

    Se encarga de establecer el pool de conexiones y su interacion con el mismo, al igual de la administración de los slots del pool para su uso.
    """
    _DB = 'DB_practicas'
    _HOST = 'localhost'
    _DB_PORT = '5432'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    _MIN = 1
    _MAX = 5
    _pool = None

    # Creación del Pool de Conexiones.
    @classmethod
    def mk_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                cls._MIN,
                cls._MAX,
                user = cls._USER,
                password = cls._PASSWORD,
                host = cls._HOST,
                port = cls._DB_PORT,
                dbname = cls._DB
                )
                log.info(f'Conexión Exitosa: {cls._pool}')
                return cls._pool
            except Exception as ex:
                log.critical(f"{ex}")
                sys.exit()
        else:
            return cls._pool

    # Crea y devuelve un objeto de tipo conexión
    @classmethod
    def pool_conn(cls):
        connection = Connexion.mk_pool().getconn()
        return connection

    # Liberacion de la Conexión para su retorno al Pool de Conexiones.
    @classmethod
    def pool_drop(cls, conexion):
        drop = Connexion.mk_pool().putconn(conexion)
        log.info(f'{cls._pool} Liberado')
        return drop

    # Cierra el Pool de conexiones.
    @classmethod
    def pool_close(cls):
        Connexion.mk_pool().closeall()
        log.info(f'{cls._pool} cerrado')

if __name__ == '__main__':
    Connexion.mk_pool()
    conexion = Connexion.pool_conn()
    Connexion.pool_drop(conexion)
    Connexion.pool_close()
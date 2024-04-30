from clases.connexion import Connexion
from clases.looger_info import log
from clases.cls_users import Users
import sys


class PoolCursor:
    """Pool Cursor

    Handrel para el pool, creación del cursor y automatización de apertura y cierre en las
    transacciones con la base de datos.
    """

    def __init__(self):
        self._connexion = None
        self._cursor = None

    def __enter__(self):
        self._connexion = Connexion.pool_conn()
        self._cursor = self._connexion.cursor()
        return self._cursor

    def __exit__(self, excep_type, excep_val, details):
        if excep_val:
            self._connexion.rollback()
            log.error(f"{excep_type}:{excep_val}")
            log.warning("Se realizo un RollBack..")
            sys.exit()
        else:
            self._connexion.commit()
            log.info("Transaccion finalizada...")
        # cierro el cursor y devuelvo la conexión al pool de conexiones.
        self._cursor.close()
        Connexion.pool_drop(self._connexion)


if __name__ == "__main__":
    with PoolCursor() as cursor:
        cursor.execute("SELECT * FROM usuarios_db ORDER BY id_key ASC")
        data = cursor.fetchall()
        for x in data:
            user = Users(x[0], x[1], x[2], x[3])
            print(user)

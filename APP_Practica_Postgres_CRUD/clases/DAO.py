from hashlib import md5
from clases.cls_users import Users
from clases.ConnHandler import PoolCursor
from clases.looger_info import log


class DAOAPP:
    """Data Access Object

    Controlador para el acceso a los datos de la base de datos.
    CRUD - Create, Read, Update, Delete
    """

    _CREATE = 'INSERT INTO usuarios_db(user_name, email, password) VALUES(%s, %s, %s)'
    _READ = 'SELECT * FROM usuarios_db ORDER BY id_key ASC'
    _UPDATE = 'UPDATE usuarios_db SET user_name= %s, email= %s, password= %s WHERE id_key= %s'
    _DELETE = 'DELETE FROM usuarios_db WHERE id_key= %s'
    # Encryptado del password ante del ingreso a la db.
    @classmethod
    def encryp_pass(cls, password):
        """Recibe la propiedad con el password del usuario y lo convierte a un objeto encryptado con md5

        Args:
            password (property): Propiedad del usuario con el valor del password

        Returns:
            str: pass encrypted con md5
        ejemplo: 'asdasda' -> 'efasdsad23sad'
        """
        __cod_pass = md5(password.encode())
        __cod_pass =  __cod_pass.hexdigest()
        return __cod_pass

    # Tratamiento de los datos y ingreso de los mismos a la base de datos.
    @classmethod
    def mk_reg(cls, user: Users):
        """Recibe el objeto de clase usuario y obtiene los atributos necesarios para la creación
        de un registro valido para la base de datos.

        Args:
            user (Users): objeto con los datos a ingresar

        Returns:
            int: Devuelve el numero de lineas afectadas
        """
        user.password = cls.encryp_pass(user.password)
        data = (user.user_name, user.email, user.password)
        with PoolCursor() as cursor:
            cursor.execute(cls._CREATE, data)
            log.info(user)
            return cursor.rowcount

    # Consulta de registros en la base de datos.
    @classmethod
    def show_reg(cls):
        """Realiza una consulta SQL en la base datos.

        Returns:
            [list]: Lista de objetos de clase User
        """
        with PoolCursor() as cursor:
            cursor.execute(cls._READ)
            registros = cursor.fetchall()
            usuarios = []
            for user in registros:
                usuario = Users(user[0], user[1], user[3], user[2])
                usuarios.append(usuario)
            return usuarios

    # Actualización de datos de un registro en la base de datos.
    @classmethod
    def updt_reg(cls, user: Users, upt_type = 'all'):
        """Actualiza los datos de un registro

        Args:
            user (Users): Objeto con las propiedades a modificar del registro.
            upt_type (str, optional): [all, username, password, email] según lo que se desee modificar. Defaults to 'all'.
        """
        match upt_type:
            case 'all':
                with PoolCursor() as cursor:
                    user.password = cls.encryp_pass(user.password)
                    data = (user.user_name, user.email, user.password, user.id_key)
                    cursor.execute(cls._UPDATE, data)
                    log.info(f'registro(s) actualizado(s): {cursor.rowcount}')
                    return f'Se actualizo el usuario: {user}'
            case 'username':
                with PoolCursor() as cursor:
                    data = (user.user_name,user.id_key)
                    cursor.execute('UPDATE usuarios_db SET user_name = %s WHERE id_key = %s', data)
                    log.info(f'registro(s) actualizado(s): {cursor.rowcount}')
                    return f'User name actualizado: {user.user_name}'
            case 'email':
                with PoolCursor() as cursor:
                    data = (user.email, user.id_key)
                    cursor.execute('UPDATE usuarios_db SET email = %s WHERE id_key = %s', data)
                    log.info('Registro(s) actualizado(s): {cursor.rowcount}')
                    return f'Email actualizado: {user.email}'
            case 'password':
                with PoolCursor() as cursor:
                    user.password = cls.encryp_pass(user.password)
                    data = (user.password, user.id_key)
                    cursor.execute('UPDATE usuarios_db SET password = %s WHERE id_key = %s', data)
                    log.info(f'Registro(s) actualizado(s): {cursor.rowcount}')
                    return f'Se actualizo el password correctamente'
            case _:
                raise ValueError(f"'{upt_type}' no esta definido.")

    # Método para la eliminación de registros en la bd.
    @classmethod
    def del_reg(cls, user: Users):
        """Elimina un registro de la base de datos.

        Args:
            user (Users): Elemento usuario donde se extrae la propiedad identificadora para la eliminación del registro.

        Returns:
            [int]: Numero de registros eliminados
        """
        with PoolCursor() as cursor:
            data = (user.id_key,)
            cursor.execute(cls._DELETE, data)
            log.info('Registro eliminado...')
            return cursor.rowcount


if __name__ == '__main__':
    user_in = Users(user_name='root',email='root@app.com', password='rootadmin', id_key=2)
    users = DAOAPP.show_reg()
    for user in users:
        print(f'{user}')

    info = DAOAPP.updt_reg(user_in, upt_type='password')
    print(info)
    users = DAOAPP.show_reg()
    for user in users:
        print(f'{user}')
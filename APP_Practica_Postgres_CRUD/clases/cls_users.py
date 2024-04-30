class Users:
    """Users
    Clase encargada de generar los objetos de tipo usuario para su manipulación.
    """
    def __init__(self, id_key: int = None, user_name: str = None, password: str = None, email: str = None):
        self._id_key = id_key
        self._user_name = user_name
        self._password = password
        self._email = email


    def __str__(self):
        return f'''Key:{self._id_key}
    UserName:{self._user_name}
    Email:{self._email}
    Password:{self._password}
    '''

    @property
    def id_key(self):
        return self._id_key

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @id_key.setter
    def id_key(self, new_key):
        self._id_key = new_key

    @user_name.setter
    def user_name(self, new_name):
        self._user_name = new_name

    @password.setter
    def password(self, new_pass):
        self._password = new_pass

    @email.setter
    def email(self, new_email):
        self._email = new_email


if __name__ == '__main__':
    mes = Users(user_name='Mesach', password='bwsk6372', email='mesach.venegas@hotmail.com')
    print(mes)

    mes.password = 'mesach'
    print(mes.password)
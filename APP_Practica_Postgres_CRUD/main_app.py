from clases.cls_users import Users
from clases.looger_info import log
from clases.DAO import DAOAPP
import sys



def main_menu(menu:str = 'main'):
    """Despliegue de menu principal o secundario.

    Args:
        menu (str, optional): Muestra en pantalla un estilo de menu determinado por el parámetro indicado [main/ update]. Defaults to 'main'.
    """
    match menu:
        case 'main':
            home_menu = [
                'Crear Usuario',
                'Ver usuarios',
                'Actualizar usuario',
                'Eliminar Usuario',
                'Salir'
            ]
            num = 1
            print('\n\t\tHola Bienvenido al registro.')
            print('Elije una de las opciones(1-5):\n')
            for opt in home_menu:
                print(f'\t\t{num}.- {opt}')
                num += 1
        case 'update':
            upd_menu = [
                'Actualizar todos los datos.',
                'Actualizar Username.',
                'Actualizar email.',
                'Actualizar password',
                'Salir'
            ]
            print('\t\t\nActualizar usuario elija una de las opciones:(1-5) \n')
            num = 1
            for opt in upd_menu:
                print(f'\t\t{num}.- {opt}')
                num += 1
        case _:
            log.error(f"<'{menu}'> no esta definido.")
            sys.exit()

def opt_val(ask: str):
    """Toma la entrada del usuario y determina si es un dígito para su conversion a tipo 
    entero.

    Args:
        ask (str): Entrada a validar para su conversion a entero

    Returns:
        [int]: entrada convertida en valor numérico tipo 'int'
    """
    while not ask.isdigit():
        log.warning(f"valor de tipo:{type(ask)} invalido, ingresa valores numéricos <class 'int'>")
        ask = input()
    else:
        ask = int(ask)
        return ask

def fmt_pass(pwd: str):
    """Validación del password ingresado, para que cumpla con los requerimientos predefinidos

    Args:
        pwd (str): password ingresada por el usuario

    Returns:
        str: password que cumple con el formato predefinido.
    """
    invalid_words = ['/', '>', '<', '=', '\\', '&', '%', '#', '(', ')', ' ']
    pwd_ok = ''
    while not pwd_ok:
        for char in pwd:
            if not char in invalid_words and len(pwd) >= 6:
                pwd_ok = pwd
                break
            else:
                if len(pwd) < 6:
                    log.warning('La contraseña debe ser de una longitud minima de 6 caracteres.')
                for char in pwd:
                    if char in invalid_words:
                        log.warning(f'La contraseña no debe incluir caracteres especiales {invalid_words} ni espacios en blanco.')
                pwd = input('Ingresa una contraseña valida: ')
    return pwd_ok

if __name__ == '__main__':

    flag = False

    while not flag:
        main_menu()
        ask = opt_val(input('\nElija una opción: '))
        #Crear usuario.
        if ask == 1:
            name = input('\nIngresa el nombre de usuario: ')
            email = input('Ingresa el correo electrónico: ')
            wordkey = fmt_pass(input('Ingresa el password: '))
            user = Users(user_name=name, email=email, password=wordkey)
            row = DAOAPP.mk_reg(user)
            print(f'Se ingreso correctamente: {row} registro')

        # Consulta de usuarios.
        elif ask == 2:
            data = DAOAPP.show_reg()
            for user in data:
                print(f'''\n ID: {user.id_key}   User Name: {user.user_name}     Email: {user.email} ''')

        # Actualizar usuario.
        elif ask == 3:
            main_menu('update')
            cont = 1
            upt = 0
            while not flag:
                if cont == 1:
                    opt = input('\nQue desea actualizar (1-5): ')
                elif upt > 1:
                    opt = input('\nDesea modificar algo mas(1-5): ')
                else:
                    opt = input('Ingresa un opción valida(1-5): ')

                match opt:
                    case '1':
                        id_key = input('Cual es el id a modificar: ')
                        name = input('Ingrese el nuevo user name: ')
                        email = input('Ingresa el nuevo email: ')
                        keyword = fmt_pass(input('Ingresa la nueva contraseña: '))
                        new_data = Users(id_key, name, keyword, email)
                        row = DAOAPP.updt_reg(new_data)
                        print(f'Se actualizo {row} usuario correctamente.')
                        log.info(f'Se modifico {row} registro en base de datos.')
                        upt += 1
                    case '2':
                        id_key = input('Ingresa el id a modificar: ')
                        name = input('Ingresa el nuevo user name: ')
                        new_data = Users(user_name=name, id_key=id_key)
                        row = DAOAPP.updt_reg(new_data ,upt_type='username')
                        print('Se actualizo el username correctamente')
                        log.info(f'Se modifico {row} atributo del id:{id_key}')
                        upt += 1
                    case '3':
                        id_key = input('Ingresa el id a modificar: ')
                        email = input('Ingresa el nuevo email: ')
                        new_data = Users(email=email, id_key=id_key)
                        row = DAOAPP.updt_reg(new_data, upt_type='email')
                        print('Correo electrónico actualizado.')
                        log.info(f'Se modifico {row} atributo en el id:{id_key}')
                        upt += 1
                    case '4':
                        id_key = input('Ingresa el id a modificar: ')
                        password = input('Ingresa el nuevo password: ')
                        new_data = Users(password=password, id_key= id_key)
                        row = DAOAPP.updt_reg(new_data, upt_type='password')
                        print('Password actualizado correctamente.')
                        log.info(f'Se modifico {row} atributo en el id:{id_key}.')
                        upt += 1
                    case '5':
                        break
                    case _:
                        cont += 1
                        log.warning('Opción invalida')
        # Eliminar usuario.
        elif ask == 4:
            id_key = input('Ingresa el id a eliminar: ')
            data = Users(id_key=id_key)
            row = DAOAPP.del_reg(data)
            print(f'Se elimino a el usuario.')
            log.info(f'Se elimino {row} registro con el id:{id_key}')

        # salir
        elif ask == 5:
            flag = True
            print('\n\t\t Muchas gracias, nos vemos! :)')
            sys.exit()
        else:
            log.warning(f"{ask} no es una opción valida elija una opción entre 1 - 5")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo o no existe.")
    except PermissionError:
        print("Se encontró el archivo pero no tienes los permisos requeridos")


if __name__ == '__main__':
    main()
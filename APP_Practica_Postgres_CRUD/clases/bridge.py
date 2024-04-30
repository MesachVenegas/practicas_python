import sys
import os


# Obtengo el nombre del directorio desde donde esta este archivo.
current = os.path.dirname(os.path.realpath(__file__))

# Obtengo el nombre de la carpeta padre de el archivo
parent = os.path.dirname(current)

# Agrego la carpeta al path para su acceso.
sys.path.append(parent)

if __name__ == '__main__':
    print(current)
    print(parent)
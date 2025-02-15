import os

data_dir = os.path.dirname(os.path.realpath('__file__'))

def abrir_fichero():
    nombre=str(input("Ingrese el nombre del archivo (debe estar en la misma carpeta que los .py): "))
    try:
        fichero=open(data_dir+"/"+nombre,"r")
        return fichero
    except FileNotFoundError:
        return 0

def reconocedor ():
    archivo=abrir_fichero()
    if archivo==0:
        print("Archivo no encontrado. No se puede ejecutar")
    else:
        for linea in archivo:
            return None
    
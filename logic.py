import os

data_dir = os.path.dirname(os.path.realpath(__file__))

def abrir_fichero():
    nombre=str(input("Ingrese el nombre del archivo (debe estar en la misma carpeta que los .py): "))
    ruta = os.path.join(data_dir,nombre)
    print("Buscando archivo en: ".format(ruta) )
    try:
        with open(ruta, "r") as fichero:
            return fichero.readlines()
    except FileNotFoundError:
        print("No se encuentra el archivo")
        return None

class RobotRecognizer:
    
    def __init__(self, lines):
        self.lines = lines
        self.variables = set()
        self.procedures = {}
        self.errors = []
        self.call_stack = []
        pass

    def separador (self,line):
        caracteres = ""
        lista_caracteres = []
        for char in line:
            if char.isalpha() or char.isdigit() or char in "#_":
                caracteres += char
            
            else: 
                if caracteres:
                    lista_caracteres.append(caracteres)
                    caracteres = ""
                if char.strip():
                    lista_caracteres.append(char)
        if caracteres:
            lista_caracteres.append(caracteres)
        return lista_caracteres
    def parse(self):
        if not self.lines:
            return
        for line in self.lines:
            caracteres= self.separador(line.strip())
            print ("Caracteres en linea: {}".format(caracteres))
        
def reconocedor ():
    archivo=abrir_fichero()
    if archivo is None:
        print("Archivo no encontrado. No se puede ejecutar")
        return
    else:
        robot = RobotRecognizer(archivo)
        
        robot.parse()
    
import os

data_dir = os.path.dirname(os.path.realpath(__file__))

def abrir_fichero():
    nombre=str(input("Ingrese el nombre del archivo (debe estar en la misma carpeta que los .py): "))
    ruta = os.path.join(data_dir,nombre)
    print("Buscando archivo en: ".format(ruta))
    try:
        with open(ruta, "r") as fichero:
            return [line.strip() for line in fichero.readlines()]
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
        self.instructions = ["move","turn","face","goto","put","pick","jump","if","while","proc"]
        

    def separador (self,line):
        caracteres = ""
        lista_caracteres = []
        print(f"Tipo de 'line': {type(line)}")
        for char in line:
            if char == "|" or char in "[]":
                continue
            if char.isalpha() or char.isdigit() or char in "#_":
                caracteres += char
            
            else: 
                if caracteres:
                    lista_caracteres.append(str(caracteres))
                    caracteres = ""
                if char.strip():
                    lista_caracteres.append(char)
        if caracteres:
            lista_caracteres.append(caracteres)
        return lista_caracteres
    
    def parse(self):
        if not self.lines:
            return False
        for line in self.lines:
            caracteres= self.separador(line.strip())
            self.procesador(caracteres)
        return len(self.errors) == 0

    def procesador(self, caracteres):
        if not caracteres:
            return
        comandos = caracteres[0]
        if comandos in self.instructions:
            self.validador(comandos, caracteres[1:])
        else: 
            self.errors.append("Comando desconocido: {}".format(comandos))
    
    def procesos(self, caracteres):
        if len(caracteres) < 3 or caracteres[1] in self.instructions:
            self.errors.append("Error en procesos")
            return
        nom_proc = caracteres[1]
        self.procedures[nom_proc] = [] 
           
    def validador(self, comandos, args):
        comandos = comandos.lower()
        if comandos == "goto":
            if len(args) == 3 and args[1] == "with:" and args[0].isdigit() and args[2].isdigit():
                return
            else:
                self.errors.append("Error en el comando goto")
        elif comandos == "move":
            if not args[0].isdigit():
                self.errors.append("Error en el comando move")
        elif comandos == "turn":
            if args[0] not in ["#left","#right","#around"]:
                self.errors.append("Error en el comando turn")
        elif comandos == "face":
            if args[0] not in ["#north","#south","#west","#east"]:
                self.errors.append("Error en el comando face")
        elif comandos == "put":
            if len(args) == 3 and args[1] == "ofType:" and args[0].isdigit() and args[2] in ["#balloons", "#chips"]:
                return
            else:
                self.errors.append("Error en el comando put")
        elif comandos == "pick":
            if len(args) == 3 and args[1] == "ofType:" and args[0].isdigit() and args[2] in ["#balloons", "#chips"]:
                return
            else:
                self.errors.append("Error en el comando pick")
        elif comandos == "jump":
            if len(args) == 3 and (args[1] == "toThe:" or args[1] == "inDir:") and args[0].isdigit() and args[2] in ["#front", "#right","#left","#back","#north", "#south","#west","#east"]:
                return
            else:
                self.errors.append("Error en el comando jump")
                
    def errores(self):
        if self.errors:
            print("Errores encontrados en el lenguaje: ")
            for errores in self.errors:
                print(errores)
        else: 
            print("El lenguaje es correcto.")
        
def reconocedor ():
    archivo=abrir_fichero()
    if archivo is None:
        print("Archivo no encontrado. No se puede ejecutar")
        return
    else:
        robot = RobotRecognizer(archivo)
        
        resultado = robot.parse()
        robot.errores()
        return resultado


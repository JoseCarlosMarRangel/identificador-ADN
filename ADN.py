#import csv  # Libreria necesaria para los csv

class ADN(object):
    def __init__(self, sD=[], sA="", r=[0], p={}):
        # contiene [AAGT, AGAT]
        self.strDeDatos = sD
        # contiene "AGSAGSGATSGATAGST"
        self.strDeADN = sA
        # contiene las repeticiones de cada strdeDato en el str [1, 5, 9]
        self.repetDatos = r
        # contiene las personas en un diccionario {alice: [1, 5, 9]
        #                                           bob : [2, 3, 4]}
        self.personas = p

    # Por cada string de strDeDatos analiza toda la string del txt
    # si encuentra una igual aumenta su repeticion en 1
    # si no se encuentra el indice se agrega
    def llenarRepetDatos(self):
        indice = 0
        for s in self.strDeDatos: # [AAGT, AAAT] AAGT -> AAAT
            for i in range(len(self.strDeADN) - len(s)):
                # genera los bloquecitos; s es la cabecera del csv
                #if self.strDeADN[i:i+len(s)] == s:
                if s in self.strDeADN:
                    # checa si la lista esta vacia
                    # ej. [0] -> indice 1 => error 
                    # para solucionar ese error se pone append
                    # [0].append(1) => [0, 1] indice 1 == 1
                    #  [AAGT, AGAT] se necesita una lista de tamaño 2
                    # Si AAGT se encuentra en el string 5 veces y AGAT 4
                    # repetDatos => [5, 4]
                    if len(self.repetDatos)-1 < indice:
                        self.repetDatos.append(1)
                    else:
                        self.repetDatos[indice] += 1
                        
                    self.strDeADN = self.strDeADN.replace(s , "", 1)
            indice += 1
        pass

    def menu(self):
        while True:
            print("MENU")
            print("1 - Cargar CSV")
            print("2 - cargar TXT")
            print("3 - Resultados")
            print("4 - Salir")
            opcion = input()
            if opcion == '1':
                print("Introduce la ruta al CSV")
                RutaCSV = input() # para probar codigo rapidamente usar la linea de abajo
                #RutaCSV = "adn.csv"
                # Carga el csv completo
                with open(RutaCSV, "r") as archivoCSV:
                    # EL [:-1] del final indica que no se tomara el salto de linea "\n"
                    strDeCSV = archivoCSV.readline()[:-1]
                    # Se cargan todas las lineas siguientes
                    strDePersonas = archivoCSV.readlines()
                # separar con split y se toman todos menos el primero
                self.strDeDatos = strDeCSV.split(sep=",")[1:]
                # Obtiene las personas
                for line in strDePersonas:
                    # elimina el \n al final de cada linea
                    line = line.strip()
                    # crea el diccionario de cada persona y convierte los numeros en enteros
                    self.personas[line.split(sep=',')[0]] = list(map(int, line.split(sep=',')[1:]))
            elif opcion == '2':
                print("Introduce la ruta al TXT")
                txt = input() # para probar codigo rapidamente usar la linea de abajo
                #txt = "no_match.txt"
                with open(txt, 'r') as archivoTXT:
                    self.strDeADN = archivoTXT.readline()[:-1]
            elif opcion == '3':
                if self.strDeDatos == [] or self.personas == {}:
                    print("Llena todos los datos primero")
                    pass
                else:
                    self.llenarRepetDatos()
                    #print(self.repetDatos)
                    existePersona = False
                    for nombre, listaDatos in self.personas.items():
                        if listaDatos == self.repetDatos:
                            print("El ADN es de la persona ", nombre)
                            existePersona = True
                            break
                    if existePersona == False:
                        print("No existe persona con ese ADN")
                    self.repetDatos = [0]
            elif opcion == '4':
                break
            else:
                print("Error, opcion incorrecta")

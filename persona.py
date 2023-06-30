class Persona():
    tipoDoc =""
    documento =0
    nombre =""
    apellido =""
    peso =0.0
    estatura  = 0.0 
    edad = 0
    sexo =""
    
    
    
    def __init__(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo):
        self.tipoDoc= tipoDoc
        self.documento= documento
        self.nombre= nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo
    
    def getnombre(self):
        return self.nombre    
    def setNombre(self,nombre):
        self.nombre=nombre
    def getApellido(self):
        return self.apellido   
    def setApellido(self):  
        self.apellido

    def getpeso(self):
        return self.peso  
    def setpeso(self):
        self.peso
    def getEstatura(self):
        return self.estatura 
    def setEstatatura(self):
        self.estatura
    def getEdad(self):
        return self.edad
    def setEdad(self):
        self.edad
    def getSexo(self):
        return self.sexo
    def setSexo(self):
        self.sexo





    def pedirDatos(self):
        self.tipoDoc= input("Ingrese el tipo de documento \n ")
        self.documento= int (input("ingrese el documento \n"))
        self.nombre= input("Ingrese el nombre \n ")
        self.apellido=input("Ingrese el Apellido \n ")
        self.peso=float (input("Ingrese el peso \n "))
        self.estatura=float (input("Ingrese la estatura \n "))
        self.edad=int(input("Ingrese la edad \n "))
        self.sexo=input("Ingrese el tipo de sexo \n ")
        
        
        
    def mostrarPersonal (self):
        print(f"EL usuario {self.nombre} {self.apellido} con tipo de documento {self.tipoDoc} con numero {self.documento}")
        print(f"Con edad {self.edad} Tiene un peso de {self.peso} y mide {self.estatura}")
        
    def calcularmc(self):
        pesoActual=self.peso /(self.estatura ** 2)
        return pesoActual
        if pesoActual < 20 :
            print ("el peso esta por debajo")
        elif pesoActual > 20 and pesoActual < 26 :
            print ("el peso es ideal")
        elif pesoActual> 25 :
            print("sobrepeso")
        return pesoActual 
    
    def mayorEdad(self,edad):
        if edad < 18 :
            print("Eres menor de edad")
        elif edad   > 17 :
            print("eres mayor de edad")
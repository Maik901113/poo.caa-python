from persona import Persona


class Empleados(Persona):
    cargo = ""
    valorHora = 0
    horasTrabajadas = 0 
    departamento=""
    honorarios = 0
        
    
    
    def __init__(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo,
                 cargo,valorHora,horasTrabajadas,departamento ):
        super().__init__(tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo)
        self.cargo= cargo
        self.valorHora= valorHora
        self.horasTrabajadas= horasTrabajadas
        self.departamento= departamento
    
    def pedirDatos(self):
        self.cargo = input("Ingrese el cargo del empleado \n")
        self.valorHora = int(input("Ingrese el valor de la hora \n") )
        self.horasTrabajadas = int(input("Ingrese la horas trabajadas \n"))
        self.departamento = input("ingrese el departamento \n")
    def calcularHonorarios(self):
        honorarios=(self.valorHora * self.horasTrabajadas) *(1-0.00966)  
        return honorarios
    def imprimirEmpleado(self):
        print(f"EL empleado con  {self.tipoDoc} con numero {self.documento} y nombre  {self.nombre}  {self.apellido} ")
        print(f"Con el cargo  {self.cargo} trabajo {self.horasTrabajadas} horas, cada hora con valor de  {self.valorHora} y un total de honorarios a pagar de {self.calcularHonorarios()}")
        
        


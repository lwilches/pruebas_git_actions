from datetime import datetime
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: float
    apellido: str

    def dar_nombre(self):
        return self.nombre

    def dar_edad(self):
        return self.edad

    def asignar_edad(self , edad:float ):
        self.edad = edad
    
    def asignar_nombre(self , nombre :str ):
        self.nombre = nombre
    
    def asignar_apellido(self, apellido :str):
        self.apellido = apellido

    def dar_nombre_completo(self):
        return self.nombre +  ' ' +   self.apellido 
        
    def calcular_anio_nacimiento(self, ya_cumplio_aaaa:bool):
        aaaa_actual = datetime.now().year
        return (aaaa_actual - self.edad) if ya_cumplio_aaaa else (aaaa_actual - self.edad + 1)




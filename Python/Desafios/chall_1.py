class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f'feliz cumpleaños #{self.edad} {self.nombre}')
        
    

persona1 = Persona("paco", 30)
persona1.cumplir_anios
print(persona1)



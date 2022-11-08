class Vehiculo:
    def __init__(self):
        self.color= "Verde"
        self.ruedas= 4
        self.puertas= 2

class coche (Vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad= 120
        self.cilindrada=1.3


d = coche()

print ("Color es:", d.color)
print ("Tiene", d.ruedas, "ruedas")
print ("Tiene", d.puertas, "puertas")
print ("Es de una velocidad de:", d.velocidad)
print ("Tiene una cilindrada de:", d.cilindrada)
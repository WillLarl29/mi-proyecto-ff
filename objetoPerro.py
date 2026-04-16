class Perro:
    def __init__(self, nombre, edad, raza):
        self.name = nombre
        self.age = edad
        self.race = raza
    
    def cumple(self):
        self.age += 1

    def getName(self):
        return self.name
    
miperro = Perro("Bobby", 5, "Poodle")
print(miperro.name)  # Output: Bobby
print(miperro.age)   # Output: 5
print(miperro.getName())  # Output: Bobby
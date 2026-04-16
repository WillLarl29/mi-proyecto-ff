class Usuario:
    def __init__(self):
        self.name = "Nariyoshi"
        self.apellido = "Miyagi"
        self.age = 30
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 1000.0
        self.saldo_pagar = 0.0

    def hacer_ccompra(self, monto):
        self.saldo_pagar += monto

## Creación de instancias
miyagi = Usuario()
daniel = Usuario()

# Accedemos a los atributos de las instancias
print(miyagi.name)  # Output: Nariyoshi
print(daniel.name)  # Output: Nariyoshi 

## Ahora establezcamos valores distintos para nuestras instancias:
daniel.name = "Daniel"
daniel.apellido = "Larson"
print(daniel.name)  # Output: Daniel

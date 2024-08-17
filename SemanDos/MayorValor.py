class MayorValor:

    def __init__(self):
        self.valorUno = float(input("Ingrese el primer valor: "))
        self.valorDos = float(input("Ingrese el segundo valor: "))

    def mayorValor(self):
        if self.valorUno > self.valorDos:
            return self.valorUno
        else:
            return self.valorDos
        
mayor = MayorValor()

print("El mayor valor es:", mayor.mayorValor())
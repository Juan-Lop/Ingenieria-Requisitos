class Liros:
    def __init__(self):
        self.litrosProducidos = float(input("Ingrese la cantidad de litros producidos: "))
        self.precioGalonLeche = float(input("Ingrese el precio por galón: "))
        self.litrosPorGalon = 3.785  

    def calcularPago(self):
        galones_producidos = self.litrosProducidos / self.litrosPorGalon
        pago = galones_producidos * self.litrosPorGalon
        return pago


produccion = Liros()



print("El pago total es:", produccion.calcularPago())
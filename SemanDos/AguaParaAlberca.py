class AguaParaAlberca:

    def __init__(self):
        self.largo = float(input("Ingrese el largo de la alberca: "))
        self.ancho = float(input("Ingrese el ancho de la alberca: "))
        self.prondidad = float(input("Ingrese la profundidad de la alberca: "))
        self.costoMetroCubico = float(input("Ingrese el costo por metro cubico: "))

    def calcularElVolumen(self):
        volumen = self.largo * self.ancho * self.prondidad
        return volumen
    
    def calcularElCosto(self):
        volumen = self.calcularElVolumen()
        costo = volumen * self.costoMetroCubico
        return costo

aguaCostoTotal = AguaParaAlberca()

print("El costo total de llenar la alberca es:", aguaCostoTotal.calcularElCosto())
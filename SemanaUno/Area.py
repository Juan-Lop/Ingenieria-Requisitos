class Area:
    def __init__(self):
        self.ladoA = float(input("Ingrese el valor del lado A: "))
        self.ladoB = float(input("Ingrese el valor del lado B: "))
        self.ladoC = float(input("Ingrese el valor del lado C: "))

    def calcularArea(self):
        areaTriangulo = (self.ladoA - self.ladoC) * self.ladoB / 2

  # Calculamos el área del rectángulo
        AreaRectangulo = self.ladoA * self.ladoB

  # Calculamos el área total
        AreaTotal = areaTriangulo + AreaRectangulo

        return AreaTotal
    

area = Area()

print("El área total es:", area.calcularArea())
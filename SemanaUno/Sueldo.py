class Sueldo:
    def __init__(self):
        self.horastrabajadas = float(input("Ingrese el número de horas trabajadas: "))
        self.pagoHora = float(input("Ingrese el pago por hora: "))

    def calcularSueldo(self):
        sueldo = self.horastrabajadas * self.pagoHora
        return sueldo

sueldo = Sueldo()

print("Su sueldo es: ", sueldo.calcularSueldo())
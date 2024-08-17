class Tela:

    def __init__(self):
        self.metros = float(input("Ingrese la cantidad de tela en metros: "))

    def calcularTela(self):
        tela = self.metros / 0.0254

        return tela
    

tela = Tela()

print(" La cantidad de tela que se quiere pedir en pulgadas es:", tela.calcularTela())
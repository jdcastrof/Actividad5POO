import math

class CalculosNumericos:
    @staticmethod
    def calcularLogaritmoNeperiano(valor):
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.log(valor)
            print("Resultado = " + str(resultado))
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError:
            print("El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calcularRaizCuadrada(valor):
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.sqrt(valor)
            print("Resultado = " + str(resultado))
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError:
            print("El valor debe ser numérico para calcular la raíz cuadrada")

    @staticmethod
    def main():
        try:
            valor = float(input("Valor numérico = "))
        except ValueError:
            print("El valor debe ser numérico")
            return
        CalculosNumericos.calcularLogaritmoNeperiano(valor)
        CalculosNumericos.calcularRaizCuadrada(valor)

if __name__ == "__main__":
    CalculosNumericos.main()

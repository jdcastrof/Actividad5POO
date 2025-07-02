class PruebaExcepciones:
    @staticmethod
    def main(args=[]):
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0
            print("Después de la división")
        except ArithmeticError as e:
            print("División por cero")
        finally:
            print("Ingresando al primer finally")

        try:
            print("Ingresando al segundo try")
            objeto = None
            objeto.toString()
            print("Imprimiendo objeto")
        except ArithmeticError as e:
            print("División por cero")
        except Exception as e:
            print("Ocurrió una excepción")
        finally:
            print("Ingresando al segundo finally")


if __name__ == "__main__":
    PruebaExcepciones.main()
    

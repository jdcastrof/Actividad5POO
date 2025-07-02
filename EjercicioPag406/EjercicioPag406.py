class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def imprimir(self):
        print("Nombre del vendedor = " + str(self.nombre))
        print("Apellidos del vendedor = " + str(self.apellidos))
        print("Edad del vendedor = " + str(self.edad))

    def verificarEdad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    @staticmethod
    def main():
        nombre = input("Nombre del vendedor = ")
        apellidos = input("Apellidos del vendedor = ")
        vendedor = Vendedor(nombre, apellidos)
        edad = int(input("Edad del vendedor = "))
        vendedor.verificarEdad(edad)
        vendedor.imprimir()

if __name__ == "__main__":
    Vendedor.main()

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombreEquipo, universidad, lenguajeProgramacion):
        self.nombreEquipo = nombreEquipo
        self.universidad = universidad
        self.lenguajeProgramacion = lenguajeProgramacion
        self.programadores = [None] * 3
        self.tamanoEquipo = 0

    def estaLleno(self):
        return self.tamanoEquipo == len(self.programadores)

    def anadir(self, programador):
        if self.estaLleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamanoEquipo] = programador
        self.tamanoEquipo += 1

    @staticmethod
    def validarCampo(campo):
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

    @staticmethod
    def main():
        nombre = input("Nombre del equipo = ")
        universidad = input("Universidad = ")
        lenguaje = input("Lenguaje de programación = ")
        equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
        print("Datos de los integrantes del equipo")
        for i in range(3):
            nombreProgramador = input("Nombre del integrante = ")
            EquipoMaratonProgramacion.validarCampo(nombreProgramador)
            apellidosProgramador = input("Apellidos del integrante = ")
            EquipoMaratonProgramacion.validarCampo(apellidosProgramador)
            programador = Programador(nombreProgramador, apellidosProgramador)
            equipo.anadir(programador)

if __name__ == "__main__":
    EquipoMaratonProgramacion.main()

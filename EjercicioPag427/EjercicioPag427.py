class LeerArchivo:
    @staticmethod
    def main():
        nombreArchivo = "C:/prueba.txt"
        try:
            with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
                linea = archivo.readline()
                while linea:
                    print(linea.rstrip('\n'))
                    linea = archivo.readline()
        except IOError:
            print("No se pudo leer el archivo.")

if __name__ == "__main__":
    LeerArchivo.main()

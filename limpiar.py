import sys

DEFAULT_FILE = "palabrascomun.txt"

def clasificar(archivo):
    """
    Limpia la lista de palabras del archivo dejando solo la primera palabra por linea.
    """
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except IOError:
        print(f"Error al abrir el archivo {archivo}.")
        return

    palabras = []
    for linea in lineas:
        palabra = linea.split(' ')[0].strip()
        if palabra:
            palabras.append(palabra)
    
    nombre_archivo = archivo.split('.')[0] + "_limpio.txt"
    try:
        with open(nombre_archivo, 'w') as f:
            f.write("\n".join(palabras))
    except IOError:
        print(f"Error al escribir el archivo {nombre_archivo}.")
        return
    print(f"Archivo limpio creado: {nombre_archivo}")



def main():
    if len(sys.argv) != 2:
        print("Usage: python limpiar.py <archivo>")
        return
    if len(sys.argv) == 2:
        clasificar(sys.argv[1])


if __name__ == "__main__":
    main()
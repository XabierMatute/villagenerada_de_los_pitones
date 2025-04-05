import sys

DEFAULT_FILE = "palabrascomun.txt"

# tesis (Sustantivo)
# testificar (Verbo)
# texto (Sustantivo)
# tía (Sustantivo)
# tiburón (Sustantivo)
# tío (Sustantivo)
# tirar (Verbo)
# título (Sustantivo)
# tocar (Verbo)
# toma de decisiones (Sustantivo)
# tomar (Verbo)
# torcer (Verbo)
# toro (Sustantivo)
# tortuga (Sustantivo)
# trabajar [funcionar] (Verbo)
# trabajar (Verbo)
# traducción (Sustantivo)
# traducir (Verbo)
# tragar (Verbo)
# traición (Sustantivo)
# traje (Sustantivo)
# tranquilizar (Verbo)
# transcribir (Verbo)
# transcripción (Sustantivo)
# transcurrir (Verbo)
# transferir (Verbo)
# transformar (Verbo)
# transición (Sustantivo)
# transitar (Verbo)
# tranvía (Sustantivo)
# trasladar (Verbo)
# trasquilar (Verbo)
# trastear (Verbo)
# trastonar (Verbo)
# tratar (Verbo)
# tren (Sustantivo)
# trepar (Verbo)
# trineo (Sustantivo)
# tripular (Verbo)
# triturar (Verbo)
# trono (Sustantivo)
# tropezar (Verbo)
# trueque (Sustantivo)
# U
# ultimátum (Sustantivo)
# ultra (Sustantivo)
# un cuarto (Adjetivo)
# una cuarta parte (Adjetivo)
# unánime (Adjetivo)
# universo (Sustantivo)
# urgente (Adjetivo)
# usar (Verbo)
# V
# vaca (Sustantivo)
# vagar (Verbo)
# vagón (Sustantivo)
# vale (Interjección)
# valer (Verbo)
# valor (económico) (Sustantivo)
# valor (Sustantivo)
# vapor (de agua) (Sustantivo)
# vaquera (Sustantivo)
# vaquero (Sustantivo)
# variar (Verbo)
# velar (Verbo)
# vencer (Verbo)
# vender (Verbo)
# venerar (Verbo)
# venir (Verbo)
# ventilar (Verbo)
# verano (Sustantivo)
# verde (Adjetivo)
# verificar (Verbo)
# verter (Verbo)
# vestir (Verbo)
# viajar (Verbo)
# víbora (Sustantivo)
# vibrar (Verbo)
# viernes (Sustantivo)
# violar (Verbo)
# violencia (Sustantivo)
# violeta (Adjetivo)
# violín (Sustantivo)
# virar (Verbo)
# virtud (Sustantivo)
# visitar (Verbo)
# vocabulario (Sustantivo)
# volar (Verbo)
# volcar (Verbo)
# volver (Verbo)
# X
# xilófono (Sustantivo)
# Y
# yacer (Verbo)
# yerno (Sustantivo)
# Z
# zambomba (Sustantivo)
# zampar (Verbo)
# zapatera (Sustantivo)
# zapatero (Sustantivo)
# zapatilla (Sustantivo)
# zapato (Sustantivo)
# zarpar (Verbo)
# zorra (Sustantivo)
# zorro (Sustantivo)
# zurcir (Verbo)

def clasificar(archivo):
    """
    Clasifica las palabras en un archivo de texto y las guarda en archivos separados.
    """
    try:
        with open(archivo, 'r') as f:
            palabras = f.read().splitlines()
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return

    sustantivos = []
    verbos = []
    adjetivos = []
    interjecciones = []
    adverbios = []
    preposiciones = []
    conjunciones = []
    otras = []

    print(f"Clasificando palabras del archivo {archivo}...")
    for palabra in palabras:
        print(f"Clasificando: {palabra}")
        tipodepalabra = palabra.split('(')[-1].split(')')[0].strip()
        print(f"Tipo de palabra: {tipodepalabra}")
        if "Sustantivo" in tipodepalabra:
            sustantivos.append(palabra)
        elif "Verbo" in tipodepalabra:
            verbos.append(palabra)
        elif "Adjetivo" in tipodepalabra:
            adjetivos.append(palabra)
        elif "Interjección" in tipodepalabra:
            interjecciones.append(palabra)
        elif "Adverbio" in tipodepalabra:
            adverbios.append(palabra)
        elif "Preposición" in tipodepalabra:
            preposiciones.append(palabra)
        elif "Conjunción" in tipodepalabra:
            conjunciones.append(palabra)
        else:
            otras.append(palabra)
    print("Clasificación completa.")
    try:
        with open("sustantivos.txt", 'w') as f:
            f.write("\n".join(sustantivos))
        with open("verbos.txt", 'w') as f:
            f.write("\n".join(verbos))
        with open("adjetivos.txt", 'w') as f:
            f.write("\n".join(adjetivos))
        with open("interjecciones.txt", 'w') as f:
            f.write("\n".join(interjecciones))
        with open("adverbios.txt", 'w') as f:
            f.write("\n".join(adverbios))
        with open("preposiciones.txt", 'w') as f:
            f.write("\n".join(preposiciones))
        with open("conjunciones.txt", 'w') as f:
            f.write("\n".join(conjunciones))
        with open("otras.txt", 'w') as f:
            f.write("\n".join(otras))
    except IOError:
        print("Error al escribir los archivos de salida.")
        return

def main():
    if len(sys.argv) > 2:
        print("Usage: python clasificar.py <archivo>")
        return
    if len(sys.argv) == 2:
        clasificar(sys.argv[1])
    else:
        clasificar(DEFAULT_FILE)

if __name__ == "__main__":
    main()
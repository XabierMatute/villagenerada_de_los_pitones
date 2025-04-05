import random

import requests
import re

import spacy

nlp = spacy.load("es_core_news_sm")

# import wikipediaapi

# wiki_wiki = wikipediaapi.Wikipedia(user_agent='generador de nombres')


def obtener_genero(palabra):
    """
    Devuelve el género de una palabra en español. consultando Wikipedia (wikidictionary).

    """
    doc = nlp(palabra)
    genero = doc[0].morph
    return genero


def generar_añadido(sustantivos):
    sustantivo_aleatorio = random.choice(sustantivos)
    # sustantivo_aleatorio = "gallinas"
    genero = obtener_genero(sustantivo_aleatorio)
    # genero : spacy.tokens.morphanalysis.MorphAnalysis = obtener_genero(sustantivo_aleatorio)
    añadido = sustantivo_aleatorio
    print(f"El género de {sustantivo_aleatorio} es {genero}.")
    
    if "Gender=Masc" in genero and "Number=Sing" in genero:
        añadido = "del " + sustantivo_aleatorio
    elif "Gender=Fem" in genero and "Number=Sing" in genero:
        añadido = "de la " + sustantivo_aleatorio
    elif "Gender=Masc" in genero and "Number=Plur" in genero:
        añadido = "de los " + sustantivo_aleatorio
    elif "Gender=Fem" in genero and "Number=Plur" in genero:
        añadido = "de las " + sustantivo_aleatorio
    else:
        añadido = "de " + sustantivo_aleatorio

    return añadido

# Ejemplo de uso
# print(obtener_genero("gallina"))  # Devuelve: "masculino"

def main():
    sustantivos = open("sustantivos_limpio.txt", 'r').read().splitlines()
    adjetivos = open("adjetivos_limpio.txt", 'r').read().splitlines()
    sustantivo_aleatorio = random.choice(sustantivos)
    # sustantivo_aleatorio = "gallina"
    genero = obtener_genero(sustantivo_aleatorio)
    print(f"{sustantivo_aleatorio} es un sustantivo {genero}.")
    adjetivo_aleatorio = random.choice(adjetivos)
    while (obtener_genero(adjetivo_aleatorio) != genero):
        print(f"{adjetivo_aleatorio} no es un adjetivo {genero}.")
        print(f"{sustantivo_aleatorio}{adjetivo_aleatorio} no queda bien.")
        adjetivo_aleatorio = random.choice(adjetivos)
    añadido = generar_añadido(sustantivos)

    print(f"{sustantivo_aleatorio}{adjetivo_aleatorio} {añadido}")

if __name__ == "__main__":
    main()
    
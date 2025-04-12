import sys
import spacy
nlp = spacy.load("es_core_news_sm")
with open('es.subject.txt', 'r') as file:
    
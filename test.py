import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("gato")
print(doc[0].morph)  # Género=Masc|Número=Sing
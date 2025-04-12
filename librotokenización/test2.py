import sys
import spacy
nlp = spacy.load("es_core_news_sm")

def is_simple_shape(token):
    for c in token.shape_:
        if c.lower() != 'x':
            return False
    return True

with open('es.subject.txt', 'r') as file:
    # nouns_file = open('nouns.txt', 'w')
    # nms_file = open('nms.txt', 'w')
    # nfs_file = open('nfs.txt', 'w')
    # nmp_file = open('nmp.txt', 'w')
    # nfp_file = open('nfp.txt', 'w')

    # adjectives_file = open('adjectives.txt', 'w')
    # ams_file = open('ams.txt', 'w')
    # afs_file = open('afs.txt', 'w')
    # amp_file = open('amp.txt', 'w')
    # afp_file = open('afp.txt', 'w')

    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            doc = nlp(line)
            for token in doc:
                if True:
                # if token.pos_ == "VERB":
                    print(f"Token: {token.text}")
                    print(f"  Lemma: {token.lemma_}")
                    print(f"  POS: {token.pos_}")
                    print(f"  Tag: {token.tag_}")
                    print(f"  Dep: {token.dep_}")
                    print(f"  Shape: {token.shape_}")
                    print(f"  Is alpha: {token.is_alpha}")
                    print(f"  Is stop: {token.is_stop}")
                    print(f"  Morph: {token.morph}")
                    print(f"  Parent: {token.head.text}")

                # check if simple shape (only contains x)
                if not is_simple_shape(token):
                    continue

                # if token.pos_ == "ADJ":
                #     print(f"  Is adjective: {token.text}")
                #     adjectives_file.write(token.text + '\n')

                #     if "Gender=Masc" in token.morph and "Number=Sing" in token.morph:
                #         print(f"  Is masculine singular: {token.text}")
                #         ams_file.write(token.text + '\n')
                #     if "Gender=Fem" in token.morph and "Number=Sing" in token.morph:
                #         print(f"  Is feminine singular: {token.text}")
                #         afs_file.write(token.text + '\n')
                #     if "Gender=Masc" in token.morph and "Number=Plur" in token.morph:
                #         print(f"  Is masculine plural: {token.text}")
                #         amp_file.write(token.text + '\n')
                #     if "Gender=Fem" in token.morph and "Number=Plur" in token.morph:
                #         print(f"  Is feminine plural: {token.text}")
                #         afp_file.write(token.text + '\n')
                    

                # if token.pos_ == "NOUN":
                #     print(f"  Is noun: {token.text}")
                #     nouns_file.write(token.text + '\n')
                #     # mirar si es masculino singular
                #     print(token.morph)
                #     # if token.morph = Gender=Masc|Number=Sing
                #     if "Gender=Masc" in token.morph and "Number=Sing" in token.morph:
                #         print(f"  Is masculine singular: {token.text}")
                #         nms_file.write(token.text + '\n')
                #     if "Gender=Fem" in token.morph and "Number=Sing" in token.morph:
                #         print(f"  Is feminine singular: {token.text}")
                #         nfs_file.write(token.text + '\n')
                #     if "Gender=Masc" in token.morph and "Number=Plur" in token.morph:
                #         print(f"  Is masculine plural: {token.text}")
                #         nmp_file.write(token.text + '\n')
                #     if "Gender=Fem" in token.morph and "Number=Plur" in token.morph:
                #         print(f"  Is feminine plural: {token.text}")
                #         nfp_file.write(token.text + '\n')
import sys
import spacy
import os

DIRECTORIO_PALABRAS = "palabras"
EXTENSION_PALABRAS = ".palabras"
if not os.path.exists(DIRECTORIO_PALABRAS):
    os.makedirs(DIRECTORIO_PALABRAS)

DIRECTORIO_NOMBRES = os.path.join(DIRECTORIO_PALABRAS, "nombres")
if not os.path.exists(DIRECTORIO_NOMBRES):
    os.makedirs(DIRECTORIO_NOMBRES)

DIRECTORIO_ADJETIVOS = os.path.join(DIRECTORIO_PALABRAS, "adjetivos")
if not os.path.exists(DIRECTORIO_ADJETIVOS):
    os.makedirs(DIRECTORIO_ADJETIVOS)

DIRECTORIO_VERBOS = os.path.join(DIRECTORIO_PALABRAS, "verbos")
if not os.path.exists(DIRECTORIO_VERBOS):
    os.makedirs(DIRECTORIO_VERBOS)

MASCULINO_SINGULAR = "masculino_singular"
MASCULINO_PLURAL = "masculino_plural"
FEMENINO_SINGULAR = "femenino_singular"
FEMENINO_PLURAL = "femenino_plural"

IMPERATIVO_SINGULAR = "imperativo_singular"
IMPERATIVO_PLURAL = "imperativo_plural"

NMS_FILE = os.path.join(DIRECTORIO_NOMBRES, f"{MASCULINO_SINGULAR}{EXTENSION_PALABRAS}")
NFS_FILE = os.path.join(DIRECTORIO_NOMBRES, f"{FEMENINO_SINGULAR}{EXTENSION_PALABRAS}")
NMP_FILE = os.path.join(DIRECTORIO_NOMBRES, f"{MASCULINO_PLURAL}{EXTENSION_PALABRAS}")
NFP_FILE = os.path.join(DIRECTORIO_NOMBRES, f"{FEMENINO_PLURAL}{EXTENSION_PALABRAS}")
AMS_FILE = os.path.join(DIRECTORIO_ADJETIVOS, f"{MASCULINO_SINGULAR}{EXTENSION_PALABRAS}")
AFS_FILE = os.path.join(DIRECTORIO_ADJETIVOS, f"{FEMENINO_SINGULAR}{EXTENSION_PALABRAS}")
AMP_FILE = os.path.join(DIRECTORIO_ADJETIVOS, f"{MASCULINO_PLURAL}{EXTENSION_PALABRAS}")
AFP_FILE = os.path.join(DIRECTORIO_ADJETIVOS, f"{FEMENINO_PLURAL}{EXTENSION_PALABRAS}")
IS_FILE = os.path.join(DIRECTORIO_VERBOS, f"{IMPERATIVO_SINGULAR}{EXTENSION_PALABRAS}")
IP_FILE = os.path.join(DIRECTORIO_VERBOS, f"{IMPERATIVO_PLURAL}{EXTENSION_PALABRAS}")

def is_simple_shape(token):
    if not token.shape_ or len(token.shape_) < 2:
        return False
    for c in token.shape_:
        if c.lower() != 'x':
            return False
    return True


def extract_words(input_file):
    nlp = spacy.load("es_core_news_sm")

    with open(input_file, 'r') as file:
        nms_file = open(NMS_FILE, 'a', encoding='utf-8')
        nfs_file = open(NFS_FILE, 'a', encoding='utf-8')
        nmp_file = open(NMP_FILE, 'a', encoding='utf-8')
        nfp_file = open(NFP_FILE, 'a', encoding='utf-8')
        ams_file = open(AMS_FILE, 'a', encoding='utf-8')
        afs_file = open(AFS_FILE, 'a', encoding='utf-8')
        amp_file = open(AMP_FILE, 'a', encoding='utf-8')
        afp_file = open(AFP_FILE, 'a', encoding='utf-8')

        is_file = open(IS_FILE, 'a', encoding='utf-8')
        ip_file = open(IP_FILE, 'a', encoding='utf-8')

        text = file.read()
        lines = [text[i:i+nlp.max_length] for i in range(0, len(text), nlp.max_length)]
        for line in lines:
            line = line.strip()
            if line:
                doc = nlp(line)
                for token in doc:
                    if not is_simple_shape(token):
                        continue
                    if token.pos_ == "ADJ":
                        if "Gender=Masc" in token.morph and "Number=Sing" in token.morph:
                            ams_file.write(token.text + '\n')
                        if "Gender=Fem" in token.morph and "Number=Sing" in token.morph:
                            afs_file.write(token.text + '\n')
                        if "Gender=Masc" in token.morph and "Number=Plur" in token.morph:
                            amp_file.write(token.text + '\n')
                        if "Gender=Fem" in token.morph and "Number=Plur" in token.morph:
                            afp_file.write(token.text + '\n')
                        

                    if token.pos_ == "NOUN":
                        if "Gender=Masc" in token.morph and "Number=Sing" in token.morph:
                            nms_file.write(token.text + '\n')
                        if "Gender=Fem" in token.morph and "Number=Sing" in token.morph:
                            nfs_file.write(token.text + '\n')
                        if "Gender=Masc" in token.morph and "Number=Plur" in token.morph:
                            nmp_file.write(token.text + '\n')
                        if "Gender=Fem" in token.morph and "Number=Plur" in token.morph:
                            nfp_file.write(token.text + '\n')

                    if token.pos_ == "VERB":
                        if "Mood=Imp" in token.morph and "Person=2" in token.morph:
                            print(token.text, token.morph)

                            if "Number=Sing" in token.morph:
                                is_file.write(token.text + '\n')
                            if "Number=Plur" in token.morph:
                                ip_file.write(token.text + '\n')
        nms_file.close()
        nfs_file.close()
        nmp_file.close()
        nfp_file.close()
        ams_file.close()
        afs_file.close()
        amp_file.close()
        afp_file.close()

        is_file.close()
        ip_file.close()

        print(f"Words extracted to {DIRECTORIO_PALABRAS} directory.")
        print("Extraction complete.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_words.py <input_file>")
        return
    for input_file in sys.argv[1:]:
        print(f"Processing file: {input_file}")
        if not input_file.endswith('.libro'):
            print(f"Skipping non-libro file: {input_file}")
            continue
        if not os.path.isfile(input_file):
            print(f"File not found: {input_file}")
            continue
        print(f"Extracting words from {input_file}...")
        extract_words(input_file)
        print(f"Finished processing {input_file}")

if __name__ == "__main__":
    main()
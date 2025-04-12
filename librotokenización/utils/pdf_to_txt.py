import os
import sys
import pypdf

def pdf_to_txt(input_file):
    reader = pypdf.PdfReader(input_file)

    output_file = input_file.replace('.pdf', '.txt')
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                txt_file.write(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python TXT_to_csv.py <input_file>")
        return
    pdf_to_txt(sys.argv[1])

if __name__ == "__main__":
    main()
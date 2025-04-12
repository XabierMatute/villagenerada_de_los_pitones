import sys
import os

def txt_to_libro(input_file):

    output_file = input_file.replace('.txt', '.libro')
    print(f"Converting {input_file} to {output_file}")
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()
        with open(output_file, 'w', encoding='utf-8') as libro_file:
            libro_file.write(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python TXT_to_csv.py <input_files>")
        return
    for input_file in sys.argv[1:]:
        print(f"Processing file: {input_file}")
        if not input_file.endswith('.txt'):
            print(f"Skipping non-txt file: {input_file}")
            continue
        if not os.path.isfile(input_file):
            print(f"File not found: {input_file}")
            continue
        txt_to_libro(input_file)

if __name__ == "__main__":
    main()
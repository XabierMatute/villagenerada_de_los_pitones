# importing all the required modules
import pypdf

# creating a pdf reader object
reader = pypdf.PdfReader('VE_jdr.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())

for i in range(len(reader.pages)):
    # print the text of the page
    print(reader.pages[i].extract_text())
    # print the text of the page
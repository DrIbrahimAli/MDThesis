import sys
from accents import latexAccents

def utf_to_latex(text):
    for search, replace in latexAccents:
         text = text.replace(search, replace)
    return text

tex = open(sys.argv[1],'r')



for line in  tex:
    print(utf_to_latex(line))


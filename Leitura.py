#Primeira implemetação para código de leitura dos documentos .doc/.docx
import pandas as pd
import numpy as np
import os
from docx import Document
from doc2docx import convert
import PyPDF2


arquivo_pdf = open("exemplo.pdf", "rb")
pdf = PyPDF2.PdfReader(arquivo_pdf)

forms = pdf.get_fields()

pagina = pdf.pages[0]

conteudo_pagina = pagina.extract_text()

imagem = pagina.images[0]

checkbox = pdf.get_form_text_fields()

print(forms)
#print(conteudo_pagina)
#print(checkbox)
#print(imagem)

#convert("exemplo.doc")
#doc = "exemplo.docx"
#documento = Document(doc)
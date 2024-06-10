#Primeira implemetação para código de leitura dos documentos .doc/.docx
import pandas as pd
import numpy as np
import os
from docx import Document


caminho = "Exemplos"
arquivos = os.listdir(caminho)
print(arquivos)


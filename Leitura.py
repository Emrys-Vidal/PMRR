#Primeira implemetação para código de leitura dos documentos .doc/.docx
import pandas as pd
import numpy as np
#import os ñ tem q baixar, ja vem integrado
from docx import Document


caminho = "Exemplos"
arquivos = os.listdir(caminho)
print(arquivos)

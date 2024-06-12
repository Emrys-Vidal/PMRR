import PyPDF2
from PyPDF2 import PdfReader

path = r"C:/Users/bruno/OneDrive/BRUNO/PMRR-sao_jose_&_floripa/GitHub/PMRR/exemplo.pdf"

with open(path, "rb") as file:
        if not PdfReader.get_fields:
            print("00000")
        else:
              print("OPA")

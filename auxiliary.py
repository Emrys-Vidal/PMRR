from PyPDF2 import PdfReader

path = r"C:/Users/bruno/OneDrive/BRUNO/PMRR-sao_jose_&_floripa/GitHub/PMRR/exemplo.pdf"
pdf = open(path, "rb")

info = PdfReader.metadata

def extract_form_values(path):
    with open(path, "rb") as file:
        if not PdfReader.get_fields:
            return 0
        
        form_fields = PdfReader(path).get_fields
        field_values = {}

        for field_name, field_data in form_fields:
            field_values[field_name] = field_data

        return field_values

form_values = extract_form_values(path)

for field, value in form_values.items():
    print(f"Field Name: {field}, Value: {value}")
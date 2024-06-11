
"""rom docx import Document
import pandas as pd
import glob
# Load the DOC file
#doc2doc
doc = Document(r"D:\Users\guima\OneDrive\UFSC\Programação\PMRR\Exemplos\P 001 BURACO NA VIA PÚBLICA  02 01 2023.docx")

# Lists to hold the extracted data
form_data = []
table_data = []

# Extract text from paragraphs (assuming form fields labeled with colons)
for para in doc.paragraphs:
    if ':' in para.text:  # Assuming form fields are labeled with colons
        key, value = para.text.split(':', 1)
        form_data.append([key.strip(), value.strip()])

# Extract text from tables
for table in doc.tables:
    for rows in table.rows:
        rows_data = [cell.text.strip() for cell in rows.cells]
        table_data.append(rows_data)

# Convert form data to DataFrame
df_form = pd.DataFrame(form_data, columns=['Field', 'Value'])

# Convert table data to DataFrame (if all tables have the same structure)
df_table = pd.DataFrame(table_data)

# Save form data and table data to separate sheets in an Excel file
with pd.ExcelWriter('output_1.xlsx') as writer:
    df_form.to_excel(writer, sheet_name='Form Data', index=False)
    df_table.to_excel(writer, sheet_name='Table Data', index=False)"""


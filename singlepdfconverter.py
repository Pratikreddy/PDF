#Pratik

import pdfplumber
import pandas as pd

pdf_path = r'C:\Users\pratiks\Desktop\sorting pdfs\structured\ISN DXP OSHA Form 300 - No Names.pdf'
output_excel = r'C:\Users\pratiks\Desktop\sorting pdfs\structured\ISN DXP OSHA Form 300 - No Names.xlsx'

table_settings = {
    'vertical_strategy': 'lines',
    'horizontal_strategy': 'lines',
    'intersection_tolerance': 5,
    'snap_tolerance': 5,
}

data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table(table_settings=table_settings)
        if table is not None:
            data.extend(table[1:])

df = pd.DataFrame(data[1:], columns=data[0])
df.to_excel(output_excel, index=False)
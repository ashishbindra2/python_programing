from docxtpl import DocxTemplate
from datetime import datetime
import os 

import pathlib

doc_path = r"./templates/invoice_template_test.docx"

file_name= pathlib.Path(doc_path).stem
output_path = f"files/invoices/generate_{file_name}.docx"

# items = {
#     "description" : ["as","As","sd"],
#     "qty": [1,2,3],
#     "price": [12,12,23],
#     "vat_per": [33,44,12],
#     "priseExVat": [1223,12323,34545]
# } 

items = [
    {"description": "as", "qty": 1, "price": 12, "vat_per": 33, "priseExVat": 1223},
    {"description": "As", "qty": 2, "price": 12, "vat_per": 44, "priseExVat": 12323},
    {"description": "sd", "qty": 3, "price": 23, "vat_per": 12, "priseExVat": 34545}
]

today_date: str = datetime.now().strftime("%d-%b-%Y")

context = {
    "clientName": "Asshish",
    "invoiceNumber": 124354,
    "ProjectName": "testing",
    "items": items,
    "date": today_date,
    "dueDate": "12/12/23",
    "clientAddress": "client address",
    "vatNo": "123"
}
try:
    doc = DocxTemplate(doc_path)
        
    doc.render(context)

    doc.save(output_path)
    
    print(f"File sucessfully save in {output_path} location")
except PermissionError as e:
    print("File is already open",e)
except NameError as ne:
    print("File path is wrong",ne)
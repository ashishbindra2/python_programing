import os
from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

template_name = "invoice_template_test.docx"

def invoice_gen(doc_name, invoice_num=1) -> None:
    """
    function to generate invoice
    :param html_name:
    :return:
    """
    file_name, _ = os.path.splitext(doc_name)

    print(f"{file_name:=}")
    template = Environment(loader=FileSystemLoader("./templates")).get_template(doc_name)
    today_date: str = datetime.now().strftime("%d-%b-%Y")
    
    try:
        for invoice in range(1, invoice_num):
            print(invoice)

            context = {
                "clientName": "Asshish",
                "invoiceNumber": 124354,
                "ProjectName": "testing",
                "date": today_date,
                "dueDate": "12/12/23",
                "clientAddress": "client address",
                "vatNo": "123"
            }
            
            report_text = template.render(context)
            os.makedirs("files/invoices", exist_ok=True)

            file_path = f"./files/invoices/invoice_{file_name}_123"
            
            with open(f"{file_path}.html", mode="w", encoding="UTF-8") as f:
                f.write(report_text)

            # pdf_converter(f"{file_path}.html", f"{file_path}.pdf")
    except Exception as e:
        print("Error", e)

    print("Invoice generated successfully!!!!")
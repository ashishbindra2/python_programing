import jinja2

from report import make_report
from invite import invite_people
from invoices import invoice_gen

html = "sales_report_template.html"


def main() -> None:
    while True:
        print("Press the following numer to generate the result: ")
        print("Press 1: For Generate a report ")
        print("Press 2: For Generate marriage  Invitation  ")
        print("Press 3: For Generate Invoices!!! ",end="")

        try:
            value = int(input())
            if value == 1:
                make_report(html)
                break
            elif value == 2:
                invite_people(template_name="invite_template.txt")
                break
            elif value == 3:
                invoice_gen("invoic_template_1.html")
                break
            else:
                print("Please choose 1 or 2 and 3 numbers aare allowed")

        except ValueError:
            print("Only Integer value allowed 1 or 2")

        except jinja2.exceptions.TemplateNotFound:
            print("file not found!!")


if __name__ == "__main__":
    main()

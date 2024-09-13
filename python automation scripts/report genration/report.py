import os
import io
import base64
import jinja2

from random import randint
from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

from matplotlib import pyplot as plt
from html_to_pdf import pdf_converter


def populate_dummy_data():
    # create data for a report
    sales_table = []

    for i in range(1, 11):
        #     print(i)
        cost_pr_unit = randint(1, 15)
        num_units = randint(100, 1500)

        sales_table.append({
            "sNo": i,
            "name": "Item " + str(i),
            "cPu": cost_pr_unit,
            "nUnits": num_units,
            "revenue": cost_pr_unit * num_units
        })

    top_items = [x["name"] for x in sorted(sales_table, key=lambda x: x["revenue"], reverse=True)][:3]
    return sales_table, top_items


def evaluate_graph(sales_table: list[dict[str, str | int]]) -> str:
    #  Generate sales bae chart image
    plot_img_bytes = io.BytesIO()
    fig, ax = plt.subplots()

    ax.bar([x["name"] for x in sales_table], [x["revenue"] for x in sales_table])

    fig.tight_layout()
    fig.savefig(plot_img_bytes, format="jpg")
    plot_img_bytes.seek(0)

    plot_img_str: str = base64.b64encode(plot_img_bytes.read()).decode()
    return plot_img_str


def make_report(html_filename="sales_report_template.html"):

    file_name, _ = os.path.splitext(html_filename)

    # Create jinja template object from file
    template = Environment(
        loader=FileSystemLoader("./templates"),
    ).get_template(html_filename)

    today_date: str = datetime.now().strftime("%d-%b-%Y")
    sales_table, top_items = populate_dummy_data()

    # plot_img_str = evaluate_graph(sales_table)

    # Create logo image from file
    with open("./static/img/bird-logo.avif", "rb") as f:
        logo_img = base64.b64encode(f.read()).decode()

    # Data for injecting into jinja2 template
    context = {
        "reportDtStr": today_date,
        "salesTblRows": sales_table,
        "topItemsRows": top_items,
        # "salesBarChartImg": plot_img_str,
        "logoImg": logo_img
    }

    # Rander the data in jinja
    report_text = template.render(context)

    # os.mkdir("files/reports")
    os.makedirs("files/reports", exist_ok=True)

    file_path = f"./files/reports/report_{file_name}"
    with open(f"{file_path}.html", mode="w") as f:
        f.write(report_text)

    pdf_converter(f"{file_path}.html", f"{file_path}.pdf")

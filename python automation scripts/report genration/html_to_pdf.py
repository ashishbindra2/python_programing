from playwright.sync_api import sync_playwright
import pathlib
import os


# convert a relative path of a local file into an absolute path
# you can skip this if you have an absolute path like "C:\\Users\\James\\reports\\sales_report.html"

def pdf_converter(html_path: str, pdf_path: str):
    file_path = os.path.abspath(html_path)

    # derive the URL path of a local file to be opened in browser
    file_url = pathlib.Path(file_path).as_uri()

    # print the file as a pdf from Chromium browser using playwright
    with sync_playwright() as p:
        # create a browser instance
        browser = p.chromium.launch()

        # open a new tab in the browser
        page = browser.new_page()

        # goto the URL of the HTML page
        page.goto(file_url)

        # change css media type to screen
        page.emulate_media(media="screen")

        # print the html page as pdf in the browser
        page.pdf(path=pdf_path, format="A4",
                 landscape=True, margin={"top": "2cm"})

        # close the browser
        browser.close()
        print("Html to pdf conversion successfully!!!")

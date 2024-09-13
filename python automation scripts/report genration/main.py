from report import make_report
from invite import invite_people

html = "sales_report_template.html"


def main() -> None:
    while True:
        print("Press the following numer to generate the result: ")
        print("Press 1: For Generate a report ")
        print("Press 2: For Generate marriage  Invitation  ")

        try:
            value = int(input())
            if value == 1:
                make_report(html)
                break
            elif value == 2:
                invite_people(template_name="invite_template.txt")
                break
            else:
                print("Please choose 1 or 2 numer only")

        except ValueError:
            print("Only Integer value allowed 1 or 2")


if __name__ == "__main__":
    main()

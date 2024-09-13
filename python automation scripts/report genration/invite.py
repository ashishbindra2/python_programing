import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

guests_set = ("Sreshti", "Akash", "Duby", "Vivek", "Vishal", "Maajid", "jitesh", "Priyanka", "Amrinder")


def invite_people(venu_detail=None, template_name: str = "invite_template.txt",
                  guests: list | tuple = guests_set):
    if venu_detail is None:
        venu_detail = {}
    os.makedirs("files/invites", exist_ok=True)

    # Create jinja template object from file
    template = Environment(
        loader=FileSystemLoader("./templates")
    ).get_template(template_name)

    #  Data for injecting into jinja2 template

    template_context = {
        "recipientName": "",
        "eventDtStr": venu_detail.get("date", "Sunday, October 27, 2024"),
        "venuStr": venu_detail.get("palace", "Patiala"),
        "senderName": venu_detail.get("sender_name", "Ashish Bindra"),
        "contactInfo": venu_detail.get("contact", 9041213440),
        "time": venu_detail.get("time", "10: 30 A.M")
    }

    for guest in guests:
        template_context["recipientName"] = guest

        # rander data in jinja template
        invite_text = template.render(template_context)

        # make a file
        with open(f"./files/invites/{guest}.txt", "w") as f:
            f.write(invite_text)

    print("Invitation Generate Successfully!!")
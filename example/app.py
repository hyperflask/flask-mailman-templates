from flask import Flask
from flask_mailman import Mail
from flask_mailman_templates import MailTemplates, send_mail


app = Flask(__name__)
app.config["MAIL_BACKEND"] = "console"
mail = Mail(app)
mail_templates = MailTemplates(app)


@app.route("/")
def index():
    send_mail("hello.txt", "hello@localhost")
    send_mail("hello_html.html", "hello@localhost")
    return "Emails sent !"
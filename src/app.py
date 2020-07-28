from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import os
import dotenv

app = Flask(__name__)


def mailConfig():
    app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
    app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
    app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
    app.config['MAIL_USE_TLS'] = bool(os.getenv("MAIL_USE_TLS"))
    app.config['MAIL_USE_SSL'] = bool(os.getenv("MAIL_USE_SSL"))


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "GET":
        print(os.getenv("SERVER"))
        return render_template("send.html")

    if request.method == "POST":

        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        msg = request.form['message']

        mail = Message(sender=sender,
                       body=msg,
                       subject=subject,
                       recipients=[recipient])

        mailer.send(mail)

        return redirect("/send")


if __name__ == "__main__":
    mailConfig()
    mailer = Mail(app)
    app.run('0.0.0.0', port=5000)

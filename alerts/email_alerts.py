import smtplib
from email.message import EmailMessage

def send_alert(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "alerts@cloudoptimizer.com"
    msg['To'] = to_email

    with smtplib.SMTP('smtp.yourprovider.com', 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)

if __name__ == "__main__":
    send_alert(
        "Cloud Cost Alert",
        "Your cloud spend exceeded the defined threshold.",
        "client@example.com"
    )

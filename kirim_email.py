import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

SMTP_SERVER = "localhost"
SMTP_PORT = 1025
EMAIL_PENGIRIM = "praktikum@local.test"
EMAIL_PENERIMA = "mahasiswa@local.test"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "laporan_praktikum.txt")

msg = MIMEMultipart()
msg["From"] = EMAIL_PENGIRIM
msg["To"] = EMAIL_PENERIMA
msg["Subject"] = "Praktikum SMTP dengan MailHog"

msg.attach(MIMEText("Email ini dikirim melalui MailHog.", "plain"))

with open(file_path, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition",
                "attachment; filename=laporan_praktikum.txt")

msg.attach(part)

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.send_message(msg)
server.quit()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# KONFIGURASI SMTP (MAILHOG)
SMTP_SERVER = "localhost"
SMTP_PORT = 1025

def kirim_email():
    try:
  
        # INPUT DINAMIS
        email_pengirim = input("Masukkan email pengirim: ")
        email_penerima = input("Masukkan email penerima: ")
        subject = input("Masukkan subjek email: ")
        body = input("Masukkan isi email: ")

        # MEMBUAT OBJEK EMAIL
        msg = MIMEMultipart()
        msg["From"] = email_pengirim
        msg["To"] = email_penerima
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # MULTIPLE LAMPIRAN
        while True:
            file_path = input("Masukkan path lampiran (Enter jika selesai): ")

            if file_path == "":
                break

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

            with open(file_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())

            encoders.encode_base64(part)
            filename = os.path.basename(file_path)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}"
            )

            msg.attach(part)

        # KIRIM EMAIL
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.send_message(msg)
        server.quit()

        print("Email berhasil dikirim melalui MailHog.")

    except FileNotFoundError as e:
        print(f"Error File: {e}")

    except ConnectionRefusedError:
        print("Error: Server SMTP tidak dapat dihubungi. Pastikan MailHog aktif.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    kirim_email()

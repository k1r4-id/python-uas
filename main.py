import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(from_email, from_password, to_emails, subject, message, image_path=None):
    # Buat objek MIME multipart
    msg = MIMEMultipart()

    # Isi pengirim, penerima, dan subjek
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = subject

    # Tambahkan isi email dalam format HTML
    html = f'<html><body>{message}</body></html>'
    msg.attach(MIMEText(html, 'html'))

    # Tambahkan gambar jika ada
    if image_path:
        with open(image_path, 'rb') as img_file:
            image_data = img_file.read()
        image = MIMEImage(image_data, name='image.png')
        msg.attach(image)

    # Kirim email menggunakan SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.close()
        print('Email berhasil dikirim!')
    except Exception as e:
        print(f'Gagal mengirim email: {str(e)}')

if __name__ == '__main__':
    from_email = 'ikhsanaa@students.amikom.ac.id'
    from_password = 'Ara130202@'
    to_emails = input("Masukkan alamat email penerima: ")
    subject = input("Masukkan subjek email: ")
    message = input("Masukkan pesan email: ")
    #image_path = 'path/to/image.png'  # Ganti dengan path gambar yang ingin dikirim, jika ada

    send_email(from_email, from_password, to_emails, subject, message) # Tambahkan image_path pada kurung jika ingin mengirim foto

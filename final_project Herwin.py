import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "pengirim@gmail.com"
toaddr = "penerima@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python"

body = "Mengirimkan logo python sebagai lampiran"

msg.attach(MIMEText(body, 'plain'))

filename = "logo.png"
attachment = open("C:\\Users\\DELL\\Documents\\python\\basic-python\\Final\\logo.png","rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "PASSWORD GMAIL")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
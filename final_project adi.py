# AUTHOR: ADI

import os
import csv
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


def read_target_email_address(nama_file):
    try:
        with open(nama_file, 'r') as file:
            contents = file.readlines()
        return [item.strip() for item in contents]    
    except Exception:
        raise


def read_file_content(nama_file):
    try:
        with open(nama_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            next(csv_reader)
            return list(csv_reader)
    except Exception:
        raise 


def send_email_test(your_email_password):
    
    fromaddr = 'adi.python.test.2020@gmail.com'
    toaddr = 'adi4vista@gmail.com'
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Test Kirim Email dengan Python Script'
    
    body = "Hi ..."
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, your_email_password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    

def send_email_test_2(list_data_penerima, your_email_password):
    
    fromaddr = 'adi.python.test.2020@gmail.com'
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = ','.join(list_data_penerima)
    msg['Subject'] = 'Test Kirim Email dengan Python Script Test 5'
    
    body = "Test Kirim Email Pakai Script Python Nih !!!"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, your_email_password)
    server.send_message(msg)
    server.quit()
    

def send_email_test_3(list_data_penerima, your_email_password):
    
    fromaddr = 'adi.python.test.2020@gmail.com'
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['Subject'] = 'Test Kirim Email dengan Python Script Test 6'
    
    body = "Test Kirim Email dengan Attachment"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, your_email_password)
    server.sendmail(fromaddr, list_data_penerima, msg.as_string())
    server.quit()


def send_email_test_with_attachment(list_data_penerima, your_email_password):
    
    fromaddr = 'adi.python.test.2020@gmail.com'
    nama_file_pdf = 'python_file_tutorialpoint.pdf'
    nama_file_image = 'wonderful_indonesia.jpg'
    nama_file_text = 'final_project.py'
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = ','.join(list_data_penerima)
    msg['Subject'] = 'Email Test Dikirim dari Python'
    
    body = f'Ini adalah sample body message.\nAnda Bisa Ubah Isi Pesan Email Sesuai dengan yang anda inginkan\n\nthanks.'
        
    msg.attach(MIMEText(body, 'plain'))

    # attach pdf
    lampiran1 = MIMEApplication(open(nama_file_pdf, 'rb').read())
    lampiran1.add_header('Content-Disposition', 'attachment', filename=nama_file_pdf)
    msg.attach(lampiran1)
    
    # attach image
    fp = open(nama_file_image, 'rb')
    lampiran2 = MIMEImage(fp.read())
    lampiran2.add_header('Content-Disposition', 'attachment', filename=nama_file_image)
    fp.close()
    msg.attach(lampiran2)

    # attach text file
    lampiran3 = MIMEText(open(nama_file_text, 'r').read())
    lampiran3.add_header('Content-Disposition', 'attachment', filename=nama_file_text)
    msg.attach(lampiran3)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.set_debuglevel(1)
    server.login(fromaddr, your_email_password)
    # server.sendmail(fromaddr, list_data_penerima, msg.as_string())
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    os.system('cls')
    your_email_password = getpass.getpass('email password ? ')
    try:
        # list_data_penerima = read_file_content('receiver_list.txt')
        # print(list_data_penerima)
        list_data_penerima = read_target_email_address('receiver_list.txt')
        for item in list_data_penerima:
            print(item)
        send_email_test_with_attachment(list_data_penerima, your_email_password)
        print('done.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
    

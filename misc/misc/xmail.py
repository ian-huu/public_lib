# -*- coding: utf-8 -*-
import time, datetime
import smtplib, email
import re, string
import StringIO

def send(from_addr, to_addr, subject, text, files, conf = {}):
    from_addr = from_addr if from_addr else conf['from'] if 'from' in conf else 'service@ethercap.com'
    to_addr = ','.join(to_addr) if isinstance(to_addr, (list, tuple)) else to_addr

    server = conf['server'] if 'server' in conf else "smtp.exmail.qq.com"
    port = cinf['port'] if 'port' in conf else 465
    username = conf['username'] if 'username' in conf else 'service@ethercap.com'
    passwd = conf['passwd'] if 'passwd' in conf else '***'
    server = smtplib.SMTP_SSL(server, port)
    server.ehlo()
    server.login(username, passwd)
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    if 'cc' in conf:
        cc_addr = ','.join(conf['cc']) if isinstance(conf['cc'], (list, tuple)) else conf['cc']
        msg['Cc'] = cc_addr
    else:
        cc_addr = ''
    msg['Subject'] = subject
    msg.attach(email.MIMEText.MIMEText(text, 'html', 'utf-8'))

    for name, f in files.items():
        part = email.MIMEBase.MIMEBase('application', "octet-stream")
        part.set_payload(f.getvalue() if isinstance(f, StringIO.StringIO) else open(f, "rb").read())
        email.Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % name)
        msg.attach(part)
    to_addr_lst = filter(lambda x: x, to_addr.split(',')+ cc_addr.split(','))
    server.sendmail(from_addr, to_addr_lst, msg.as_string())
    server.close()

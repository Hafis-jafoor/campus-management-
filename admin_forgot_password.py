#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()

import random
otp = random.randint(00000, 99999)

print("""
<html>
<head>
</head>
<body>
    <h2><i>Forgot Password</i></h2>
    <div>
        <form method = "post">
            <input type="email" placeholder="enter the email"  name = "email"><br><br>
            <input type = "submit" value = "sent otp" name = "ssub">
            <p>back to login?<a href = "admin_login.py">login form</a></p>
        </form>
    </div>
</body>
</html>
""")
import cgi

a = cgi.FieldStorage()
uemail = a.getvalue("email")
usub = a.getvalue("ssub")
if usub != None:
    cur.execute("""select Sno,Email from Admin where Email = '%s'""" % (uemail))
    f = cur.fetchone()
    if f != None:
        import smtplib
        from email.message import EmailMessage

        fromacc = "hafis3052000@gmail.com"
        passwd = "bscv jeej slrv jttb"
        toacc = uemail
        message = EmailMessage()
        message.set_content('  This is your OTP: %s' % (otp))
        message['Subject'] = 'admin password reset'
        message['From'] = "hafis3052000@gmail.com"
        message['To'] = uemail
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromacc, passwd)
        server.send_message(message)
        server.quit()
        print("""
        <script>
           alert(" mail sent successfully..!");
           location.href = "admin_otp.py?otp=%s&sno=%s"
        </script>
        """ % (otp, f[0]))
    else:
        print("""
        <script>
           alert(" mail not registered..!");
        </script>
        """)
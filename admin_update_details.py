#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi
import os

a = cgi.FieldStorage()
ids = a.getvalue("sno")
# print(ids)

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Admin where Sno = %s""" % (ids))
f = cur.fetchone()
# print(f)
print("""
<html>
<head>
</head>
<body>
    <h2><i>Update</i></h2>
    <div>
        <form method = "post" enctype = "multipart/form-data">
            <input type="text" placeholder="enter the username"  name = "uname" value ="%s"><br><br>
            <input type = "email" placeholder="enter the email"  name = "uemail" value ="%s"><br><br>
            <input type = "password" placeholder="enter the password"  name = "upass" value ="%s"><br><br>
            <input type = "file" placeholder="enter the image"  name = "ufile" value ="%s"><br><br>
            <input type = "submit" name = "ssub" value="update">
            <p>admin profile?<a href = "admin_main_page.py">Admin profile</a></p>
        </form>
    </div>
</body>
</html>
""" % (f[1], f[2], f[3], f[4]))

name = a.getvalue("uname")
passw = a.getvalue("upass")
email = a.getvalue("uemail")
image = a['ufile']
sub = a.getvalue("ssub")
if sub != None:
    fn = os.path.basename(image.filename)
    open("files/" + fn, "wb").write(image.file.read())
    cur.execute("""update Admin set Username = "%s",Email = '%s',Password="%s", File="%s" where Sno = '%s'""" % (name,
                                                                                                                 email,
                                                                                                                 passw,
                                                                                                                 fn,
                                                                                                                 ids))
    conn.commit()
    print("""
            <script>
               alert("updated");
               location.href = "admin_main_page.py"
            </script>
            """)


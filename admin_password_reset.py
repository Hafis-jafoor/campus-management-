#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi

a = cgi.FieldStorage()
id1 = a.getvalue("sno")
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()

print("""
<html>
<head>
</head>
<body>
    <h2><i>set new admin password</i></h2>
    <div>
        <form method = "post">
            <input type="password" placeholder="enter the password"  name = "upass"><br><br>
            <input type="password" placeholder="enter the confirm password"  name = "cpass"><br><br>
            <input type = "submit" value = "update" name = "ssub">
            <p>back to login?<a href = "admin_login.py" >login form</a></p>
        </form>
    </div>
</body>
</html>
""")

pas = a.getvalue("upass")
cass = a.getvalue("cpass")
sub = a.getvalue("ssub")
if sub != None:
    if pas == cass:
        cur.execute("""update Admin set Password = '%s' where Sno = '%s'""" % (pas, id1))
        conn.commit()
        print("""
            <script>
               alert("password changed");
               location.href = "admin_login.py"
            </script>
            """)
    else:
        print("""
            <script>
               alert("password not match");
            </script>
            """)

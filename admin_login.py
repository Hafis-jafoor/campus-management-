#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
print("""
<html>
<head>
</head>
<body>
    <h2><i>Admin Login</i></h2>
    <div>
        <form method = "post">
            <input type="text" placeholder="enter the admin email" name = "aemail"><br><br>
            <input type="password" placeholder="enter the admin password" name = "apass"><br><br>
            <input type = "submit" name = "ssub">
            <p>forgot password?<a href = "admin_forgot_password.py">click here</a></p>
        </form>
    </div>
</body>
</html>
""")
import cgi
a = cgi.FieldStorage()
email = a.getvalue("aemail")
password = a.getvalue("apass")
ssub = a.getvalue("ssub")
if ssub != None:
    cur.execute("""select * from Admin where Email = '%s' and Password = '%s'"""
                % (email, password))
    f = cur.fetchone()
    if f != None:
        print("""
            <script>
                alert("login successfully");
            </script>
            """)
    else:
        print("""
            <script>
                alert("login unsuccessfull");
            </script>
            """)

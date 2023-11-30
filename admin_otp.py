#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi

a = cgi.FieldStorage()
potp = a.getvalue("otp")
ids = a.getvalue("sno")
print(potp)

print("""
<html>
<head>
</head>
<body>
    <h2><i>otp validation</i></h2>
    <div>
        <form method = "post">
            <input type="number" placeholder= " enter the otp" name = "uotp"><br><br>
            <input type = "submit" value = "validate" name = "ssub">
            <p>back to login?<a href = "admin_login.py">login form</a></p>
        </form>
    </div>
</body>
</html>
""")

otpq = a.getvalue("uotp")
usub = a.getvalue("ssub")
if usub != None:
    if potp == otpq:
        print("""
            <script>
               alert("otp correct");
               location.href = "admin_password_reset.py?sno=%s"
            </script>
            """%(ids))
    else:
        print("""
            <script>
               alert("otp incorrect");
            </script>
            """)

#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
print("""
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .fa{
            padding:20px;
            font-size: 35px;
        }
    </style>
</head>
<body>
    <a href="admin_main_page.py"><i class="fa fa-arrow-left"></i></a>
    <h2><i>pioneers insert</i></h2>
    <div>
        <form method = "post" enctype = "multipart/form-data" >
              <input type="text" placeholder="enter the pioneer name" name = "pname"><br><br>
              <input type="text" placeholder="enter the pioneer designation" name = "dname"><br><br>
              <input type="file" name = "pimage"><br><br>
              <input type = "submit" value = "insert" name = "ssub">
        </form>
    </div>
</body>
</html>
""")
import cgi, os

f = cgi.FieldStorage()
name = f.getvalue("pname")
designation = f.getvalue("dname")
image = f['pimage']
sub = f.getvalue("ssub")
if sub != None:
    fn = os.path.basename(image.filename)
    open("files/" + fn, "wb").write(image.file.read())
    cur.execute("""insert into Pioneers(Name,Designation,File)values('%s','%s','%s')
                """ % (name, designation, fn))
    conn.commit()
    print("""
        <script>
           alert("inserted successfully..!");
        </script>
        """)

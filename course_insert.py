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
    <h2><i>Course insert</i></h2>
    <div>
        <form method = "post" enctype = "multipart/form-data" >
            <input type="text" placeholder="enter the course name" name = "cname"><br><br>
            <label>Eligibility</label>
            <input type="radio" name = "eligible" value="Ug">Ug
            <input type="radio" name = "eligible" value="Pg">Pg 
            <input type="radio" name = "eligible" value="Diploma">Diploma<br><br>
            duration
            <input type="text" placeholder="enter the fees detail" name = "fdetail"><br><br>
            <input type="file" name = "cfile"><br><br>
            <input type = "submit" value = "insert" name = "ssub">
        </form>
    </div>
</body>
</html>
""")
import cgi, os

f = cgi.FieldStorage()
name = f.getvalue("cname")
course = f.getvalue("cdetail")
batch = f.getvalue("cbatch")
image = f['cimage']
sub = f.getvalue("ssub")
if sub != None:
    fn = os.path.basename(image.filename)
    open("files/" + fn, "wb").write(image.file.read())
    cur.execute("""insert into Cappers(Name,Course,Batch,File)values('%s','%s','%s','%s')
                """ % (name, course, batch, fn))
    conn.commit()
    print("""
        <script>
           alert("inserted successfully..!");
        </script>
        """)

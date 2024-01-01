#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

from datetime import date
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
today = date.today()
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
    <h2><i>Notification insert</i></h2>
    <div>
        <form method = "post">
            <input type="date" name = "ndate" value="%s"><br><br>
            <input type="text" placeholder="enter the subject" name = "sname"><br><br>
            <label>enter the person to sent</label>
            <input type="radio" name = "position" value="student">student
            <input type="radio" name = "position" value="faculty">faculty 
             <input type="radio" name = "position" value="common">common<br><br>
             <textarea  name="notification" rows="10" cols="100" placeholder="enter the notification">
            </textarea><br><br>  
            <input type = "submit" value = "insert" name = "ssub">
        </form>
    </div>
</body>
</html>
""" % today)
import cgi

f = cgi.FieldStorage()
date = f.getvalue("ndate")
name = f.getvalue("sname")
notification = f.getvalue("notification")
position = f.getvalue("position")
sub = f.getvalue("ssub")
if sub != None:
    cur.execute("""insert into Notification(Date,Subject,Person,Notification)values('%s','%s','%s','%s')
                """ % (date, name, position, notification))
    conn.commit()
    print("""
        <script>
           alert("inserted successfully..!");
        </script>
        """)

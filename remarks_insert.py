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
</head>
<body>
    <h2><i>remarks insert</i></h2>
    <div>
        <form method = "post">
            <input type="date" placeholder="enter the current date" name = "rdate" value="%s"><br><br>
            <textarea  name="remark" rows="10" cols="100">
            </textarea><br><br>
            <input type="text" placeholder="enter the username" name = "rname"><br><br>
            <input type="radio" name = "position" value="student">student
            <input type="radio" name = "position" value="faculty">faculty  <br><br>  
            <input type = "submit" value = "insert" name = "ssub">
        </form>
    </div>
</body>
</html>
""" % (today))
import cgi

f = cgi.FieldStorage()
date = f.getvalue("rdate")
remark = f.getvalue("remark")
name = f.getvalue("rname")
position = f.getvalue("position")
sub = f.getvalue("ssub")
if sub != None:
    cur.execute("""insert into Remarks(Date,Remarks,Status,Username,Position)values('%s','%s','%s','%s','%s')
                """ % (date, remark, 'recent', name, position))
    conn.commit()
    print("""
        <script>
           alert("inserted successfully..!");
        </script>
        """)

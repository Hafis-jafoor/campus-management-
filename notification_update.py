#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi

a = cgi.FieldStorage()
ids = a.getvalue("sno")
# print(ids)

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Notification where Sno = %s""" % (ids))
f = cur.fetchone()
# print(f)
print("""
<html>
<head>
</head>
<body>
    <h2><i>Notification Update</i></h2>
    <div>
        <form method = "post">
            <input type="date" name = "ndate" value="%s"><br><br>
            <input type="text" name = "sname" value="%s"><br><br>
            <label>enter the person to sent</label>
            <input type="radio" name = "position" value="student">student
            <input type="radio" name = "position" value="faculty">faculty 
             <input type="radio" name = "position" value="common">common<br><br>
             <textarea  name="notification" rows="10" cols="100">
            </textarea><br><br>  
            <input type = "submit" value = "update" name = "ssub">
            <input type = "submit" name = "sdelete" value="delete">
        </form>
    </div>
</body>
</html>
""" % (f[1], f[2]))

date = a.getvalue("ndate")
name = a.getvalue("sname")
position = a.getvalue("position")
notification = a.getvalue("notification")
sub = a.getvalue("ssub")
dsub = a.getvalue("sdelete")
if sub != None:
    cur.execute("""update Notification set Date = "%s",Subject = '%s',Person="%s", Notification="%s" 
    where Sno = '%s'""" % (date, name, position, notification, ids))
    conn.commit()
    print("""
            <script>
               alert("updated");
               location.href = "all_notification_retrieve.py"
            </script>
            """)
if dsub != None:
    cur.execute("""DELETE FROM Notification WHERE Sno = "%s" """ % ids)
    conn.commit()
    print("""
                <script>
                   alert("deleted");
                   location.href = "all_notification_retrieve.py"
                </script>
                """)

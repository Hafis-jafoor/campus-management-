#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi

a = cgi.FieldStorage()
ids = a.getvalue("sno")
# print(ids)

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Cappers where Sno = %s""" % (ids))
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
            <input type="text" placeholder="enter the name"  name = "uname" value ="%s"><br><br>
            <input type = "text" placeholder="enter the course"  name = "ucourse" value ="%s"><br><br>
            <input type = "text" placeholder="enter the batch"  name = "ubatch" value ="%s"><br><br>
            <input type = "file" placeholder="enter the image"  name = "ufile" value ="%s"><br><br>
            <input type = "submit" name = "ssub" value="update">
            <input type = "submit" name = "sdelete" value="delete">
            <p>admin profile?<a href = "cappers_table_retrieve.py">pioneers table</a></p>
        </form>
    </div>
</body>
</html>
""" % (f[1], f[2], f[3], f[4]))
import  os
name = a.getvalue("uname")
course = a.getvalue("ucourse")
batch = a.getvalue("ubatch")
# file = a.getvalue("ufile")
image = a['ufile']
sub = a.getvalue("ssub")
dsub = a.getvalue("sdelete")
if sub != None:
    fn = os.path.basename(image.filename)
    open("files/" + fn, "wb").write(image.file.read())
    cur.execute("""update Cappers set Name = "%s",Course = '%s',Batch="%s", File="%s" where Sno = '%s'""" % (name,
                                                                                                             course,
                                                                                                             batch,
                                                                                                             fn,
                                                                                                             ids))
    conn.commit()
    print("""
            <script>
               alert("updated");
               location.href = "cappers_table_retrieve.py"
            </script>
            """)
if dsub != None:
    cur.execute("""DELETE FROM Cappers WHERE Sno = "%s" """ % ids)
    conn.commit()
    print("""
                <script>
                   alert("deleted");
                   location.href = "cappers_table_retrieve.py"
                </script>
                """)

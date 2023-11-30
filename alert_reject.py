#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql, cgi

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
f = cgi.FieldStorage()
rid = f.getvalue("rid")
if rid != None:
    q = """update Remarks set Status='rejected' where Sno=%s""" % rid
    cur.execute(q)
    conn.commit()
    conn.close()
    print("""
        <script>
            alert("rejected");
            location.href="recent_remarks.py";
        </script>
        """)

orid = f.getvalue("orid")
if orid != None:
    q = """update Remarks set Status='rejected' where Sno=%s""" % orid
    cur.execute(q)
    conn.commit()
    conn.close()
    print("""
        <script>
            alert("rejected");
            location.href="ongoing_remarks.py";
        </script>
        """)


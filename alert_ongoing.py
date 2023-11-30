#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql, cgi

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
f = cgi.FieldStorage()
oid = f.getvalue("oid")
if oid != None:
    q = """update Remarks set Status='ongoing' where Sno=%s""" % oid
    cur.execute(q)
    conn.commit()
    conn.close()
    print("""
        <script>
            alert("ongoing");
            location.href="recent_remarks.py";
        </script>
        """)

roid = f.getvalue("roid")
if roid != None:
    q = """update Remarks set Status='ongoing' where Sno=%s""" % roid
    cur.execute(q)
    conn.commit()
    conn.close()
    print("""
        <script>
            alert("ongoing");
            location.href="rejected_remarks.py";
        </script>
        """)
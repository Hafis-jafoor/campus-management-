#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql, cgi

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
f = cgi.FieldStorage()
aid = f.getvalue("aid")
q = """update Remarks set Status='approved' where Sno=%s""" % aid
cur.execute(q)
conn.commit()
conn.close()
print("""
    <script>
        alert("approved");
        location.href="ongoing_remarks.py";
    </script>
    """)

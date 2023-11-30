#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Remarks where Status="ongoing" """)
f = cur.fetchall()

print("""
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
    table,td,th{
         border-radius:30px;
         padding:10px;
         background-color:white;
         border:2px solid black;
         border-collapse:collapse;
    }
    div{
        display:flex;
        text-items:center;
        justify-content:center;
    }
    .fa{
        padding:20px;
        font-size: 35px;
        }
</style>
</head>
<body>
    <a href="admin_main_page.py"><i class="fa fa-arrow-left"></i></a>
    <h2 style = "text-align:center"><i>Ongoing Remarks Details</i></h2>
    <div>
    <table>
        <tr>
            <th>Date</th>
            <th>Remarks</th>    
            <th>Status</th>    
            <th>Username</th>
            <th>Position</th>
            <th>Stage</th>
        </tr>""")
for i in f:
    print("""
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
            <form method = "post" action="alert_approve.py">  
                <input type="hidden" value="%s" name="aid">
                <input type = "submit" value = "approve" name = "rsub">
            </form>
            <form method = "post" action="alert_reject.py">  
                <input type="hidden" value="%s" name="orid">
                <input type = "submit" value = "reject" name = "rsub">
            </form>
            </td>
        </tr>""" % (i[1], i[2], i[3], i[4], i[5], i[0], i[0]))
print("""
        </table>
        </div>
    </body>
    </html>
    """)

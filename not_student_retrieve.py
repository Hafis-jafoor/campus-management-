#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Notification where Person="student" """)
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
    <h2 style = "text-align:center"><i>Student Notification Details</i></h2>
    <div>
    <table>
        <tr>
            <th>Date</th>
            <th>Subject</th>    
            <th>Person</th>
            <th>Notification</th>
            <th>update</th>
        </tr>""")
for i in f:
    print("""
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a href = "notification_update.py?sno=%s">update</a></td>
        </tr>""" % (i[1], i[2], i[3], i[4], i[0]))
print("""
        </table>
        </div>
    </body>
    </html>
    """)
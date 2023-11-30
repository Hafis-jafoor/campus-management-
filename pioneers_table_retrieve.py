#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Pioneers""")
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
    <h2 style = "text-align:center"><i>pioneers Details</i></h2>
    <div>
    <table>
        <tr>
            <th>Name</th>
            <th>Designation</th>    
            <th>File</th>
            <th>Update</th>
        </tr>""")
for i in f:
    print("""
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a href = "pioneers_update.py?sno=%s">update</a></td>
        </tr>""" % (i[1], i[2], i[3], i[0]))
print("""
        </table>
        </div>
    </body>
    </html>
    """)

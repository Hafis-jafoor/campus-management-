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
        *{
            margin: 0px;
            padding: 0px;
        }
        body{
             background-image: url("assets/images/main_page1.jpg");
             background-size: cover;   
        }
        .pioneers_image img{
            border:2px solid white;
            border-radius:10px;
        }
        .pioneers_image{
            position:relative;
            top:150px;
            float:left;
            padding:50px;
            left:60px;
            transition:transform 0.5s;
        }
        .pioneers_image:hover{
            transform:translateY(-30px);
        }
        .pioneers_image p{
            color:black;
            font-weight:bold;
            font-size:20px;
        }
        .institute_footer{
            position:absolute;
            background-color:white;
            width:100%;
            bottom:-280px;
            padding:30px;
            opacity:0.6;
        }
        .if1,.if2{
            display: flex;
            justify-content: center;
            color:black;
        }
        .main{
            height:100%;
            width:100%;
            position:relative;
        }
        .institute_name{
            position:absolute;
            background-color:white;
            width:100%;
            height:100px;
            top:0px;
            opacity:0.6;
            z-index:1;
        }
        .institute_name h1{
            font-size:70px;
            color:black;
            text-align:center;
            opacity:1;
        }
        .institute_span{
            position:absolute;
            margin-left:900px;
        }
        .head{
            position:absolute;
            margin-left:620px;
            top:120px;
        }
        .fa{
            position:absolute;
            padding:20px;
            font-size: 35px;
            z-index:1;
        }
    </style>
    </head>
    <body>
    <div class="main">
        <div class="institute_name">
                <h1>PEACE INSTITUTE</h1>
                <span class="institute_span"><i>since 2000</i></span>
        </div>
        <a href="index.html"><i class="fa fa-home"></i></a>
        <h1 class="head">Pioneers</h1>
""")

for i in f:
    b = "files/" + i[3]
    c = i[1]
    d = i[2]

    print("""
        <div class = "pioneers_image">
            <img src = '%s' height = "200" width = "300">
            <p style = "text-align: center;"><b><i>%s</i></b></p>
            <p style = "text-align: center;"><i>%s</i></p>
        </div>
    """ % (b, c, d))
print("""
        <div class="institute_footer">
            <span class="if1"><b>© Copyright 2023 - PEACE INSTITUTE.</b></span>
            <span class="if2">Powered By Aju Hafi</span>
        </div>
    </div>
    </body>
    </html>
""")

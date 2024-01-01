#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = conn.cursor()
cur.execute("""select * from Admin where Username='Hafis Jafoor V'""")
f = cur.fetchone()
print("""
<html>
<head>
    <link rel="stylesheet" 
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        *{
            margin: 0px;
            padding: 0px;
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
            margin-left:920px;
        }
        .portal{
            position:absolute;
            background-color:black;
            width:100%;
            height:50px;
            top:120;
            opacity:0.3;
            z-index:1;
            padding:10px;
        }
        .portal h1{
            font-size:50px;
            color:white;
            text-align:center;
            opacity:1;
        }
        .sidenav {
            height: 100%;
            width: 200px;
            position: fixed;
            z-index: 1;
            top: 0;
            # top: 101;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            padding-top: 20px;
        }
        .sidenav a, .dropdown-btn {
            padding: 6px 8px 6px 16px;
            text-decoration: none;
            font-size: 23px;
            color: white;
            display: block;
            border: none;
            background: none;
            width: 100%;
            text-align: left;
            cursor: pointer;
            # outline: none;
        }
        .sidenav a:hover, .dropdown-btn:hover {
            color: grey;
        }
        .active {
          background-color: black;
          color: red;
        }
        .dropdown-container {
            display: none;
            background-color: white;
            padding-left: 8px;
        }
        .dropdown-container a{
            color:black;
            font-size: 20px;
        }
        .fa-caret-down {
            float: right;
            padding-right: 8px;
        }
        .institute_footer{
            position:absolute;
            background-color:white;
            width:100%;
            bottom:0;
            padding:30px;
            background-color:white;
            opacity:0.6;
        }
        .if1,.if2{
            display: flex;
            justify-content: center;
            color:black;
        }
        .middle{
            position:absolute;
            height:350px;
            width:1000px;
            top:200;
            left:250;
        }
        .middle p{
            font-size:30px;
            margin-top:20px;
            margin-left:100px;
            padding:10px;
        }
        .middle img{
            float:right;
            margin-top:-200px;
            margin-right:120px;
        }
        .middle a button{
            float:right;
            margin-right:130px;     
            text-decoration:none;
            margin-top:20px;
            font-size: 25px;
            padding:5px;
            border-radius:10px;
        }
        .middle a button:hover{
            background-color:grey;
        }
    </style>
</head>""")
b = "files/" + f[4]
print(""""
<body>
    <div class="main">
        <div class="institute_name">
            <h1>PEACE INSTITUTE</h1>
            <span class="institute_span"><i>since 2000</i></span>
        </div>
        <div class="portal">
            <h1>Admin Portal</h1>
        </div>
        <div class="sidenav">
            <a href="">Profile</a>
            <button class="dropdown-btn">Faculty 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="#">New faculty</a>
                <a href="#">Existing faculty</a>
            </div>
            <button class="dropdown-btn">Students 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="#">New students</a>
                <a href="#">Existing students</a>
            </div>
            <button class="dropdown-btn">Courses 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="#">New courses</a>
                <a href="#">Existing courses</a>
            </div>
            <button class="dropdown-btn">Notification 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="notification_insert.py">New notification</a>
                <a href="not_student_retrieve.py">Student notification</a>
                <a href="not_faculty_retrieve.py">Faculty notification</a>
                <a href="not_common_retrieve.py">Common notification</a>
                <a href="all_notification_retrieve.py">All notification</a>
            </div>
            <button class="dropdown-btn">Remarks 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="recent_remarks.py">Recent Remarks</a>
                <a href="ongoing_remarks.py">Ongoing Remarks</a>
                <a href="approved_remarks.py">Approved Remarks</a>
                <a href="rejected_remarks.py">Rejected Remarks</a>
                <a href="all_remarks.py">All Remarks</a>
            </div>
            <button class="dropdown-btn">Pioneers 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="pioneers_table_retrieve.py">Existing pioneers</a>
                <a href="pioneers_insert.py">New pioneers</a>
            </div>
            <button class="dropdown-btn">Cappers 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="cappers_table_retrieve.py">Existing cappers</a>
                <a href="cappers_insert.py">New cappers</a>
            </div>
            <button class="dropdown-btn">Academes 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-container">
                <a href="academes_table_retrieve.py">Existing academes</a>
                <a href="academes_insert.py">New academes</a>
            </div>
            <a href="#about">Logout</a>
        </div>
        <div class = "middle">
            <p><b>Username:%s</b></p>
            <p><b>Email:%s</b></p>
            <p><b>Password:%s</b></p>
            <img src = '%s' height = "200" width = "200">
            <a href = "admin_update_details.py?sno=%s"><button class="u_middle">update details </button></a>
        </div>
        <div class="institute_footer">
            <span class="if1"><b>© Copyright 2023 - PEACE INSTITUTE.</b></span>
            <span class="if2">Powered By Aju Hafi</span>
        </div>
    </div>""" % (f[1], f[2], f[3], b, f[0]))
print(""""
    <script>
        var dropdown = document.getElementsByClassName("dropdown-btn");
        var i;
        for (i = 0; i < dropdown.length; i++) {
          dropdown[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === "block") {
              dropdownContent.style.display = "none";
            } else {
              dropdownContent.style.display = "block";
            }
          });
        }
    </script>
</body>
</html>
""")

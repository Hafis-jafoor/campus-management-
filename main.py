#!C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


# DATABASE CREATION
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="")
# cur = connection.cursor()
# cur.execute("""create database Peace_institution""")
# connection.commit()
# print("""
# <script>
#     alert("database created successfully..!")
# </script>
# """)
# connection.close()

# TABLE CREATION Pioneers
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Pioneers(Sno int(50)auto_increment primary key,
#                                     Name varchar(100),
#                                     Designation varchar(255),
#                                     File varchar(100) )""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Cappers
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Cappers(Sno int(50)auto_increment primary key,
#                                     Name varchar(100),
#                                     Course varchar(255),
#                                     Batch varchar(100),
#                                     File varchar(100))""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Academes
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Academes(Sno int(50)auto_increment primary key,
#                                     Name varchar(100),
#                                     Achievement varchar(255),
#                                     File varchar(100))""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Admin
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Admin(Sno int(20)auto_increment primary key,
#                                     Username varchar(100),
#                                     Email varchar(200),
#                                     Password varchar(100),
#                                     File varchar(200))""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE INSERTION OF Admin
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""insert into Admin(Username,Email,Password,File)values('Hafis Jafoor V','hafis3052000@gmail.com',
# '12345', 'hafis_profile.jpg') """)
# cur.execute("""insert into Admin(Username,Email,Password,File)values('Ajhad','aju@gmail.com','123456',
#                 'aju_profile.jpg')
#                 """)
# connection.commit()
# print("""
# <script>
#     alert("inserted successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Remarks
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Remarks(Sno int(50)auto_increment primary key,
#                                     Date  DATE,
#                                     Remarks varchar(65530),
#                                     Status varchar(100))""")
# cur.execute("""ALTER TABLE Remarks
# ADD Username varchar(255)""")
# cur.execute("""ALTER TABLE Remarks
# ADD Position varchar(255)""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Notification
# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
# cur = connection.cursor()
# cur.execute("""create table Notification(Sno int(50)auto_increment primary key,
#                                     Date  DATE,
#                                     Subject varchar(200),
#                                     Person varchar(100),
#                                     Notification varchar(65530))""")
# # cur.execute("""ALTER TABLE Remarks
# # ADD Username varchar(255)""")
# # cur.execute("""ALTER TABLE Remarks
# # ADD Position varchar(255)""")
# connection.commit()
# print("""
# <script>
#     alert("table created successfully..!");
# </script>
# """)
# connection.close()

# TABLE CREATION Courses
import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="Peace_institution")
cur = connection.cursor()
# cur.execute("""create table Courses(Sno int(50)auto_increment primary key,
#                                     Course_name  varchar(200),
#                                     Eligibility  varchar(200),
#                                     Duration varchar(200),
#                                     Fees varchar(100))""")
cur.execute("""ALTER TABLE Courses
ADD File varchar(255)""")
# cur.execute("""ALTER TABLE Remarks
# ADD Position varchar(255)""")
connection.commit()
print("""
<script>
    alert("table created successfully..!");
</script>
""")
connection.close()

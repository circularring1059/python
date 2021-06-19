import pymysql

connect = pymysql.connect(host="192.168.112.12", port=3306, user="root", passwd="root", db='ring', charset="utf8")
cursor1 = connect.cursor()
cursor1.execute("select name, class_id from class")
class_list = cursor1.fetchall()
cursor1.close()
connect.close()
print(class_list)

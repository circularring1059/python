import pymysql

connect = pymysql.connect(host="192.168.112.12", port=3306, user="root", passwd="root", db="ring", charset="utf8")

cursor4 = connect.cursor()
cursor4.execute("delete from class where class_id = 2")
connect.commit()
cursor4.close()
connect.close()
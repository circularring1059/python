import  pymysql

connect = pymysql.connect(host="192.168.112.12", port=3306, user="root", passwd="root", db="ring", charset="utf8")
cursor3 = connect.cursor()
cursor3.execute("update class set name='物理一班' where class_id = 5")
connect.commit()
cursor3.close()
connect.close()
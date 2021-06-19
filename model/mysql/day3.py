# import pymysql
#
# connect = pymysql.connect(host="192.168.112.12", port=3306, user="root", passwd="root", db="ring", charset="utf8")
# cursor2 = connect.cursor(cursor=pymysql.cursors.DictCursor)
# cursor2.execute("insert into class(name, class_id)values(%s, %s)",['电子一班',4])
# connect.commit()
# cursor2.close()
# connect.close()
# print("添加成功")
print("insert into class(name, class_id)values(%s, %s)",['电子一班',4])

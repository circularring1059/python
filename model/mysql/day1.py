import pymysql

def classes():
    conn = pymysql.connect(host='192.168.112.12', port=3306, user='root', password='root', db='ring', charset='utf8')  #创建链接
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 设置查询结果为字典格式
    # cursor = conn.cursor()  # 设置查询结果为字典格式
    cursor.execute("select name, class_id from class")
    class_list = cursor.fetchall()  # 结果为字典,全部数据
    # class_list = cursor.fetchone()  # 结果为字典，一条数据
    cursor.close()  #关闭游标
    conn.close() #关闭连接
    print(class_list)
    return class_list

print(type(classes()))   #list
import pymysql
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='970320',
    db='python',
    charset='utf8')
cursor=connect.cursor()
for i in range(1,3):
    cursor.execute('create table if not exists %s(id int,info varchar(20))',(i))
    connect.commit()
    connect.close()
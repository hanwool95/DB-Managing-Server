
import pymysql

from secrete_dir.password import mysql_password
from secrete_dir.template import make_d, make_l, make_m

if "__main__":
    conn = pymysql.connect(host="127.0.0.1", user='root', password=mysql_password, db='test_db', charset='utf8')
    curs = conn.cursor()
    curs.execute(make_d)
    curs.execute(make_l)
    curs.execute(make_m)

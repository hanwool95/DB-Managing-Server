
import pymysql

from secrete_dir.password import mysql_password
from secrete_dir.template import orient_table

if "__main__":
    conn = pymysql.connect(host="127.0.0.1", user='root', password=mysql_password, db='test_db', charset='utf8')
    curs = conn.cursor()
    for case in orient_table:
        curs.execute(case)

import pymysql
import csv

from secrete_dir.password import mysql_password

from secrete_dir.template import insert_code_dict, code_list, float_dict


def Data_to_DB(code):
    conn = pymysql.connect(host="127.0.0.1", user='root', password=mysql_password, db='test_db', charset='utf8')
    curs = conn.cursor()
    conn.commit()

    f = open('secrete_dir/'+code+'.csv', 'r')
    r = csv.reader(f)

    next(r)
    float_list = float_dict[code]

    for row in r:
        value_list = []
        for i, value in enumerate(row):
            data = value
            if i in float_list:
                if data == '':
                    data = None
                else:
                    data = float(data)
            value_list.append(data)
        value_tuple = tuple(value_list)
        curs.execute(insert_code_dict[code], value_tuple)

    f.close()
    conn.close()

if "__main__":
    for code in code_list:
        Data_to_DB(code)



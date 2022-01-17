import pymysql

import csv

from secrete_dir.template import insert_code_new_dict, select_code_dict, concate_table, concate_csv_list

from secrete_dir.password import mysql_password


def get_case_and_make_table(number):

    conn = pymysql.connect(host="127.0.0.1", user='root', password=mysql_password, db='test_db', charset='utf8')
    curs = conn.cursor()

    case_number = "Case "+number

    making_new_concatenate_tables(curs)
    add_data_to_new_table(case_number, curs, 'dx')
    add_data_to_new_table(case_number, curs, 'lab')
    add_data_to_new_table(case_number, curs, 'med')

    make_csv_new_table(case_number, curs)



def making_new_concatenate_tables(curs):
    sql_table = concate_table

    curs.execute(sql_table)


def add_data_to_new_table(case_number, curs, data_style):
    sql = select_code_dict[data_style]
    curs.execute(sql, (case_number))

    res = curs.fetchall()

    for data in res:
        value_tuple = tuple(x for i, x in enumerate(data) if i > 0)
        sql = insert_code_new_dict[data_style]
        curs.execute(sql, value_tuple)

def make_csv_new_table(case_number, curs):

    file_name = "case_"+case_number

    sql = """SELECT * FROM new_table ORDER BY DATE DESC;"""

    curs.execute(sql)

    res = curs.fetchall()

    f = open(file_name, 'w', newline='')
    wr = csv.writer(f)
    wr.writerow(concate_csv_list)

    for data in res:
        data_list = list(x for i, x in enumerate(data) if i > 0)
        wr.writerow(data_list)
    f.close()

    #Todo 정렬하여 개별 저장 만들고 아래 함수 옮겨야 함.
    sql = """ DROP TABLE new_table"""
    curs.execute(sql)


if "__main__":
    number = input('원하는 Case 숫자를 입력해주세요')
    get_case_and_make_table(number)


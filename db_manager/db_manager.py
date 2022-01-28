

import pymysql, csv

from secrete_dir.template import insert_code_dict, table_name_list, select_code_dict, insert_code_new_dict, concate_csv_title

from .db_template import *

float_dict = {
    table_name_list[0]: [],
    table_name_list[1]: [6],
    table_name_list[2]: [7],
    table_name_list[3]: []
}


class DB_manager():
    conn = None
    curs = None
    res = None
    sql = """"""

    def __init__(self, host, user, password, db_name):
        self.access_db(host, user, password, db_name)

    def access_db(self, host, user, password, db_name):
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()

    def insert_sql(self, text):
        self.sql = text

    def execute_current_query(self):
        self.curs.execute(self.sql)

    def execute_text_query(self, text):
        self.curs.execute(text)

    def insert_csv_data_to_table(self, file_name, table_name):
        float_list = float_dict[table_name]

        f = open(file_name, 'r')
        r = csv.reader(f)
        next(r)

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
            self.curs.execute(insert_code_dict[table_name], value_tuple)
        f.close()

    def add_data_to_concate_table(self, case_number, table_name):
        self.sql = select_code_dict[table_name]
        self.curs.execute(self.sql, (case_number))

        self.res = self.curs.fetchall()

        for data in self.res:
            value_tuple = tuple(x for i, x in enumerate(data) if i > 0)
            self.sql = insert_code_new_dict[table_name]
            self.curs.execute(self.sql, value_tuple)

    def make_case_csv_by_new_table(self, case_number):
        self.select_new_table_order_date()
        self.res = self.curs.fetchall()

        file_name = case_number + ".csv"
        f = open(file_name, 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(concate_csv_title)

        for data in self.res:
            data_list = list(x for i, x in enumerate(data) if i > 0)
            wr.writerow(data_list)
        f.close()

        self.rename_new_table_to_case_table(case_number)

    def make_csv_by_table(self, table_name):

        file_name = table_name + ".csv"
        f = open(file_name, 'w', newline='')
        wr = csv.writer(f)
        self.sql = """ SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME =(%s);"""
        self.curs.execute(self.sql, (table_name))
        self.res = self.curs.fetchall()
        column_name_list = []
        for i, data in enumerate(self.res):
            if i != 0:
                column_name_list.append(data[0])
        wr.writerow(column_name_list)

        self.sql = select_all_from + table_name
        self.execute_current_query()
        self.res = self.curs.fetchall()

        for data in self.res:
            data_list = list(x for i, x in enumerate(data) if i > 0)
            wr.writerow(data_list)
        f.close()

    def select_new_table_order_date(self):
        self.sql = select_all_from + """new_table """ + order_by_date_asc
        self.execute_current_query()


    def rename_new_table_to_case_table(self, case_number):
        self.sql = rename_table + """new_table """ + to + case_number.replace(" ", "") + query_over
        self.execute_current_query()

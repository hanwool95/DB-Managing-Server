import pymysql

from secrete_dir.password import mysql_password
from secrete_dir.template import select_case, concate_event_csv_list

import csv

class Condition_manager():
    case_number = ""
    curs = None
    res = None
    event = 0

    def __init__(self, curs, case_number):
        self.curs =curs
        self.case_number = case_number
        self.get_data_to_res()

    def get_data_to_res(self):
        sql = select_case(self.case_number)
        print(sql)
        self.curs.execute(sql)
        self.res = self.curs.fetchall()

    def data_to_csv(self):
        self.get_data_to_res()
        f = open(self.case_number+"_event.csv", 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(concate_event_csv_list)

        for data in self.res:
            data_list = list(x for i, x in enumerate(data) if i > 0)
            wr.writerow(data_list)
        f.close()

    def insert_event_condition(self):
        current_date = None
        for i, data in enumerate(self.res):
            if i == 0:
                current_date = self.init_date(str(data[concate_event_csv_list.index('Date')+1]))
            id = data[0]
            if data[concate_event_csv_list.index('dataType')+1] == "lab":
                pass
            else:
                if current_date != self.init_date(str(data[concate_event_csv_list.index('Date')+1])):
                    current_date = self.init_date(str(data[concate_event_csv_list.index('Date')+1]))
                    self.event += 1
            sql = """UPDATE """ + self.case_number + """ SET Event=""" + str(self.event) + """ """
            sql += """WHERE id=""" + str(id) +""";"""
            self.curs.execute(sql)

    def init_date(self, date):
        date = date[:10]
        return date


def calculate_event(number):

    conn = pymysql.connect(host="127.0.0.1", user='root', password=mysql_password, db='test_db', charset='utf8')
    curs = conn.cursor()

    case_number = "Case" + number

    add_event_column(case_number, curs)

    current_Case = Condition_manager(curs, case_number)

    current_Case.insert_event_condition()
    current_Case.data_to_csv()

def add_event_column(case_number, curs):
    sql = """ALTER TABLE """
    sql += case_number
    sql += """ ADD Event VARCHAR(5);"""
    curs.execute(sql)



if "__main__":
    number = input("원하시는 번호를 눌러주세요")
    calculate_event(number)

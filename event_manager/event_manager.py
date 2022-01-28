

import csv
from secrete_dir.template import *
from db_manager.db_template import *
from db_manager.db_manager import DB_manager


class Event_rule_manager(DB_manager):
    case_number = ""
    event_list = []
    event_table_name = ""

    def __init__(self, case_number, host, user, password, db_name):
        super().__init__(host, user, password, db_name)
        self.access_db(host, user, password, db_name)
        self.case_number = case_number
        self.event_table_name = case_number+"""_important"""
        self.get_data_to_res()

    def add_event_column(self):
        self.sql = """ALTER TABLE """ + self.case_number + add_event
        self.execute_current_query()

    def add_important_column(self):
        self.sql = """ALTER TABLE """ + self.case_number + add_event
        self.execute_current_query()

    def get_data_to_res(self):
        sql = select_case(self.case_number)
        self.execute_text_query(sql)
        self.res = self.curs.fetchall()

    def data_to_csv(self):
        self.get_data_to_res()
        f = open(self.case_number+"_event.csv", 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(concate_event_csv_title)

        for data in self.res:
            data_list = list(x for i, x in enumerate(data) if i > 0)
            wr.writerow(data_list)
        f.close()

    def insert_event_condition(self):
        current_date = None
        event = 0
        for i, data in enumerate(self.res):
            if i == 0:
                current_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))
            id = data[0]
            if data[concate_event_csv_title.index('dataType')+1] == "lab":
                pass
            else:
                if current_date != self.init_date(str(data[concate_event_csv_title.index('Date')+1])):
                    current_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))
                    event += 1
            sql = """UPDATE """ + self.case_number + """ SET Event=""" + str(event) + """ """
            sql += """WHERE id=""" + str(id) +""";"""
            self.execute_text_query(sql)

    def init_date(self, date):
        date = date[:10]
        return date

    def select_all_data_to_res(self):
        self.sql = select_all_from + self.case_number + query_over
        self.execute_current_query()
        self.res = self.curs.fetchall()

    def select_all_data_byDate_to_res(self):
        self.sql = select_all_from + self.case_number + " " + order_by_date_asc
        self.execute_current_query()
        self.res = self.curs.fetchall()

    def insert_important_event(self):
        self.select_all_data_byDate_to_res()

        event_num = 0

        cur_event = Event(event_num)
        for data in self.res:
            if str(data[Event_index]) != str(event_num):
                cur_event.is_important()
                self.event_list.append(cur_event)
                event_num = data[Event_index]
                cur_event = Event(event_num)
            else:
                cur_event.event_date = data[Date_index]

            if data[Type_index] == table_name_list[1]:
                if data[l_name_index] in l_condition_dict.keys():
                    cur_event.l = data[l_name_index] + "\n" + data[l_result_index]
            elif data[Type_index] == table_name_list[2]:
                if data[m_name_index] in m_condition_dict.keys():
                    cur_event.m = data[m_name_index] + "\n" + str(data[m_result_index])

    def create_event_table(self):
        self.sql = create_table
        self.sql += self.event_table_name + event_table_template
        self.execute_current_query()

    def insert_important_to_event_table(self):
        for event in self.event_list:
            self.sql = insert_into
            self.sql += self.event_table_name
            self.sql += insert_to_event_table
            self.curs.execute(self.sql, (event.event_num, event.event_date, event.l, event.m, event.important))


class Event():
    event_date = None
    event_num = 0
    d = None
    l = None
    m = None
    p = None
    important = False


    def __init__(self, num):
        self.event_num = num

    def is_important(self):
        if self.l or self.m:
            self.important = True

    def insert_all(self):
        self.insert_d()
        self.insert_l()
        self.insert_m()
        self.insert_p()

    def insert_d(self):
        pass

    def insert_l(self):
        pass

    def insert_m(self):
        pass

    def insert_p(self):
        pass
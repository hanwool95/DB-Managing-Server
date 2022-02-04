

import csv, copy
from secrete_dir.template import *
from db_manager.db_template import *
from db_manager.db_manager import DB_manager


class Event_rule_manager(DB_manager):

    def __init__(self, case_number, host, user, password, db_name):
        super().__init__(host, user, password, db_name)
        self.case_number = ""
        self.event_list = []
        self.event_table_name = ""

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
        before_lab = False
        for i, data in enumerate(self.res):
            if i == 0:
                current_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))

            id = data[0]
            compared_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))
            if data[concate_event_csv_title.index('dataType')+1] == table_name_list[1] or \
                    data[concate_event_csv_title.index('dataType')+1] == table_name_list[3]:
                if current_date == compared_date:
                    pass
                else:
                    if before_lab:
                        pass
                    else:
                        before_lab = True
                        current_date = compared_date
                        event += 1
            else:
                if before_lab:
                    current_date = compared_date
                    before_lab = False
                else:
                    if current_date != compared_date:
                        current_date = compared_date
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
                prev_m = copy.deepcopy(cur_event.m)
                cur_event = Event(event_num, prev_m)
            else:
                cur_event.event_date = data[Date_index]

            if data[Type_index] == table_name_list[1]:
                if data[l_name_index] in l_condition_dict.keys():
                    cur_event.l_name.append(data[l_name_index])
                    cur_event.l_result.append(data[l_result_index])
            elif data[Type_index] == table_name_list[2]:
                cur_event.m.append(data[m_name_index] + " " + str(data[m_result_index]))
        cur_event.is_important()
        self.event_list.append(cur_event)

    def create_event_table(self):
        self.sql = create_table
        self.sql += self.event_table_name + event_table_template
        self.execute_current_query()

    def insert_important_to_event_table(self):
        for event in self.event_list:
            self.sql = insert_into
            self.sql += self.event_table_name
            self.sql += insert_to_event_table
            self.curs.execute(self.sql, (event.event_num, event.event_date, event.important_l,
                                         event.important_m, event.important))


class Event():
    def __init__(self, num, prev_m=None):
        self.event_date = None
        self.event_num = num
        self.prev_m = prev_m
        self.d = None
        self.l_name = []
        self.l_result = []
        self.m = []
        self.p = None
        self.important = False
        self.important_m = ""
        self.important_l = ""

    def is_important(self):
        if len(self.l_name) != 0:
            local_important = False
            for i, name in enumerate(self.l_name):
                if l_condition_dict[name][0] == "str":
                    if l_condition_dict[name][1] not in self.l_result[i]:
                        self.important = True
                        local_important = True
                elif l_condition_dict[name][0] == "float":
                    result = self.l_result[i]
                    for exception in except_list:
                        result = result.replace(exception, "")
                    result = float(result)
                    if (result < l_condition_dict[name][1][0]) or \
                            (result > l_condition_dict[name][1][1]):
                        self.important = True
                        local_important = True
                if local_important:
                    self.important_l += name + " " + self.l_result[i] + "\n"
                    local_important = False
            if self.important:
                self.important_l = self.important_l[:-1]

        if self.m != self.prev_m:
            self.important = True
            for m_data in self.m:
                self.important_m += m_data + "\n"
            self.important_m = self.important_m[:-1]

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
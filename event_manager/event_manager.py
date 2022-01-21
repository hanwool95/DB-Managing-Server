

from secrete_dir.template import select_case, concate_event_csv_title

# Todo 문서화, 이슈 뽑아내기 위해 필요한 정상치 반영. (Important rule)
#  Event가 하나의 객체이고, (Event rule -> Event별 객체 생성)

class Event():
    d = None
    l = None
    m = None
    p = None
    important = {}

    def is_important(self):
        pass

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


class Event_rule_manager():
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
        wr.writerow(concate_event_csv_title)

        for data in self.res:
            data_list = list(x for i, x in enumerate(data) if i > 0)
            wr.writerow(data_list)
        f.close()

    def insert_event_condition(self):
        current_date = None
        for i, data in enumerate(self.res):
            if i == 0:
                current_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))
            id = data[0]
            if data[concate_event_csv_title.index('dataType')+1] == "lab":
                pass
            else:
                if current_date != self.init_date(str(data[concate_event_csv_title.index('Date')+1])):
                    current_date = self.init_date(str(data[concate_event_csv_title.index('Date')+1]))
                    self.event += 1
            sql = """UPDATE """ + self.case_number + """ SET Event=""" + str(self.event) + """ """
            sql += """WHERE id=""" + str(id) +""";"""
            self.curs.execute(sql)

    def init_date(self, date):
        date = date[:10]
        return date
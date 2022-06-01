from manager.models import Dx, Fx, Lab, Med, Px, Event
from django.forms.models import model_to_dict
import datetime

class Rule:
    def __init__(self, case_number: str):
        self.model_dict = {'Dx': Dx, 'Fx': Fx, 'Lab': Lab, 'Med': Med, 'Px': Px}
        self.__case_number = case_number
        self.event = Event
        self.queries = self.__set_queries()
        self.__sort_queries_by_date()
        self.important_list = []

    def __set_queries(self) -> list:
        result_query = []
        for model_name, model in self.model_dict.items():
            queries = model.objects.filter(number=self.__case_number).values()
            for query in queries:
                self.__add_model_name_in_query(model_name, query)
            result_query += queries
        return result_query

    @staticmethod
    def __add_model_name_in_query(model_name: str, query: dict):
        query['model'] = model_name

    def add_event_column(self, date: str, event_num: int, important: bool):
        self.event(number=self.__case_number, date=date, event_num=event_num, important=important).save()

    @staticmethod
    def init_event():
        records = Event.objects.all()
        records.delete()

    def __sort_queries_by_date(self):
        self.queries.sort(key=lambda x: x['date'])

    def insert_event_condition(self):
        current_date = None
        event = 0
        before_lab = False
        for i, query in enumerate(self.queries):
            if i == 0:
                current_date = self.init_date(query['date'])

            compared_date = self.init_date(query['date'])

            if query['model'] is 'Lab' or query['model'] is 'px':
                if current_date != compared_date and not before_lab:
                    before_lab = True
                    current_date = compared_date
                    self.add_event_column(date=current_date, event_num=event, important=False)
                    event += 1
            else:
                if before_lab:
                    current_date = compared_date
                    before_lab = False
                else:
                    if current_date != compared_date:
                        current_date = compared_date
                        self.add_event_column(date=current_date, event_num=event, important=False)
                        event += 1

    @staticmethod
    def init_date(date):
        date = str(date)[:10]
        return date

    def get_event_queries(self):
        return Event.objects.filter(number=self.__case_number).values()

    def create_important_event(self):
        event_queries = self.get_event_queries()
        cur_event = Important(0)

        for i, event_query in enumerate(event_queries):
            event_num = event_query['event_num']
            cur_date = event_query['date']
            cur_event.event_date = cur_date
            information_queries = self.__get_all_queries_by_date(cur_date)

            for information_query in information_queries:
                if information_query['model'] is 'Lab' and information_query['test_name'] in Condition.l_condition_dict.keys():
                    cur_event.l_name.append(information_query['test_name'])
                    cur_event.l_result.append(information_query['result_total'])

                elif information_query['model'] is 'Med':
                    cur_event.m.append(information_query['name_ingredient'] + " " + str(information_query['prescription']))

            cur_event.is_important()
            self.important_list.append(cur_event)

            cur_event = Important(event_num+1, cur_event)

    def __get_all_queries_by_date(self, date: datetime) -> list:
        result_query = []
        for model_name, model in self.model_dict.items():
            queries = model.objects.all().values()
            for query in queries:
                if self.init_date(query['date']) == self.init_date(date):
                    self.__add_model_name_in_query(model_name, query)
                    result_query.append(query)
        return result_query

    def insert_important_event_table(self):
        for important in self.important_list:
            cur_event = Event.objects.filter(number=self.__case_number, date=important.event_date)[0]
            cur_event.important = important.important
            cur_event.save()



class Important:
    def __init__(self, num, prev_Event=None):
        self.event_date = None
        self.event_num = num
        self.prev_Event = prev_Event
        self.prev_m = []
        if self.prev_Event:
            while self.prev_Event.m == []:
                self.prev_Event = self.prev_Event.prev_Event
                if not self.prev_Event:
                    break
            if self.prev_Event:
                self.prev_m = self.prev_Event.m
        self.d = None
        self.l_name = []
        self.l_result = []
        self.m = []
        self.p = None
        self.important = False
        self.important_m = ""
        self.important_l = ""

    def is_important(self):
        l_condition_dict = Condition.l_condition_dict
        except_list = Condition.except_list

        if len(self.l_name) != 0:
            local_important = False
            for i, name in enumerate(self.l_name):
                if l_condition_dict[name][0] == "str":
                    if l_condition_dict[name][1] not in self.l_result[i].lower():
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


class Condition:
    l_condition_dict = {'Foot Both AP': ('str', 'no significant bony abnormality'),
                        'Foot Both Obl': ('str', 'no significant bony abnormality'),
                        'Foot Both Lat': ('str', 'no significant bony abnormality'),
                        'Uric Acid(검사24시간가능)': ('float', (3.0, 7.0)),
                        'Creatinine(검사24시간가능)': ('float', (0.7, 1.4)),
                        'BUN(검사24시간가능)': ('float', (10, 26)),
                        'GOT (AST)(검사24시간가능)': ('float', (1, 40)),
                        'GPT (ALT)(검사24시간가능)': ('float', (1, 40)),
                        'Cholesterol(검사24시간가능)': ('float', (0, 240)),
                        'Triglyceride (TG)(검사24시간가능)': ('float', (0, 200)),
                        'HDL-Cholesterol(검사24시간가능)': ('float', (35, 55)),
                        'LDL-Cholesterol(검사24시간가능)': ('float', (0, 130)),
                        'LDL cholesterol (계산식)': ('float', (0, 130)),
                        'ESR(검사24시간가능)': ('float', (0, 20)),
                        'hs-CRP quantitation(검사24시간가능)': ('float', (0, 0.5)),
                        'WBC(검사24시간가능)': ('float', (4, 10)),
                        'Hb A1c': ('float', (float("-inf"), 5.6))}

    except_list = [">", "<"]

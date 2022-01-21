

from secrete_dir.db_info import host, user, mysql_password, db
from db_manager.db_manager import DB_manager
from event_manager.event_manager import Event_rule_manager

def calculate_event(number):

    dbm = DB_manager(host, user, mysql_password, db)
    case_number = "Case" + number
    dbm.add_event_column(case_number)

    current_Case = Event_rule_manager(dbm.curs, case_number)

    current_Case.insert_event_condition()
    current_Case.data_to_csv()


if "__main__":
    number = input("원하시는 번호를 눌러주세요")
    calculate_event(number)

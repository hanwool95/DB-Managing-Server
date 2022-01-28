

from secrete_dir.db_info import host, user, mysql_password, db
from event_manager.event_manager import Event_rule_manager

def calculate_event(number):

    case_number = "Case" + number

    current_Case = Event_rule_manager(case_number, host, user, mysql_password, db)
    current_Case.add_event_column()

    current_Case.insert_event_condition()
    current_Case.data_to_csv()


if __name__ == "__main__":
    number = input("원하시는 번호를 눌러주세요")
    calculate_event(number)

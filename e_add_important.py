
from secrete_dir.db_info import host, user, mysql_password, db
from event_manager.event_manager import Event_rule_manager


def add_important(number):
    case_number = "Case" + number
    current_Case = Event_rule_manager(case_number, host, user, mysql_password, db)
    current_Case.insert_important_event()
    current_Case.create_event_table()
    current_Case.insert_important_to_event_table()
    current_Case.make_csv_by_table(current_Case.event_table_name)


if "__main__":
    number = input("원하시는 번호를 눌러주세요")
    add_important(number)
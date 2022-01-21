

from secrete_dir.template import concate_table, table_name_list
from secrete_dir.db_info import host, user, mysql_password, db
from db_manager.db_manager import DB_manager
from secrete_dir.password import mysql_password


def get_case_and_make_table(number):
    dbm = DB_manager(host, user, mysql_password, db)
    case_number = "Case "+number
    dbm.execute_text_query(concate_table)

    for table_name in table_name_list:
        dbm.add_data_to_concate_table(case_number, table_name)

    dbm.make_case_csv_by_new_table(case_number)



if "__main__":
    number = input('원하는 Case 숫자를 입력해주세요')
    get_case_and_make_table(number)


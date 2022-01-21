

import csv

from secrete_dir.db_info import host, user, mysql_password, db
from db_manager.db_manager import DB_manager
from secrete_dir.template import table_name_list


def Data_to_DB(table_name):

    dbm = DB_manager(host, user, mysql_password, db)
    dbm.conn.commit()
    dbm.insert_csv_data_to_table('secrete_dir/' + table_name + '.csv', table_name)

if "__main__":
    for code in table_name_list:
        Data_to_DB(code)



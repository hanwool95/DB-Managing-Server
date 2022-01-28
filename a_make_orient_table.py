

from secrete_dir.db_info import host, user, mysql_password, db
from secrete_dir.template import orient_table
from db_manager.db_manager import DB_manager

if __name__ == "__main__":
    dbm = DB_manager(host, user, mysql_password, db)
    for case in orient_table:
        dbm.execute_text_query(case)
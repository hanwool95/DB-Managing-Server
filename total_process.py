

from c_Get_Data_by_case import *
from d_output_event import *
from e_add_important import *

import time

if __name__ == "__main__":
    # number = input("원하시는 번호를 눌러주세요")
    # get_case_and_make_table(number)
    # time.sleep(1)
    # calculate_event(number)
    # time.sleep(1)
    # add_important(number)
    start = 1
    for i in range(27):
        number = str(start+i)
        print(number)
        get_case_and_make_table(number)
        calculate_event(number)
        add_important(number)


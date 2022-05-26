import csv
from .schema import schema_dict
from manager.models import *
import sys
mod = sys.modules[__name__]

class File_Handler:
    def __init__(self):
        self.__filename = ""

    def upload_file(self, file):
        self.__filename = str(file)

        with open('static/'+self.__filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    def select_file_name(self, file_name):
        self.__filename = file_name

    def insert_db(self):
        with open('static/'+self.__filename, 'r') as f:
            r = csv.reader(f)
            # schema = schema_dict[self.__filename]
            next(r)
            db_object = self.select_db_object()

            for line in r:
                self.insert_dx_line(db_object, line)

    def select_db_object(self):
        if self.__filename == 'd.csv':
            return Dx
        elif self.__filename == 'l.csv':
            return Lab
        elif self.__filename == 'm.csv':
            return Med
        else:
            return Px

    def insert_dx_line(self, dx, line):
        dx(number=line[0], sex=line[1], birth=line[2], department=line[3], date=line[4], first_date=line[5],
                diagnostic_code=line[6], diagnostic_name=line[7], icd10_code=line[8]).save()


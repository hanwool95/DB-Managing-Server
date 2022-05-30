import csv
from .schema import schema_dict
from manager.models import *
import sys
mod = sys.modules[__name__]

class FileHandler:
    def __init__(self):
        self.__filename = ""

    def get_filename(self) -> str:
        return self.__filename

    def upload_file(self, file):
        self.__filename = str(file)
        print(self.__filename)

        with open('static/'+self.__filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)


class DbHandler:

    def __init__(self):
        self.__filename = ""

    def select_file_name(self, file_name: str):
        self.__filename = file_name

    def __initialize_db(self, db: object):
        records = db.objects.all()
        records.delete()

    def insert_db(self):
        with open('static/'+self.__filename, 'r') as f:
            r = csv.reader(f)
            next(r)
            db_object = self.__select_db_object()
            self.__initialize_db(db_object)
            for line in r:
                self.__insert_line(db_object, line)

    def __select_db_object(self) -> object:
        if self.__filename == 'd.csv':
            return Dx
        elif self.__filename == 'l.csv':
            return Lab
        elif self.__filename == 'm.csv':
            return Med
        else:
            return Px

    def __insert_line(self, db_object: object, line: list):
        if self.__filename == 'd.csv':
            return self.__insert_dx_line(db_object, line)
        elif self.__filename == 'l.csv':
            return self.__insert_lab_line(db_object, line)
        elif self.__filename == 'm.csv':
            return self.__insert_med_line(db_object, line)
        else:
            return self.__insert_px_line(db_object, line)

    def __insert_dx_line(self, dx: Dx, line: list):
        dx(number=line[0], sex=line[1], birth=line[2], department=line[3], date=line[4], first_date=line[5],
                diagnostic_code=line[6], diagnostic_name=line[7], icd10_code=line[8]).save()

    def __insert_lab_line(self, lab: Lab, line: list):
        lab(number=line[0], sex=line[1], birth=line[2], department=line[3], date=line[4], test_name=line[5],
                result_numerical=float(line[6]) if line[6] else None, result_negpos=line[7], result_total=line[8]).save()

    def __insert_med_line(self, med: Med, line: list):
        print(line)
        med(number=line[0], sex=line[1], birth=line[2], department=line[3], date=line[4], name_ingredient=line[5],
                name_normal=line[6], prescription=line[7] if line[7] else None).save()


    def __insert_px_line(self, px: Px, line: list):
        px(number=line[0], sex=line[1], birth=line[2], date=line[3], format_name=line[4], format_content=line[5]).save()



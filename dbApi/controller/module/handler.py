import csv
from .schema import schema_dict
from manager.models import *
import sys
mod = sys.modules[__name__]

class Db:
    dx = Dx
    lab = Lab
    med = Med
    fx = Fx
    px = Px

    def get_unique_numbers(self) -> list:
        all_dx = self.dx.objects.all()
        number_dict = all_dx.values('number').distinct()
        unique_numbers = []
        for number_query in number_dict:
            unique_numbers.append(number_query['number'])
        return unique_numbers


class File_Handler:
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


class Db_Handler:

    def __init__(self):
        self.__filename = ""

    def select_file_name(self, file_name: str):
        self.__filename = file_name

    @staticmethod
    def __initialize_db(db: object):
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
        elif self.__filename == "f.csv":
            return Fx
        else:
            return Px

    def __insert_line(self, db_object: object, line: list):
        if self.__filename == 'd.csv':
            return self.__insert_dx_line(db_object, line)
        elif self.__filename == 'l.csv':
            return self.__insert_lab_line(db_object, line)
        elif self.__filename == 'm.csv':
            return self.__insert_med_line(db_object, line)
        elif self.__filename == 'f.csv':
            return self.__insert_fx_line(db_object, line)
        else:
            return self.__insert_px_line(db_object, line)

    @staticmethod
    def __insert_dx_line(dx: Dx, line: list):
        dx(
            number=line[0],
            sex=line[1],
            birth=line[2],
            department=line[3],
            date=line[4],
            first_date=line[5],
            diagnostic_code=line[6],
            diagnostic_name=line[7],
            icd10_code=line[8]
        ).save()

    @staticmethod
    def __insert_lab_line(lab: Lab, line: list):
        lab(
            number=line[0],
            sex=line[1],
            birth=line[2],
            department=line[3],
            date=line[4],
            test_name=line[5],
            result_numerical=float(line[6]) if line[6] else None,
            result_negpos=line[7],
            result_total=line[8]
        ).save()

    @staticmethod
    def __insert_med_line(med: Med, line: list):
        med(
            number=line[0],
            sex=line[1],
            birth=line[2],
            department=line[3],
            date=line[4],
            name_ingredient=line[5],
            name_normal=line[6],
            prescription=line[7] if line[7] else None
        ).save()

    @staticmethod
    def __insert_px_line(px: Px, line: list):
        px(
            number=line[0],
            sex=line[1],
            birth=line[2],
            date=line[3],
            format_name=line[4],
            format_content=line[5]
        ).save()

    @staticmethod
    def __insert_fx_line(fx: Fx, line: list):
        fx(
            number=line[0],
            sex=line[1],
            birth=line[2],
            department=line[3],
            date=line[4],
            format_name=line[5],
            format_content=line[6]
        ).save()



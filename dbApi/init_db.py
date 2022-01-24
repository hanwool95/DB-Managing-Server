import csv, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbApi.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from gql.models import Ddata, Mdata, Ldata, Pdata
def get_Ddata():
    f = open('csv_data/d.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for i, line in enumerate(rdr):
        Ddata(client_num=line[0], gender=line[1], birth=line[2], field=line[3], date=line[4],
              first_date=line[5], d_code=line[6], d_name=line[7], d_scode=line[8]).save()


def get_Mdata():
    f = open('csv_data/m.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for i, line in enumerate(rdr):
        Mdata(client_num=line[0], gender=line[1], birth=line[2], field=line[3], date=line[4],
              m_iname=line[5], m_oname=line[6], m_result=float(line[7]) if line[7] != "" else None).save()


def get_Ldata():
    f = open('csv_data/l.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for i, line in enumerate(rdr):
        Ldata(client_num=line[0], gender=line[1], birth=line[2], field=line[3], date=line[4],
              l_name=line[5], l_float=float(line[6]) if line[6] != "" else None,
              l_pm=line[7], l_result=line[8]).save()


def get_Pdata():
    f = open('csv_data/p.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for i, line in enumerate(rdr):
        Pdata(client_num=line[0], gender=line[1], birth=line[2], date=line[3],
              p_name=line[4], p_result=line[5]).save()


if __name__ == "__main__":
    get_Ddata()
    print("complete D")
    get_Mdata()
    print("complete M")
    get_Ldata()
    print("complete L")
    get_Pdata()
    print("complete P")


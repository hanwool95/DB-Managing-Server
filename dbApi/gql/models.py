from django.db import models

# Create your models here.

class Ddata(models.Model):
    client_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=12)
    field = models.CharField(max_length=20)
    date = models.DateField()
    first_date = models.DateField()
    d_code = models.CharField(max_length=10)
    d_name = models.CharField(max_length=50)
    d_scode = models.CharField(max_length=10)


class Mdata(models.Model):
    client_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=12)
    field = models.CharField(max_length=20)
    date = models.DateField()
    m_iname = models.CharField(max_length=5000)
    m_oname = models.CharField(max_length=5000)
    m_result = models.IntegerField()

class Ldata(models.Model):
    client_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=12)
    field = models.CharField(max_length=20)
    date = models.DateTimeField()
    l_name = models.CharField(max_length=5000)
    l_float = models.FloatField(null=True)
    l_pm = models.CharField(max_length=5)
    l_result = models.CharField(max_length=5000)


class Pdata(models.Model):
    client_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=12)
    date = models.DateTimeField()
    p_name = models.CharField(max_length=100)
    p_result = models.CharField(max_length=1000)

class ConcateData(models.Model):
    client_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=12)
    category = models.CharField(max_length=10)
    date = models.DateTimeField()
    first_date = models.DateField()
    d_code = models.CharField(max_length=10)
    d_name = models.CharField(max_length=50)
    d_scode = models.CharField(max_length=10)
    m_iname = models.CharField(max_length=5000)
    m_oname = models.CharField(max_length=5000)
    m_result = models.IntegerField()
    l_name = models.CharField(max_length=5000)
    l_float = models.FloatField(null=True)
    l_pm = models.CharField(max_length=5)
    l_result = models.CharField(max_length=5000)
    p_name = models.CharField(max_length=100)
    p_result = models.CharField(max_length=1000)
    event = models.CharField(max_length=5)


class EventData(models.Model):
    event_num = models.IntegerField()
    date = models.DateTimeField()
    d_im = models.CharField(max_length=5000)
    m_im = models.CharField(max_length=5000)
    l_im = models.CharField(max_length=5000)
    p_im = models.CharField(max_length=5000)
    important = models.BooleanField()
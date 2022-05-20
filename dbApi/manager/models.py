# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Case1(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.Field(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case1'


class Case10(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case10'


class Case10Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case10_important'


class Case11(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case11'


class Case11Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case11_important'


class Case12(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case12'


class Case12Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case12_important'


class Case13(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case13'


class Case13Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case13_important'


class Case14(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case14'


class Case14Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case14_important'


class Case15(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case15'


class Case15Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case15_important'


class Case16(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case16'


class Case16Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case16_important'


class Case17(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case17'


class Case17Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case17_important'


class Case18(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case18'


class Case18Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case18_important'


class Case19(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case19'


class Case19Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case19_important'


class Case1Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case1_important'


class Case2(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case2'


class Case20(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case20'


class Case20Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case20_important'


class Case21(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case21'


class Case21Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case21_important'


class Case22(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case22'


class Case22Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case22_important'


class Case23(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case23'


class Case23Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case23_important'


class Case24(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case24'


class Case24Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case24_important'


class Case25(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case25'


class Case25Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case25_important'


class Case26(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case26'


class Case26Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case26_important'


class Case27(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case27'


class Case27Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case27_important'


class Case2Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case2_important'


class Case3(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case3'


class Case3Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case3_important'


class Case4(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case4'


class Case4Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case4_important'


class Case5(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case5'


class Case5Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case5_important'


class Case6(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case6'


class Case6Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case6_important'


class Case7(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case7'


class Case7Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case7_important'


class Case8(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case8'


class Case8Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case8_important'


class Case9(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.FloatField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)
    event = models.CharField(db_column='Event', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Case9'


class Case9Important(models.Model):
    event_num = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lab이상 = models.CharField(max_length=5000, blank=True, null=True)
    med이상 = models.CharField(max_length=5000, blank=True, null=True)
    ctotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Case9_important'


class Casecccccc(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    datatype = models.CharField(db_column='dataType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.IntegerField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Casecccccc'


class Dx(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    진단일자 = models.DateField(blank=True, null=True)
    첫진단일자 = models.DateField(blank=True, null=True)
    진단코드 = models.CharField(max_length=10, blank=True, null=True)
    진단명 = models.CharField(max_length=50, blank=True, null=True)
    icd10코드 = models.CharField(db_column='ICD10코드', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dx'


class Fx(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    서식작성일 = models.DateField(blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fx'


class Lab(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    검사시행일 = models.DateTimeField(blank=True, null=True)
    검사명 = models.CharField(max_length=5000, blank=True, null=True)
    검사결과수치값 = models.FloatField(blank=True, null=True)
    검사결과음성양성 = models.CharField(max_length=5, blank=True, null=True)
    검사결과 = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab'


class Med(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    수진진료과 = models.CharField(max_length=20, blank=True, null=True)
    약품처방일 = models.DateField(blank=True, null=True)
    약품명성분명 = models.CharField(max_length=5000, blank=True, null=True)
    약품명일반명 = models.CharField(max_length=5000, blank=True, null=True)
    number_1일처방량 = models.IntegerField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'med'


class Px(models.Model):
    환자번호a = models.CharField(db_column='환자번호A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    성별 = models.CharField(max_length=2, blank=True, null=True)
    생년월일 = models.CharField(max_length=12, blank=True, null=True)
    서식작성일 = models.DateField(blank=True, null=True)
    서식명 = models.CharField(max_length=100, blank=True, null=True)
    서식내용 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'px'

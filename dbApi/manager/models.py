# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dx(models.Model):
    number = models.TextField(db_column='환자번호A', max_length=10, blank=True, null=True)
    sex = models.TextField(db_column='성별', max_length=2, blank=True, null=True)
    birth = models.TextField(db_column='생년월일', max_length=12, blank=True, null=True)
    department = models.TextField(db_column='수진진료과', max_length=20, blank=True, null=True)
    date = models.DateField(db_column='진단일자', blank=True, null=True)
    first_date = models.DateField(db_column='첫진단일자', blank=True, null=True)
    diagnostic_code = models.TextField(db_column='진단코드', max_length=10, blank=True, null=True)
    diagnostic_name = models.TextField(db_column='진단명', max_length=50, blank=True, null=True)
    icd10_code = models.TextField(db_column='ICD10코드', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dx'


class Fx(models.Model):
    number = models.TextField(db_column='환자번호A', max_length=10, blank=True, null=True)
    sex = models.TextField(db_column='성별', max_length=2, blank=True, null=True)
    birth = models.TextField(db_column='생년월일', max_length=12, blank=True, null=True)
    department = models.TextField(db_column='수진진료과', max_length=20, blank=True, null=True)
    date = models.DateField(db_column="서식작성일", blank=True, null=True)
    format_name = models.TextField(db_column="서식명", max_length=100, blank=True, null=True)
    format_content = models.TextField(db_column="서식내용", max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fx'


class Lab(models.Model):
    number = models.TextField(db_column='환자번호A', max_length=10, blank=True, null=True)
    sex = models.TextField(db_column='성별', max_length=2, blank=True, null=True)
    birth = models.TextField(db_column='생년월일', max_length=12, blank=True, null=True)
    department = models.TextField(db_column='수진진료과', max_length=20, blank=True, null=True)
    date = models.DateTimeField(db_column="검사시행일", blank=True, null=True)
    test_name = models.TextField(db_column="검사명", max_length=5000, blank=True, null=True)
    result_numerical = models.FloatField(db_column="검사결과수치값", blank=True, null=True)
    result_negpos = models.TextField(db_column="검사결과음성양성", max_length=5, blank=True, null=True)
    result_total = models.TextField(db_column="검사결과", max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab'


class Med(models.Model):
    number = models.TextField(db_column='환자번호A', max_length=10, blank=True, null=True)
    sex = models.TextField(db_column='성별', max_length=2, blank=True, null=True)
    birth = models.TextField(db_column='생년월일', max_length=12, blank=True, null=True)
    department = models.TextField(db_column='수진진료과', max_length=20, blank=True, null=True)
    date = models.DateField(db_column="약품처방일", blank=True, null=True)
    name_ingredient = models.TextField(db_column="약품명성분명", max_length=5000, blank=True, null=True)
    name_normal = models.TextField(db_column="약품명일반명", max_length=5000, blank=True, null=True)
    prescription = models.IntegerField(db_column='1일처방량', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'med'


class Px(models.Model):
    number = models.TextField(db_column='환자번호A', max_length=10, blank=True, null=True)
    sex = models.TextField(db_column='성별', max_length=2, blank=True, null=True)
    birth = models.TextField(db_column='생년월일', max_length=12, blank=True, null=True)
    date = models.DateField(db_column="서식작성일", blank=True, null=True)
    format_name = models.TextField(db_column="서식명", max_length=100, blank=True, null=True)
    format_content = models.TextField(db_column="서식내용", max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'px'

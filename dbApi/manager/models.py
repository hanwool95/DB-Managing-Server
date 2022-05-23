# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dx(models.Model):
    number = models.TextField(max_length=10, blank=True, null=True)
    sex = models.TextField(max_length=2, blank=True, null=True)
    birth = models.TextField( max_length=12, blank=True, null=True)
    department = models.TextField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    first_date = models.DateField(blank=True, null=True)
    diagnostic_code = models.TextField(max_length=10, blank=True, null=True)
    diagnostic_name = models.TextField(max_length=50, blank=True, null=True)
    icd10_code = models.TextField(max_length=10, blank=True, null=True)



class Fx(models.Model):
    number = models.TextField(max_length=10, blank=True, null=True)
    sex = models.TextField(max_length=2, blank=True, null=True)
    birth = models.TextField(max_length=12, blank=True, null=True)
    department = models.TextField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    format_name = models.TextField(max_length=100, blank=True, null=True)
    format_content = models.TextField(max_length=1000, blank=True, null=True)


class Lab(models.Model):
    number = models.TextField(max_length=10, blank=True, null=True)
    sex = models.TextField(max_length=2, blank=True, null=True)
    birth = models.TextField(max_length=12, blank=True, null=True)
    department = models.TextField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    test_name = models.TextField(max_length=5000, blank=True, null=True)
    result_numerical = models.FloatField(blank=True, null=True)
    result_negpos = models.TextField(max_length=5, blank=True, null=True)
    result_total = models.TextField(max_length=5000, blank=True, null=True)



class Med(models.Model):
    number = models.TextField(max_length=10, blank=True, null=True)
    sex = models.TextField(max_length=2, blank=True, null=True)
    birth = models.TextField(max_length=12, blank=True, null=True)
    department = models.TextField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    name_ingredient = models.TextField(max_length=5000, blank=True, null=True)
    name_normal = models.TextField(max_length=5000, blank=True, null=True)
    prescription = models.IntegerField(blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.


class Px(models.Model):
    number = models.TextField(max_length=10, blank=True, null=True)
    sex = models.TextField(max_length=2, blank=True, null=True)
    birth = models.TextField(max_length=12, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    format_name = models.TextField(max_length=100, blank=True, null=True)
    format_content = models.TextField(max_length=1000, blank=True, null=True)


from django.test import TestCase
from .module.rule import *

# Create your tests here.


rule = Rule("Case 1")
for i, query in enumerate(rule.queries):
    date = query['date']
    event_num = i
    important = True
    rule.add_event_column(date=date, event_num=event_num, important=important)

rule.init_event()
rule.insert_event_condition()
rule.create_important_event()
rule.insert_important_event_table()
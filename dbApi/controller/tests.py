from django.test import TestCase
from .module.rule import *

# Create your tests here.


rule = Rule("Case 2")
rule.init_event()
rule.insert_event_condition()
rule.create_important_event()
rule.insert_important_event_table()
for important in rule.important_list:
    print(important.event_date)
    print(important.important)
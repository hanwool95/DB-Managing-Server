from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm

from .module.handler import File_Handler, Db_Handler, Db
from .module.rule import Rule

from manager.models import Event
import csv

import os


def index(request):
    static_file_list = os.listdir('static')

    return render(request, 'controller/index.html', {'static_files': static_file_list})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_handler = File_Handler()
            file_handler.upload_file(request.FILES['file'])

            return HttpResponseRedirect('/controller')
        else:
            print("un valid")
    else:
        form = UploadFileForm()

    return render(request, 'controller/upload.html', {'upload_form': form})


def insert_file(request, file_name):
    db_handler = Db_Handler()
    db_handler.select_file_name(file_name)
    db_handler.insert_db()
    return HttpResponseRedirect('/controller')

def download_event_csv_file(request, case_num):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="important.csv"'},
    )

    writer = csv.writer(response)

    events = Event.objects.filter(number="Case "+str(case_num))

    for event in events:
        row = [event.date, event.event_num, event.important]
        writer.writerow(row)

    return response



def event(request):
    db = Db()
    unique_numbers = db.get_unique_numbers()

    for number in unique_numbers:
        rule = Rule(number)
        rule.init_event()
        rule.insert_event_condition()
        rule.create_important_event()
        rule.insert_important_event_table()

    return HttpResponseRedirect('/controller')
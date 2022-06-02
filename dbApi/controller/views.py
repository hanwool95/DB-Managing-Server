from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .module.handler import File_Handler, Db_Handler, Db
from .module.rule import Rule
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
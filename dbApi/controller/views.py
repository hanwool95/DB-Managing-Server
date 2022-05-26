from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .module.file_handler import File_Handler
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
    file_handler = File_Handler()
    file_handler.select_file_name(file_name)
    file_handler.insert_db()
    return HttpResponseRedirect('/controller')

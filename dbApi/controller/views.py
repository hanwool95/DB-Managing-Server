from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .file_handler import File_Handler

def index(request):
    return render(request, 'controller/index.html')


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            File_Handler(request.FILES['file'])
            return HttpResponseRedirect('/controller')
        else:
            print("un valid")
    else:
        form = UploadFileForm()

    return render(request, 'controller/upload.html', {'upload_form': form})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse

from .cipher_api.parser import Parser

from .models import File
from .forms import DeleteFileForm, UploadFileForm
# from .cipherAPI.Cipher import Cipher
from django.core.files.storage import FileSystemStorage
import os

class IndexView(generic.ListView):
    template_name = 'filemanager/index.html'
    context_object_name = 'file_list'

    def get_queryset(self):
        return File.objects.all()

class FileView(generic.DetailView):
    model = File
    template_name = 'filemanager/file.html'
    slug_field = 'name'

def handleFile(request):
    file_name = request.FILES['filename'].name
    file_contents = request.FILES['filename'].read()
    # file_to_encrypt = Cipher(request.FILES['filename'].temporary_file_path, 3)
    textParser = Parser(file_contents, 3)
    print(textParser.getEncryptedText())
    new_file = File(name=file_name, contents=file_contents.decode('utf-8'))
    new_file.save()
    return HttpResponseRedirect(reverse('filemanager:index'))

def removeFile(request):
    file_name = request.POST.get('name', '')
    file_to_delete = File.objects.get(name=file_name)
    file_to_delete.delete()
    return HttpResponseRedirect(reverse('filemanager:index'))
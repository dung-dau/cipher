from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .cipher_api.cipher.cipher import Cipher

from .models import File

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
    file_contents = request.FILES['filename'].read().decode('utf-8')
    textParser = Cipher(str(file_contents), 3)
    new_file = File(name=file_name, contents=textParser.getEncryptedText())
    new_file.save()
    return HttpResponseRedirect(reverse('filemanager:index'))

def removeFile(request):
    file_name = request.POST.get('name', '')
    file_to_delete = File.objects.get(name=file_name)
    file_to_delete.delete()
    return HttpResponseRedirect(reverse('filemanager:index'))
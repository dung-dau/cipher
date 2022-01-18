from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse

from .models import File
from .forms import UploadFileForm

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
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         with open('some/file/name.txt', 'wb+') as destination:
    #             for chunk in f.chunks():
    #                 destination.write(chunk)
    #         return HttpResponseRedirect('filemanager/')
    # else:
    #     form = UploadFileForm()
    # return render(request, 'filemanager/index.html', {'form': form})
    file_name = request.FILES['filename'].name
    file_contents = request.FILES['filename'].read()
    new_file = File(name=file_name, contents=file_contents)
    new_file.save()
    return HttpResponseRedirect(reverse('index'))

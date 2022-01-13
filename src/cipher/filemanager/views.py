from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic import DetailView

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

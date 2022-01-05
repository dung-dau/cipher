from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import File


def index(request):
    return HttpResponse("Hello, world. You're at the home page.")

def file(request, name):
	matched_file = File.objects.filter(name__startswith=name).first()

	return HttpResponse(matched_file.contents)
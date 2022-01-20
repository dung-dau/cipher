from cProfile import label
from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=500)
    contents = forms.CharField(max_length=500)
    file = forms.FileField()

class DeleteFileForm(forms.Form):
    file_name = forms.CharField(label="file_name", max_length=500)
    contents = forms.CharField(label="file_contents", max_length=500)
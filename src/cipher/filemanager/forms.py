from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=500)
    contents = forms.CharField(max_length=500)
    file = forms.FileField()
from django.urls import path
from . import views

app_name = 'filemanager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>/', views.FileView.as_view(), name='file'),
    path('handleFile', views.handleFile, name='handleFile'),
    path('removeFile', views.removeFile, name="removeFile"),
]
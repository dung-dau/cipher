from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>/', views.FileView.as_view(), name='file'),
    path('handleFile', views.handleFile, name='handleFile'),
]
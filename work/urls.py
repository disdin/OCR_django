# task.urls.py

from django.urls import path
from work import views
 
urlpatterns = [
    path('upload/',views.uploadImage, name='upload'),
    path('runScrypt/',views.runScrypt, name='runScrypt'),
]
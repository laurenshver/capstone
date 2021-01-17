from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_tool.html', views.create_tool, name='form')
]
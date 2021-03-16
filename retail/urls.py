from django.urls import path
from . import views

urlpatterns = [
    path('retail.html', views.retail_index, name='retail index'),
    path('', views.index, name = 'homepage'),
]
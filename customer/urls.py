from django.urls import path

from . import views

urlpatterns = [
    # '' -> empty path, just at /customers, views.index -> says that retuned value of views.all_customers will be at the empty url
    path('', views.all_customers, name='customer list'),
]
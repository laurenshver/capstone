from django.urls import path

from . import views

urlpatterns = [
    # '' -> empty path, just at /customers, views.index -> says that retuned value of views.all_customers will be at the empty url
    path('patron.html', views.patrons, name = 'patron'),
    path('patron/<int:pk>/', views.PatronDetailView.as_view(), name='patrondetails'),
    path('business.html', views.businesses, name = 'business'),
    path('business/<int:pk>/', views.BusinessDetailView.as_view(), name='businessdetails')

]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='order summary'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='orderdetails'),
]
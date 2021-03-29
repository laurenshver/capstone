from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-invoice', views.select_order, name = 'selectorder'),
    path('add-to-invoice/<int:oid>/<int:cid>/', views.add_to_invoice, name='addinvoice'),
    path('remove-order/<str:oid>/', views.remove_from_invoice, name = 'removeorder'),
    path('generate-invoice/', views.generate_invoice, name='generate invoice'),
    path('invoice-details/<int:pk>/', views.new_invoice, name='new invoice'),
]